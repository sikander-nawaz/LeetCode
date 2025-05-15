class Solution {
    public int findJudge(int n, int[][] trust) {
        int[] a = new int[n+1];
        int[] b = new int[n+1];

        for(int temp[] : trust){
            b[temp[0]]++;
            a[temp[1]]++;
        }

        for(int i=1;i<=n;i++){
            if(b[i] == 0 && a[i] == n-1)   return i;
        }
        return -1;
    }
}