class Solution:
    # encode: len(word)+'#'+word
    def encode(self, strs: List[str]) -> str:
        ans = ''
        for s in strs:
            n = len(s)
            ans += str(n) + '#' + s
        return ans
    def decode(self, s: str) -> List[str]:
        ans = []
        n = len(s)
        i = 0
        while i < n:
            j = i
            num = ''
            # extract till #
            while s[j] != '#': j += 1
            num = int(s[i:j])
            # j is '#', word should be s[j+1:j+num+1]
            ans.append(s[j+1:j+num+1])
            i = j + num + 1
        return ans