import java.util.*;

class Solution {
    public List<Integer> solution(int n) {
        List<Integer> answer = new ArrayList<Integer>();
        for (int i=1;i<n+1;i+=2){
            answer.add(i);
        }
        return answer;
    }
}