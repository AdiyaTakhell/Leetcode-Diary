def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    count = [0] * 26  # For 'a' to 'z'

    for ch_s, ch_t in zip(s, t):
        count[ord(ch_s) - ord("a")] += 1
        count[ord(ch_t) - ord("a")] -= 1

    return all(c == 0 for c in count)

#
# def isAnagram(s: str, t: str) -> bool
#     return sorted(s) == sorted(t)
