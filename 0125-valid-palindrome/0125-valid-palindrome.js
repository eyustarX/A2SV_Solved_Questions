/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(f) {
    let left = 0, right = f.length - 1;

    const isAlphaNum = (word) => /[a-z0-9]/i.test(word);

    while (left < right){
        while (left < right && !isAlphaNum(f[left])){
            left++;
        }

        while (left < right && !isAlphaNum(f[right])){
            right--;
        }

        if (f[left].toLowerCase() !== f[right].toLowerCase()){
            return false;
        }

        left++;
        right--;
    }

    return true
    
};
