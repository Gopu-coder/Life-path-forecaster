# Numerology calculation module
# utils/numerology.py

def get_life_path_info(name: str, dob: str):
    from datetime import datetime

    # Extract Life Path Number from DOB
    def calculate_life_path_number(dob_str):
        dob_obj = datetime.strptime(dob_str, "%Y-%m-%d")
        total = sum(int(digit) for digit in dob_obj.strftime("%Y%m%d"))
        while total > 9 and total not in [11, 22, 33]:
            total = sum(int(d) for d in str(total))
        return total

    # Very simple version for demo
    def expression_number(name):
        name = name.upper().replace(" ", "")
        letter_map = {
            'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9,
            'J':1, 'K':2, 'L':3, 'M':4, 'N':5, 'O':6, 'P':7, 'Q':8, 'R':9,
            'S':1, 'T':2, 'U':3, 'V':4, 'W':5, 'X':6, 'Y':7, 'Z':8
        }
        total = sum(letter_map.get(c, 0) for c in name)
        while total > 9:
            total = sum(int(d) for d in str(total))
        return total

    life_path = calculate_life_path_number(dob)
    expr = expression_number(name)
    soul_urge = expression_number("".join([c for c in name if c in "AEIOUaeiou"]))

    return {
        "life_path_number": life_path,
        "expression_number": expr,
        "soul_urge_number": soul_urge
    }
