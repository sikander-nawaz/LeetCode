class Solution {
    public List<List<Integer>> permuteUnique(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        List<Integer> perm = new ArrayList<>();
        Map<Integer, Integer> count = new HashMap<>();
        for (int num : nums) {
            count.put(num, count.getOrDefault(num, 0) + 1);
        }
        dfs(nums, perm, count, res);
        return res;
    }
    
    private void dfs(int[] nums, List<Integer> perm, Map<Integer, Integer> count, List<List<Integer>> res) {
        if (perm.size() == nums.length) {
            res.add(new ArrayList<>(perm));
            return;
        }
        for (int num : count.keySet()) {
            if (count.get(num) > 0) {
                perm.add(num);
                count.put(num, count.get(num) - 1);
                dfs(nums, perm, count, res);
                perm.remove(perm.size() - 1);
                count.put(num, count.get(num) + 1);
            }
        }
    }
}