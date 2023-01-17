class Solution {
    public int[] solution(int numer1, int denom1, int numer2, int denom2) {
        numer1 *= denom2;
        numer2 *= denom1;
        int gcd = getGCD(numer1 + numer2, denom1 * denom2);
        int[] answer = {(numer1 + numer2)/gcd, denom1 * denom2/gcd};
        return answer;
    }
    
    public static int getGCD(int num1, int num2) {
        if (num1 % num2 == 0) {
            return num2;
        }
        return getGCD(num2, num1 % num2);
    }
}