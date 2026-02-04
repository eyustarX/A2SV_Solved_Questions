#User function Template for python3

class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        # Your code here
        dict_a={}
        
        for n in a:
            dict_a[n]=dict_a.get(n,0)+1
        
        for x in b:
            if dict_a.get(x,0)==0:
                return False
            
            dict_a[x]-=1
        
        return True

    
    
    
