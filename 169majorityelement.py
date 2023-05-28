def majorityElement(self, nums: list[int]) -> int:
        sol = None
        count = 0
        for i in nums:
            if count == 0:
                sol = i
            count += (1 if i == sol else -1)
        return sol
