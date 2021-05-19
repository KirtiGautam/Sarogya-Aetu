from tests_helper.common import no_resp, resp, expected_resp
import random

error_resp = {
    "json": {},
    "status_code": random.randint(500, 599)
}

pincode_0 = [
    562110,
    561203,
    141010
]

pincode_3 = [
    562110,
    141010,
    562110,
    561203,
    561203,
]

slot_0 = [
    error_resp,
    no_resp,
    no_resp
]

slot_3 = [
    resp,
    resp,
    resp,
    error_resp,
    error_resp,
]

expected_slots_0 = []

expected_slots_3 = [
    expected_resp,
    expected_resp,
    expected_resp
]

test_data = [
    (
        slot_0,
        expected_slots_0,
        pincode_0
    ),
    (
        slot_3,
        expected_slots_3,
        pincode_3
    )
]
