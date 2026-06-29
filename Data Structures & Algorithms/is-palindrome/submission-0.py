class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss = ''
        for c in s:
            if 'a' <= c <= 'z' or '0' <= c <= '9': ss+= c
            elif 'A' <= c <= 'Z': ss+= chr(ord(c)+(97-65))
        return ss == ss[::-1]