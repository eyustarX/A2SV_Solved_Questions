class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        dic = {}

        for response in responses:
            r = set(response)
            for i in r:
                dic[i] = dic.get(i, 0) + 1

        max_res = max(dic.values())

        dicc = sorted(dic)
        print(dicc)
        for key in dicc:
            if dic[key] ==  max_res:
                return key
            
