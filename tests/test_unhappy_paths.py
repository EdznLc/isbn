from src.isbn import is_valid_isbn10, is_valid_isbn13, normalize_isbn, detect_isbn

def test_isbn10_invalido():
    assert is_valid_isbn10("0306406153") == False   
    assert is_valid_isbn10("03A6406152") == False   

def test_isbn13_invalido():
    assert is_valid_isbn13("9780306406158") == False 
    assert is_valid_isbn13("97803A6406157") == False  

def test_normalize_x_invalid_position():
    assert normalize_isbn("03064061X2") == ""

def test_detect_invalid_general():
    # Cadena vacía (longitud 0)
    assert detect_isbn("") == "INVALIDO" 
    # Cadena corta (longitud 5)
    assert detect_isbn("12345") == "INVALIDO"