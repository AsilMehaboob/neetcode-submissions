class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length=0
        left=0
        right=len(s)-1
        seen=set()

        for right in range(len(s)):
            while s[right]  in seen:
                seen.remove(s[left])
                left+=1

            seen.add(s[right])
            length=max(right-left+1,length)

        return length