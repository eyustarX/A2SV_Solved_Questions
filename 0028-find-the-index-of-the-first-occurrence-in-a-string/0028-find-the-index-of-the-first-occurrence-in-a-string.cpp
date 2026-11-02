class Solution {
public:
    int strStr(string haystack, string needle) {
        int i = haystack.find(needle[0]);
        int m = needle.length();
        
        for(i; i < haystack.length();i++){
            if(haystack.substr(i,m) == needle){
                return i;
            }
        }
        return -1;
    }
};