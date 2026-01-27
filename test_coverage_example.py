import pytest


@pytest.mark.parametrize("hr, age, expected", [
    (110, 10, "normal"),
    (180, 10, "tachycardic"),
    # (90, 20, "normal"),
    # (135, 20, "tachycardic"),
    ])
def test_tachycardia_analysis(hr, age, expected):
    from coverage_example import tachycardia_analysis
    answer = tachycardia_analysis(hr, age)
    assert answer == expected
