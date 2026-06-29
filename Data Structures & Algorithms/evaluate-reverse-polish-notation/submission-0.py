class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        q = []
        for c in tokens:
            if c in '+-*/':
                r = q.pop()
                l = q.pop()
                tmp = 0
                if c == '+': tmp = l + r
                elif c == '-': tmp = l - r
                elif c == '*': tmp = l * r
                elif c == '/': tmp = int(l/r)
                q.append(tmp)
            else:
                q.append(int(c))
        return q.pop()