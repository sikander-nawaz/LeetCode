class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        count = 0
        
        for j in range(n):
            count_less = count_greater = 0
            count_more = count_smaller = 0
            
            for i in range(j):
                if rating[i] < rating[j]:
                    count_less += 1
                if rating[i] > rating[j]:
                    count_more += 1
            
            for k in range(j + 1, n):
                if rating[k] > rating[j]:
                    count_greater += 1
                if rating[k] < rating[j]:
                    count_smaller += 1
            
            count += count_less * count_greater
            count += count_more * count_smaller
        
        return count
