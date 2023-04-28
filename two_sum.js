var twoSum = function(nums, target) {
    const indices = []
    for(let i = 0; i < nums.length - 1; i++){ 
        for(let j = 1; j < nums.length; j++){ 
            console.log(nums[i])
            console.log(nums[j])
            if(nums[i] + nums[j] === target) {
                indices.push(i)
                indices.push(j)
            }
        }
    }

    return indices
};

const nums = [3,2,4]
const target = 6
console.log(twoSum(nums, target))

//Future goal is to solve the problem in less that o(n^2) runtime