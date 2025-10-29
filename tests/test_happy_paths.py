from src.isbn import is_valid_isbn10, is_valid_isbn13

def test_isbn10_valido():
    assert is_valid_isbn10("0306406152") == True
    assert is_valid_isbn10("0-8044-2957-X") == True

def test_isbn13_valido():
    assert is_valid_isbn13("9780306406157") == True


from src.isbn import detect_isbn

def test_detect_isbn10_valido():
    assert detect_isbn("0306406152") == "ISBN-10 normalizado: 0306406152"