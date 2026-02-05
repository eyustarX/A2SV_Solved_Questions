class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        my_dict={}
        for domain in cpdomains:
            d=domain.split()
            my_dict[d[1]]=my_dict.get(d[1],0)+int(d[0])
            k=d[1].split('.')

            if len(k)==3:
                my_dict[k[-1]]=my_dict.get(k[-1],0) + int(d[0])
                my_dict[f"{k[-2]}.{k[-1]}"]=my_dict.get(f"{k[-2]}.{k[-1]}",0)+int(d[0])

            elif len(k)==2:
                my_dict[k[-1]]=my_dict.get(k[-1],0) + int(d[0])
                
        ans=[]
        for key,value in my_dict.items():
            ans.append(f"{value} {key}")
        
        return ans
            
