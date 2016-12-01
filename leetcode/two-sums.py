"""
    Given an array of integers, return indices of the two numbers such that they add up to a specific target.
    @author Jayesh
"""
class Solution(object):
    def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash = {}
        i = 0
        for n in nums:
            if hash.has_key(n):
                hash[n].append(i)
            else:
                hash[n] = [i]
            i = i + 1

        for k,v in hash.items():
            pair = (target - k)
            if hash.has_key(pair):
                possibilities = hash[pair]

                for o in v:
                    for p in possibilities:
                        if o != p:
                            return o, p

        raise Exception("No match found")


# Test
# if __name__ == "__main__":
#         print(twoSum([0, 4, 3, 0], 0))
