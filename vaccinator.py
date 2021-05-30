from typing import List
import requests
import bangalore.pincodes as bangalore_pincodes
from tabulate import tabulate
from fake_useragent import UserAgent

BASE_URL = "https://cdn-api.co-vin.in/api"

UA = UserAgent()

def get_slots_by_pincode(pincode: int, date: str) -> list:
    """
    Return the vaccination sessions available for given pincode and date
    :param pincode: 6-digit Indian pincode
    :param date: Date in DD-MM-YYYY format
    """

    # Setting headers for the API call, User-Agent is needed here due to API
    # returning 403 for normal python requests.
    # Refer https://github.com/cowinapi/developer.cowin/issues/19
    headers = {
        "accept": "application/json",
        "Accept-Language": "en_US",
        "User-Agent": UA.random
    }

    # Endpoint to get the slots by pincode.
    url = "/v2/appointment/sessions/public/findByPin"

    # Query params needed to fetch the slots
    payload = {
        "pincode": pincode,
        "date": date
    }

    # Setting timeout here if server take more than 2 seconds to respond
    timeout = 2

    # Hitting endpoint to get the data
    response = requests.get(f"{BASE_URL}{url}",
                            params=payload,
                            headers=headers,
                            timeout=timeout)

    # If there are some server errors, we need to catch them
    response.raise_for_status()

    # We only need sessions from the response
    return response.json()['sessions']


def get_bangalore_vaccine_slots(date: str, pincodes: List[int], bangalore: bool = True) -> list:
    """
    Returns the list of slots available based on given date and pincodes.
    Additionally, it can only be set for any region by setting bangalore as False 
    :param date: Date in DD-MM-YYYY format
    :param pincodes: list of 6-digit Indian pincodes
    :param pincodes: list of 6-digit Indian pincodes
    :param bangalore: bool flag to specify bangalore region
    """

    # List to hold the data
    schedules = []

    for pincode in pincodes:
        if  bangalore and pincode not in bangalore_pincodes.pincodes:
            # If pincode is not in Bangalore region,
            # we don't need to make the request
            continue
        try:
            sessions = get_slots_by_pincode(pincode, date)
            for session in sessions:
                schedules.extend([{
                    'Pincode': session['pincode'],
                    'Name': session['name'],
                    'Slot': slot} for slot in session['slots']])
        except (requests.exceptions.Timeout, requests.exceptions.HTTPError) \
                as e:
            print(e)
            pass

    return schedules


def driver():
    """
    This is the helper code to run the application using command line including
    instructions and inputs from user to return the data.
    """

    print('------------------------------------------------------------------'
          '-----------------------------------------')
    print('Press Ctrl+c anytime to exit or follow on screen instructions to'
          ' proceed.\n\nThis is Bangalore Vaccination slot enquiry facility.')
    print('-------------------------------------------------------------------'
          '-----------------------------------------')
    table_headers = ['Pincode', 'Name', 'Slot']
    while True:
        try:
            date = input("Enter date(DD-MM-YYYY) of enquiry ---> ")
            pincodes = list(map(int, input(
                "Enter space separated pincodes(eg.: 141010 562111) ---> ")
                .strip().split()))
            slots = get_bangalore_vaccine_slots(date, pincodes)
            data = [x.values() for x in slots]
            print(
                f'Slots available for bangalore pincodes in {pincodes} are as'
                'follows for date {date}:')
            print(tabulate(data, table_headers, tablefmt="grid",
                  numalign="center", stralign="center"))
        except Exception as e:
            print(f'Exception occured - {e.args}. Try again!')
        print('--------------------------------------------------------------'
              '-----------------------------------------')
        print('--------------------------------------------------------------'
              '----------------------------------------\n\n')


if __name__ == "__main__":
    driver()
