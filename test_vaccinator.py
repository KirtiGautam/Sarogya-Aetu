import pytest
from vaccinator import BASE_URL, get_bangalore_vaccine_slots
from tests_helper import case1, case2, case3
from requests.exceptions import Timeout, HTTPError

# Date for the test cases
date = "31-05-2021"

# Endpoint to get the slots by pincode.
url = f"{BASE_URL}/v2/appointment/sessions/public/findByPin"


@pytest.mark.parametrize('slot,expected_slots,pincode', case1.test_data)
def test_all_calls_success(requests_mock, slot, expected_slots, pincode):
    """
    This function tests the case where all calls to API returns success and check for following data return:
    i.  no slots
    ii. 1 slot available
    ii. 3 slots available
    """

    requests_mock.get(url, slot)

    response = get_bangalore_vaccine_slots(date, pincode)

    assert response == expected_slots


@pytest.mark.parametrize('slot,expected_slots,pincode', case2.test_data)
def test_some_timeouts(requests_mock, slot, expected_slots, pincode):
    """
    This function tests the case where some calls to API return timeouts(408) and check for following data return:
    i.  no slots
    ii. 3 slots available
    """

    requests_mock.get(url, slot)

    response = get_bangalore_vaccine_slots(date, pincode)

    assert response == expected_slots


@pytest.mark.parametrize('slot,expected_slots,pincode', case3.test_data)
def test_some_500s(requests_mock, slot, expected_slots, pincode):
    """
    This function tests the case where some calls to API return Server errors(500-599) and check for following data return:
    i.  no slots
    ii. 3 slots available
    """
    requests_mock.get(url, slot)

    response = get_bangalore_vaccine_slots(date, pincode)

    assert response == expected_slots


def test_all_timeouts(mocker):
    """
    This function tests the case where all calls to API return timeouts(408) and check for no data return
    """
    pincodes = case1.pincode_3
    mocker.patch('requests.get', side_effect=Timeout)

    response = get_bangalore_vaccine_slots(date, pincodes)

    assert response == []


def test_all_500s(mocker):
    """
    This function tests the case where all calls to API return server errors(500-599) and check for no data return
    """
    pincodes = case1.pincode_3
    mocker.patch('requests.get', side_effect=HTTPError)

    response = get_bangalore_vaccine_slots(date, pincodes)

    assert response == []
