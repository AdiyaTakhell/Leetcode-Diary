def isSequence(s: str, t: str) -> bool:
    if not s:
        return True
    if len(s) > len(t):
        return False

    len_s, len_t = len(s), len(t)
    i, j = 0, 0

    while i < len_s and j < len_t:
        if s[i] == t[j]:
            i += 1
            if i == len_s:
                return True
        j += 1

    return i == len_s
