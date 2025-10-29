def normalize_isbn(s):
    s = s.replace(" ", "").replace("-", "")
    for i in s:
        if not (i.isdigit() or i == "X"):
            return ""
    if "X" in s[:-1]:
        return ""
    return s

def is_valid_isbn10(s):
    s = normalize_isbn(s)
    if len(s) != 10:
        return False
    total = 0
    for i, j in enumerate(s):
        value = 10 if j == "X" else int(j)
        total += value * (10 - i)
    return total % 11 == 0

def is_valid_isbn13(s):
    s = normalize_isbn(s)
    if len(s) != 13 or not s.isdigit():
        return False
    total = 0
    for i, j in enumerate(s):
        num = int(j)
        if i % 2 == 0:
            total += num
        else:
            total += num * 3
    return total % 10 == 0

def detect_isbn(s):
    s_norm = normalize_isbn(s)
    if is_valid_isbn10(s_norm):
        return "ISBN-10 normalizado: " + s_norm
    if is_valid_isbn13(s_norm):
        return "ISBN-13 normalizado: " + s_norm
    else:
        return "INVALIDO"

'''if __name__ == "__main__":
    s = input("ISBN: ")
    print(detect_isbn(s))'''

