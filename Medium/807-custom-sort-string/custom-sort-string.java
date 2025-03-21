class Solution {
    public String customSortString(String order, String s) {
        int alpha[] = new int[26];
        for (int i = 0; i < s.length(); i++) alpha[s.charAt(i)-97]++;
        String ans = "";

        for (int i = 0; i < order.length(); i++){
            ans += ("" + String.valueOf(order.charAt(i)).repeat(alpha[order.charAt(i) - 97]));
            alpha[order.charAt(i) - 97] = 0;
        }

        for (int i = 0; i < 26; i++){
            ans += ("" + (char)(i + 97)).repeat(alpha[i]);
        }

        return ans;
    }
}