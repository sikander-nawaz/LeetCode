class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        sorted_people = sorted(zip(heights, names), reverse=True)
        sorted_names = [name for height, name in sorted_people]
        return sorted_names
