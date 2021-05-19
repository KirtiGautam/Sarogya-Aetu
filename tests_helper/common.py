from requests.exceptions import HTTPError, Timeout

# Mock response object with no sessions
no_resp = {
    "json": {
        "sessions": []
    },
    "status_code": 200
}

# Mock response object with a session
resp = {
    "json": {
        "sessions": [
            {
                "center_id": 1234,
                "name": "District General Hostpital",
                "name_l": "",
                "address": "45 M G Road",
                "address_l": "",
                "state_name": "Maharashtra",
                "state_name_l": "",
                "district_name": "Satara",
                "district_name_l": "",
                "block_name": "Jaoli",
                "block_name_l": "",
                "pincode": "562110",
                "lat": 28.7,
                "long": 77.1,
                "from": "09:00:00",
                "to": "18:00:00",
                "fee_type": "Paid",
                "fee": "250",
                "session_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                "date": "31-05-2021",
                "available_capacity": 50,
                "available_capacity_dose1": 25,
                "available_capacity_dose2": 25,
                "min_age_limit": 18,
                "vaccine": "COVISHIELD",
                "slots": [
                    "11:00AM-01:00PM"
                ]
            }
        ]},
    "status_code": 200
}

# Expected response object from vaccinator's get_bangalore_slots function
expected_resp = {
    'Pincode': '562110',
    'Name': "District General Hostpital",
    'Slot': '11:00AM-01:00PM'
}
