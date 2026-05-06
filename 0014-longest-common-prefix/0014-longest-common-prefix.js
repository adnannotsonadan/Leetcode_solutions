/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
    // if (strs.length===1){
    //     return strs[0];
    // }
    // strs.sort();
    // let i=0
    // let first=strs[0];
    // let last=strs[strs.length-1];
    // s='';
    // while (first[i]===last[i]){
    //     s+=first[i];
    //     i++;
    // }
    // return s;
    s='';
    if (strs.length===1){
        return strs[0];
    }
    strs.sort();
    let first=strs[0];
    let last=strs[strs.length-1];

    for (let i=0;i<first.length;i++){
        if (first[i]===last[i]){
            s+=first[i];
        }else{
            break;
        }

        }
    return s;
};