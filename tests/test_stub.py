from unittest.mock import patch
from src.isbn import detect_isbn

@patch('src.isbn.is_valid_isbn10')
def test_detect_isbn_stub_forces_isbn10_pass(mock_is_valid_isbn10):
    """
    Simula que is_valid_isbn10 siempre retorna True, probando la ruta de éxito
    en detect_isbn sin depender de la fórmula de checksum.
    """
    mock_is_valid_isbn10.return_value = True

    resultado = detect_isbn("1234567890") 

    assert resultado == "ISBN-10 normalizado: 1234567890"

    mock_is_valid_isbn10.assert_called_once()