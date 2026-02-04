class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        result=[]
        flag=True
        store=""

        for word in source:
            i=0
            while i<len(word):
                if flag and i+1<len(word) and word[i:i+2]=="/*":
                    flag=False
                    i+=2
                elif not flag and i+1<len(word) and word[i:i+2]=="*/":
                    flag=True
                    i+=2
                elif flag and i+1<len(word) and word[i:i+2]=="//":
                    break
                elif flag:
                    store+=word[i]
                    i+=1
                else:
                    i+=1
            if flag and store:
                result.append(store)
                store=""

        return result


        
