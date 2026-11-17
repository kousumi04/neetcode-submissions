class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        text=""
        for ch in s:
            if ch.isalnum():
                text+=ch
        return text==text[::-1]        