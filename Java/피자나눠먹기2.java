class Solution {
    public int solution(int n) {
        int answer = n/gcd(n,6);
        return answer;
    }
    
    public int gcd(int n1,int n2){
        if (n1 % n2 == 0){
            return n2;
        }
        return gcd(n2,n1%n2);
    }
}