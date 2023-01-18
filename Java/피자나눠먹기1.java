class Solution {
    public int solution(int n) {
        int answer = 1;
        answer += n/7;
        if (n%7==0){
            answer -= 1;
        }
        return answer;
    }
}