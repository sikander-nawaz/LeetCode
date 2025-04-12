class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        List<Integer> digits = new ArrayList<>();
        for (int i = 0; i < nums1.length; i++) {
            for (int j = 0; j < nums2.length; j++) {
                if (nums1[i] == nums2[j]) {
                    digits.add(nums1[i]);
                }
            }
        }
        Set<Integer> ans = new HashSet<>(digits);
        int[] result = new int[ans.size()];
        int index = 0;
        for (int num : ans) {
            result[index++] = num;
        }
        return result;
    }
}
