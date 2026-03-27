class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hash_map = {'2':"abc",'3':"def",'4':"ghi",'5':"jkl",'6':"mno", '7':"pqrs", '8':"tuv",'9':"wxyz"}

        ans = []
        n = len(digits)

        def backtracking(index,comb):
            if len(comb) == n:
                ans.append(comb[:])
                return
            
            for i in range(len(hash_map[digits[index]])):
                comb += hash_map[digits[index]][i]
                backtracking(index + 1, comb)
                comb= comb[:-1]

        backtracking(0, "")

        return ans