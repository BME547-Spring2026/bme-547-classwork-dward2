import pytest


@pytest.mark.parametrize("weight_input, expected", [
    ("22 lb", 10),
    ("50 kg", 50)])
def test_parse_weight_input(weight_input, expected):
    from weight_entry import parse_weight_input
    answer = parse_weight_input(weight_input)
    assert answer == expected
