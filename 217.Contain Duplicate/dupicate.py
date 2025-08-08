def containsDuplicate(nums: list[int]) -> bool:
    nums1 = set(nums)
    return len(nums) != len(nums1)