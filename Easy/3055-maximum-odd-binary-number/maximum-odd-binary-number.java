class Solution {
    public String maximumOddBinaryNumber(String s) {
        char[] ch = s.toCharArray();
        char[] result = new char[s.length()];
        int countZeroes = 0;
        int countOnes = 0;
        for (int i = 0; i < ch.length; i++) {
            if (ch[i] == '1') countOnes ++;
        }
        result[s.length()-1] = '1';
        countOnes--;
        int index = 0;
        while (countOnes != 0 && (index <= s.length() - 2)) {
            result[index] = '1';
            index++;
            countOnes--;
        }
        while (index <= s.length() - 2) {
            result[index] = '0';
            index++;
        }
        return String.copyValueOf(result);
    }
}