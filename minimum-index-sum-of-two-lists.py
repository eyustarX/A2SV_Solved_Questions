class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        my_dict={}

        for word in list1:
            if word in list2:
                i=list1.index(word)
                j=list2.index(word)
                my_dict[word] = i+j
        values=[n for n in my_dict.values()]
        values.sort()

        ans=[]
        for key in my_dict.keys():
            if my_dict[key]==values[0]:
                ans.append(key)
        
        return ans
        
