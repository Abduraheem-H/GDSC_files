public class Solution {
    public int romanToInt(String s) {
        int result = 0;

        for (int i = s.length() - 1; i >= 0; i--) {
            char c = s.charAt(i);
            if (c == 'I') {
                result += (result >= 5 ? -1 : 1);
            } else if (c == 'V') {
                result += 5;
            } else if (c == 'X') {
                result += 10 * (result >= 50 ? -1 : 1);
            } else if (c == 'L') {
                result += 50;
            } else if (c == 'C') {
                result += 100 * (result >= 500 ? -1 : 1);
            } else if (c == 'D') {
                result += 500;
            } else if (c == 'M') {
                result += 1000;
            }
        }

        return result;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        String romanNumeral = "XXVII";
        System.out.println("The integer value of " + romanNumeral + " is: " + solution.romanToInt(romanNumeral));
    }
}
