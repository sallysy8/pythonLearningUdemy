"""
    @param s: A string
    @return: Whether the string is a valid palindrome
"""

def isPalindrome(s):
    # write your code here
    if len(s) <= 1:
        return True
    else:
        new_s = s.lower()
        i = 0
        j = new_s[-1]
        while i < j:
            while new_s[i].isalnum() is True:
                i+=1
            while new_s[j].isalnum() is True:
                j-=1
            if new_s[i] != new_s[j]:
                return False
        return True
