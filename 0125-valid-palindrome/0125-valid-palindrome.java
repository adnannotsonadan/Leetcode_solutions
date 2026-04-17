class Solution {
    public boolean isPalindrome(String s) {
        s=s.toLowerCase();
        s = s.replaceAll("[^a-z0-9]", "");
        int i=0;
        int end=s.length()-1;
        while(i<=end){
        if(s.charAt(i) != s.charAt(end)){
            return false;
        }
            i++;
            end--;

        }
        return true;
    }
}