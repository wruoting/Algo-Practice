import math
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == '':
            return ''
        palindrome_index = 0
        longest_odd_palindrome_length = 1
        longest_even_palindrome_length = 0
        for index, character in enumerate(s):
            # longest even
            max_side_to_side = int(math.floor(longest_even_palindrome_length/2)) + 1
            left_index = index - max_side_to_side + 1
            right_index = index + max_side_to_side
            add_palindrome = True
            while add_palindrome:
                if left_index >= 0 and right_index < len(s)-1:
                    for i in range(left_index, index+1):
                        if s[i] != s[right_index-i]:
                            add_palindrome = False
                            break
                    if add_palindrome:
                        longest_even_palindrome_length += 2
                        even_palindrome_index = index
                        left_index-=1
                        right_index+=1
                else:
                    add_palindrome = False
                    
            # longest odd palindrome
            max_side_to_side = int(math.floor(longest_odd_palindrome_length/2))
            left_index = index - max_side_to_side
            right_index = index + max_side_to_side
            add_palindrome = True
            while add_palindrome:
                if left_index > 0 and right_index < len(s)-1:
                    for i in range(left_index-1, index):
                        if s[i] != s[index+index-i]:
                            add_palindrome = False
                            break
                    if add_palindrome:     
                        longest_odd_palindrome_length += 2
                        odd_palindrome_index = index
                        left_index-=1
                        right_index+=1
                else:
                    add_palindrome = False
        if longest_even_palindrome_length > longest_odd_palindrome_length:
            max_side_to_side = int(math.floor(longest_even_palindrome_length/2))
            left_index = even_palindrome_index - max_side_to_side + 1
            right_index = even_palindrome_index + max_side_to_side
        elif longest_odd_palindrome_length > longest_even_palindrome_length:
            max_side_to_side = int(math.floor(longest_odd_palindrome_length/2))
            left_index = odd_palindrome_index - max_side_to_side
            right_index = odd_palindrome_index + max_side_to_side
        return s[left_index:right_index+1]


s = "a"
a = Solution()
print(a.longestPalindrome(s))