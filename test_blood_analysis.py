import pytest


@pytest.mark.parametrize("hdl_value, expected", [
     (65, "Normal"),
     (45, "Borderline Low"),
     (20, "Low")
     ])
def test_check_HDL(hdl_value, expected):
    # arranges
    from blood_analysis import check_HDL
    # acts
    answer = check_HDL(hdl_value)
    # asserts
    assert answer == expected


@pytest.mark.parametrize("ldl_value, expected", [
    (100, "Normal"),
    (135, "Borderline High"),
    (165, "High"),
    (200, "Very High")])
def test_check_LDL(ldl_value, expected):
    from blood_analysis import check_LDL
    answer = check_LDL(ldl_value)
    assert answer == expected


"""
conda activate envname

conda install -c conda-forge pytest
conda install -c conda-forge pytest-pycodestyle

"""
