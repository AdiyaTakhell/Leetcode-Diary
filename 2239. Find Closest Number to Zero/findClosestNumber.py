def findClosestNumber(nums: list[int]) -> int:
    closest = nums[0]
    for i in range(len(nums)):
        if nums[i] < closest:
            closest = nums[i]
        elif nums[i] == closest and closest < nums[i]:
            closest = nums[i]
    return closest
