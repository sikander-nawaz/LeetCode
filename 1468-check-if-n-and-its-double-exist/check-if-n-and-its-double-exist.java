class Solution {
    public boolean checkIfExist(int[] arr) {
        HashSet<Integer> set1=new HashSet<>();
        int n = arr.length;
            int zeroCount = 0;
        for(int i=0;i<n;i++){
            set1.add(arr[i]);

             if (arr[i] == 0) {
                zeroCount++;
            }
        }
         if (zeroCount > 1) {
            return true;
        }
    
       for(int i=0;i<n;i++){
           int value = arr[i]*2;
           if(set1.contains(value) && value != arr[i]){
               return true;
           }
       }
        return false;
    }
}