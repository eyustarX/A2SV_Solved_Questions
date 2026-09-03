/**
 * @param {string} s
 * @return {string}
 */
var reverseVowels = function(f) {
    let s = f.split('')
    let array = ['a','e','i','o','u'];
    console.log(s)
    let left = 0, right = s.length - 1

    while (left < right) {
        while (left < right && !array.includes(s[left].toLowerCase())) {
            left++
        }
        while (left < right && !array.includes(s[right].toLowerCase())) {
            right--
        }
        [s[left], s[right]] = [s[right], s[left]]
        left++
        right--
    }

    return s.join('')
};