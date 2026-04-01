class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def isValid(st):
            count = 0
            for c in st:
                if c == '(':
                    count += 1
                elif c == ')':
                    count -= 1
                    if count < 0:
                        return False
            
            return count == 0
        
        self.max_len = 0
        self.res = set()

        def backtracking(i, path):
            if len(path) + len(s) - i < self.max_len:
                return 
            
            if i == len(s):
                if isValid(path):
                    if len(path) > self.max_len:
                        self.max_len = len(path)
                        self.res = set()
                        self.res.add(path)
                    elif len(path) == self.max_len:
                        self.res.add(path)

                return
            
            if s[i] in "()":
               backtracking(i + 1, path)
            
            backtracking(i + 1, path + s[i])
        
        backtracking(0, "")

        return list(self.res)