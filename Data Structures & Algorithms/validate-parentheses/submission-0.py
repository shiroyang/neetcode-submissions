class Solution:
    def isValid(self, s: str) -> bool:
        que = []
        for c in s:
            if c in '([{':
                que.append(c)
            else:
                if not que: return False
                cur = que.pop()
                if cur == '(' and c == ')': continue
                if cur == '[' and c == ']': continue
                if cur == '{' and c == '}': continue
                return False
        return True if not que else False