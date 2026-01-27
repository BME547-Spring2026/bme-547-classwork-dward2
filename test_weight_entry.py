import pytest


@pytest.mark.parametrize("weight_input, expected", [
    ("22 lb", 10),
    ("50 kg", 50),
    ("22.1 lb", 10),
    ("22", -99),
    ("22 lbs", 10),
    ("50 kgs", 50),
    # ("ten kg", 10),
    ("22 LB", 10),
    ("50 KG", 50),
    ("22 Lb", 10),
    ("50 kG", 50),
    ("22 pound", 10),
    ("22 pounds", 10),
    ("50 kilograms", 50),
    ("-22 lb", -10),
    ("0 lb", 0),
    ("10000000 kg", -99)])
def test_parse_weight_input(weight_input, expected):
    from weight_entry import parse_weight_input
    answer = parse_weight_input(weight_input)
    assert answer == expected
