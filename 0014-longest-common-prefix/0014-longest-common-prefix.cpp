class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string shortest = strs[0];

        for(string word: strs){
            if(word.length() < shortest.length()){
                shortest = word;
            }
        }

        for(int i = 0; i < shortest.length(); i++){
            for(string word: strs){
                if(shortest[i] != word[i]){
                    return shortest.substr(0,i);
                }
            }
        }
        return shortest;
    }
};