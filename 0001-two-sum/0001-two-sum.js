/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    let m={};
    let t=[];
    for (let i=0;i<nums.length;i++){
        let x=target-nums[i];
        if (!(x in m)){
            m[nums[i]]=i
        }else{
            t.push(m[x]);
            t.push(i);        
            return t;
        }
    }
};
//   let map = new Map()
//   let  n= nums.length

//   for(let i = 0 ; i<n ; i++){

//     let k = target - nums[i];

//     if(map.has(k)){
//         return [map.get(k) ,i];
//     }

//     map.set(nums[i] , i)
//   }

  
    