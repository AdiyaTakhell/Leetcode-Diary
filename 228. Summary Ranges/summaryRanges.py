def summaryRanges(nums: list[int]) -> list[str]:
    start = 0
    output = []
    for i in range(len(nums)):
        if i == len(nums) - 1 or nums[i + 1] - nums[i] != 1:
            if nums[start] == nums[i]:
                output.append(str(nums[start]))
            else:
                output.append(f"{nums[start]}->{nums[i]}")
            start = i + 1
    return output


