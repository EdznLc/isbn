from src.isbn import normalize_isbn, detect_isbn

def test_idempotencia():
    s = "978-0-306-40615-7"
    assert normalize_isbn(normalize_isbn(s)) == normalize_isbn(s)

def test_equivalencia():
    con_guiones = "978-0-306-40615-7"
    sin_guiones = "9780306406157"
    assert detect_isbn(con_guiones) == detect_isbn(sin_guiones)