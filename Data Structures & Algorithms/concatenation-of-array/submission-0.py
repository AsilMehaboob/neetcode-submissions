class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans=[]

        ans[0:len(nums)]=nums
        ans[len(nums):2*len(nums)]=nums

        return ans
