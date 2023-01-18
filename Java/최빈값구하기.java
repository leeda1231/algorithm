import java.util.*;

class Solution {
    public int solution(int[] array) {
        Arrays.sort(array);
        int idx = array[array.length-1];
        int[] arr = new int[idx+1];
        for (int i=0; i<array.length; i++){
            arr[array[i]] += 1;
        }
        int answer = 0;
        int max = 0;
        int flag = 1;
        for (int j=0; j<arr.length; j++){
            if (max < arr[j]){
                max = arr[j];
                answer = j;
                flag = 0;
            }
            else if (max == arr[j]){
                flag = 1;
            }
        }
        if (flag == 1){
            answer = -1;
        }
        return answer;
    }
}