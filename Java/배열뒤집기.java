class Solution1 {
    public int[] solution(int[] num_list) {
        int n = num_list.length;
        int[] answer = new int[n];
        for (int i=0;i<n;i++){
            answer[n-i-1] = num_list[i];
        }
        return answer;
    }
}


import java.util.*;
import java.util.stream.*;
class Solution2 {
    public int[] solution(int[] num_list) {
        List<Integer> list = Arrays.stream(num_list).boxed().collect(Collectors.toList());
        Collections.reverse(list);
        int[] answer = list.stream().mapToInt(i->i).toArray();
        return answer;
    }
}