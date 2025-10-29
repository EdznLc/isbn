import pytest

@pytest.fixture
def ejemplos_isbn():
    return {
        "isbn10_valido": "0306406152",
        "isbn10_invalido": "0306406153",
        "isbn13_valido": "9780306406157",
        "isbn13_invalido": "9780306406158"
    }

def test_con_fixture(ejemplos_isbn):
    from src.isbn import is_valid_isbn10
    assert is_valid_isbn10(ejemplos_isbn["isbn10_valido"]) == True
    assert is_valid_isbn10(ejemplos_isbn["isbn10_invalido"]) == False
