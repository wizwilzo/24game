class Solution:
    def solve(self, nums):
        def recurse(i, curr, par):
            if i >= len(nums) and par == 0:
                try:
                    return eval(curr) == 24
                except:
                    return False
            if i >= len(nums):
                return False

            if par > 0:
                # end parenthesis
                if recurse(i + 1, curr + "+" + str(nums[i]) + ")", par - 1):
                    return True
                if recurse(i + 1, curr + "*" + str(nums[i]) + ")", par - 1):
                    return True
                if nums[i] != 0 and recurse(i + 1, curr + "//" + str(nums[i]) + ")", par - 1):
                    return True
                if recurse(i + 1, curr + "-" + str(nums[i]) + ")", par - 1):
                    return True
            # regular
            if recurse(i + 1, curr + "+" + str(nums[i]), par):
                return True
            if recurse(i + 1, curr + "*" + str(nums[i]), par):
                return True
            if nums[i] != 0 and recurse(i + 1, curr + "//" + str(nums[i]), par):
                return True
            if recurse(i + 1, curr + "-" + str(nums[i]), par):
                return True
            # new parenthesis
            if recurse(i + 1, curr + "+(" + str(nums[i]), par + 1):
                return True
            if recurse(i + 1, curr + "*(" + str(nums[i]), par + 1):
                return True
            if nums[i] != 0 and recurse(i + 1, curr + "//(" + str(nums[i]), par + 1):
                return True
            if recurse(i + 1, curr + "-(" + str(nums[i]), par + 1):
                return True

            return False

        return recurse(1, str(nums[0]), 0) or recurse(1, "(" + str(nums[0]), 1)
