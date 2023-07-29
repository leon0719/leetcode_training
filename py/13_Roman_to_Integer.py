symbol_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

Two_sysbol_map = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}


def Roman_to_Integer(s: str) -> int:
    i = 0
    result = 0
    while i < len(s):
        if s[i : i + 2] in Two_sysbol_map:
            result += Two_sysbol_map[s[i : i + 2]]
            i += 2
        else:
            result += symbol_map[s[i]]
            i += 1
    return result


# unit test Roman_to_Integer


def test_Roman_to_Integer():
    assert Roman_to_Integer("III") == 3
    assert Roman_to_Integer("IV") == 4
    assert Roman_to_Integer("IX") == 9
    assert Roman_to_Integer("LVIII") == 58
    assert Roman_to_Integer("MCMXCIV") == 1994
