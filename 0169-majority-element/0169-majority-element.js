/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    let num=null;
    let counter=0
    for (x of nums){
        if (counter===0){
            num=x;
            counter++
        }else{
            if (num===x){
                counter++;
            }else{
                counter--;
            }
        }
    }
    return num;
    
};