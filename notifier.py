from typing import List
from vaccinator import get_bangalore_vaccine_slots
from notifier.notifier_data import MOBILE_DATA, API_URL, PINCODES
from datetime import date
from tabulate import tabulate
from time import sleep
import requests


def chunkify(text: str, key: int) -> List[str]:
    """
    Creates chunks of data coming to send, callmebot allows only
    768 characters at one call
    """
    chunks = []
    n = 0
    while n < len(text):
        chunks.append({
            "apikey": key,
            'text': text[n:n+768]
        })
        n += 768
    return chunks

def whatsappMe():
    """
    This function calls get_bangalore_vaccine_slots to get the data
    and sends to the mobile number mentioned in data
    """
    
    # Get slots 
    slots = [x.values() for x in 
            get_bangalore_vaccine_slots(date.today().strftime('%d-%m-%Y'), 
            PINCODES, False)]

    table_headers = ['Pincode', 'Name', 'Slot']

    Text = f'{tabulate(slots, table_headers, tablefmt="grid", numalign="center", stralign="center")}\nTotal slots available: {len(slots)}' 

    # Setting timeout here if server take more than 2 seconds to respond
    timeout = 2

    # Query params needed to send data
    for data in MOBILE_DATA:
        if not data['MOBILE']: continue
        for payload in chunkify(Text, data['API_KEY']):
            try:
                # Hitting endpoint to send the data
                response = requests.get(f'{API_URL}?phone={data.get("MOBILE")}',
                                        params=payload,
                                        timeout=timeout)
                response.raise_for_status()
                print(data['MOBILE'], data['API_KEY'])#, response.text)
            except (requests.exceptions.Timeout, requests.exceptions.HTTPError) \
                    as e:
                print('Swallowed - ' + e.args)
                pass
        sleep(1)


if __name__ == "__main__":
    while(True):
        whatsappMe()
        sleep(3600)
    