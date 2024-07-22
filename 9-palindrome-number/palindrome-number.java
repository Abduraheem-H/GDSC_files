class Solution {
    public boolean isPalindrome(int x) {
        String strX= Integer.toString(x);
        int left=0;
        int right=strX.length()-1;
        while(left<right){
            if (strX.charAt(left)!=strX.charAt(right))
            return false;
            else {
                left++;
                right--;
            }
        }
        return true;
  

   
}

}