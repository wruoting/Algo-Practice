class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest_dict = {}
        init = 0
        longest_set_length = 0
        for index, character in enumerate(s):
            if longest_dict.get(character) is not None:
                if init < longest_dict.get(character) + 1:
                    init = longest_dict.get(character) + 1
            if (index - init + 1) > longest_set_length:
                longest_set_length = index - init + 1
            longest_dict[character] = index
        return longest_set_length
            
s = "fasfafdvxxxxvdefffassvxz"
a = Solution()
print(a.lengthOfLongestSubstring(s))