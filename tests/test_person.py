import pytest
from beings import Person

@pytest.fixture()
def person():
    return Person("Gurbinder Holait",54,jobs=["Software Engineer"])

def test_init(person : Person):

    assert person.name == "Gurbinder Holait"
    assert person.age == 54
    assert person.jobs == ["Software Engineer"]

def test_forname(person : Person):
    assert person.forename == "Gurbinder"

def test_surname(person : Person):
    assert person.surname == "Holait"

def test_celebrate_birthday (person : Person):
    person.celebrate_birthday()
    assert person.age == 55

def test_add_job (person : Person):
    person.add_job("ZooKeeper")
    assert person.jobs == ["Software Engineer", "ZooKeeper"]

def test_no_surname (person : Person):
    person.name = "Gubby"
    assert not person.surname