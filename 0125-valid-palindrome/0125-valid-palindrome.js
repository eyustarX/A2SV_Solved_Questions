/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(f) {
    const s = f.toLowerCase().replace(/[^a-z0-9]/g, "")

    let left = 0
    let right = s.length - 1
    console.log(s)
    while (left < right){
        if (s[left]!== s[right]){
            return false
        }
        left += 1
        right -= 1
    }

    return true
    
};
