/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    if (s.length!==t.length){
        return false;
    }
    let m={};
    let n={};

    for (let i=0;i<s.length;i++){
        if (!(s[i] in m)){
            m[s[i]]=1
        }else{
            m[s[i]]++;
        }
    }
    
    for (let i=0;i<t.length;i++){
        if (!(t[i] in m) || m[t[i]]===0){
            return false;
        }
            m[t[i]]--;
        }
        return true;
    


};