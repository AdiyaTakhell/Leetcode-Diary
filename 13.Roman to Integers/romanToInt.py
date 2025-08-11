def romanToInt(s: str) -> int:
    roman_to_int = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total_value = 0
    i = 0
    n = len(s)

    while i < n:
        current_val = roman_to_int[s[i]]
        if i + 1 < n and current_val < roman_to_int[s[i + 1]]:
            total_value += roman_to_int[s[i + 1]] - current_val
            i += 2
        else:
            total_value += current_val
            i += 1

    return total_value
