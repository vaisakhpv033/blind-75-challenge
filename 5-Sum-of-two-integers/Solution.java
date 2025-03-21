// link: https://leetcode.com/problems/sum-of-two-integers/description/
class Solution {
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.getSum(1, 2));
    }

    public int getSum(int a, int b) {
        while (b != 0){
            int temp = (a&b) << 1;
            a = a ^ b;
            b = temp;
        }
        return a;
    }
}