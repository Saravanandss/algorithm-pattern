"""Valid Palindrome — converging two-pointer with skip pattern.

    Pattern: pointers from both ends skip non-alphanumeric characters, then
    compare case-insensitively and converge.

    Key details learned the hard way:
    - Inner skip loops MUST carry the `i < j` bound, or an all-punctuation
    input walks an index off the end of the string (IndexError).
    - With correct guards, the empty string naturally falls through to True

    Time: O(n)  Space: O(1)
"""

def is_palindrome(s:str) -> bool:
    """Return True if s is a palindrome over alphanumerics, ignoring case.

    >>> is_palindrome("A man, a plan, a canal: Panama")
    True
    >>> is_palindrome("race a car")
    False
    """
    i = 0
    j = len(s) - 1
    
    while i < j:
        while i < j and not s[i].isalnum():
            i += 1
            
        while i < j and not s[j].isalnum():
            j -= 1
        
        if s[i].lower() != s[j].lower():
            return False

        i += 1
        j -= 1

    return True

if __name__ == "__main__":
    assert not is_palindrome("Panama")
    assert is_palindrome("20man n-am02")
    assert isPalindrome("")
    assert isPalindrome("A man, a plan, a canal: Panama")
    assert isPalindrome("nn")
    assert isPalindrome("n")
    assert isPalindrome(".,")