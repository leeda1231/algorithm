class Solution {
    public int solution(int price) {
        int answer = 0;
        if (price < 100000){
            answer = price;
        }
        else if (price < 300000){
            answer = (int) (price * 0.95); 
        }
        else if (price < 500000){
            answer = price * 9 / 10;
        }
        else{
            answer = price * 8 / 10;
        }
        return answer;
    }
}