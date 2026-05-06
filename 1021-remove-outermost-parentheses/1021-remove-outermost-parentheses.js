/**
 * @param {string} s
 * @return {string}
 */
var removeOuterParentheses = function(s) {
        let count=0;
        let t="";
        for (let num of s){
            if (num==='('){
                count++;
                if (count>1){
                    t+='(';
                }
            }else{
                count--;
                if (count>0){
                    t+=num;
                }
            }
        }
        return t; 
       
       
};