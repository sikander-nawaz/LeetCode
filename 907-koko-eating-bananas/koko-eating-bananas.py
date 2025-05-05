class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canEatAllBananas(speed: int) -> bool:
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / speed)
            return hours <= h
        
        left, right = 1, max(piles)
        while left < right:
            mid = (left + right) // 2
            if canEatAllBananas(mid):
                right = mid
            else:
                left = mid + 1
        
        return left