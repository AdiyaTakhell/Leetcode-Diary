def find(nums1, nums2):
    r = sorted(nums1 + nums2)
    l = len(r) // 2
    if len(r) % 2 == 0:
        return float((r[l - 1] + r[l]) / 2)
    else:
        return r[l]



