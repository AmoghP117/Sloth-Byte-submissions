code = input("Enter a hex code: ").lower()
def is_valid_hex_code(code):
    validhex = "0123456789abcdef"
    if code[0] != "#" and len(code) != 7:
        return False
    
    for c in code[1:]:
        if c not in validhex:
               return False
    return True
print(is_valid_hex_code(code))
