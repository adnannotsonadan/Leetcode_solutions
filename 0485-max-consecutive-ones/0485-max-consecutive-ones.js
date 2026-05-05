/**
 * @param {number[]} nums
 * @return {number}
 */
var findMaxConsecutiveOnes = function(nums) {
    let maxi=0;
    let count=0;
    for (let num of nums){
        if (num===1){
            count++;
            maxi=Math.max(maxi,count)
        }else{
            count=0;
        }
    }
    return maxi;
};