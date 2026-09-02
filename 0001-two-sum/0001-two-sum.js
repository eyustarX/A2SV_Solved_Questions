/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    let hash_map = new Map()

    for (let i = 0; i < nums.length; ++i){
        let k = target - nums[i]

        if (hash_map.has(nums[i])){
            return [hash_map.get(nums[i]), i]
        }

        hash_map.set(k,i)
    }
};