import pytest
from src.gender_detector import GenderDetector


@pytest.fixture
def nome_payload_data():
    return "Ricardo"

def test_should_return_female_when_name_is_female_gender():
    detector = GenderDetector()
    expect_gender = detector.run("Ana")
    assert expect_gender == "female"

def test_should_return_male_when_name_is_male_gender():
    detector = GenderDetector()
    expect_gender = detector.run("Ricardo")
    assert expect_gender == "male"

def test_should_return_female_when_name_is_sayuri():
    detector = GenderDetector()
    expect_gender = detector.run("Sayuri")
    assert expect_gender == "female"