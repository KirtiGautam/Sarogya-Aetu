from tests_helper.common import no_resp, resp, expected_resp

pincode_0 = [
    562110,
    561203,
    141010
]

pincode_1 = [
    562110,
    141010
]

pincode_3 = [
    562110,
    562110,
    561203,
    141010
]

slot_0 = [
    no_resp,
    no_resp,
    no_resp,
]

slot_1 = [
    resp,
    no_resp
]

slot_3 = [
    resp,
    resp,
    resp,
    no_resp
]

expected_slots_0 = []

expected_slots_1 = [
    expected_resp
]

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
        slot_1,
        expected_slots_1,
        pincode_1
    ),
    (
        slot_3,
        expected_slots_3,
        pincode_3
    ),
]
