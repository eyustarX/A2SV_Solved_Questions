class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        arr=[]
        ans=[]
        my_dict={}
        for path in paths:
            root=path.split()
            f=root[0]
            for i in range(1,len(root)):
                k=root[i].split('.')
                m=k[1].split('(')
                n=m[1].split(')')
                j=f"{f}/{k[0]}.txt"
                arr.append([j,n[0]])
        
        for a in arr:
            my_dict[a[1]]=my_dict.get(a[1],0)+1

        for key in my_dict.keys():
            an=[]
            if my_dict[key]>1:
                for a in arr:
                    if key==a[1]:
                        an.append(a[0])
            if an:
                ans.append(an)
    
        return ans
