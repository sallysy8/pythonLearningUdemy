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
        j = len(new_s) - 1
        while i < j:
<<<<<<< HEAD
            while i < j and new_s[i].isalnum() is False:
                i += 1
            while i < j and new_s[j].isalnum() is False:
                j -= 1
            if new_s[i] != new_s[j]:
                return False
            else:
                i += 1
                j -= 1
=======
            while new_s[i].isalnum() is False
                i+=1
            while new_s[j].isalnum() is False:
                j-=1
            if new_s[i] != new_s[j]:
                return False
            else:
                i+=1
                j+=1
>>>>>>> 5859f4ae971a530ede8bd425c6652b3703e30938
        return True


assert isPalindrome('asjffjsa') == True
print('test pass')
