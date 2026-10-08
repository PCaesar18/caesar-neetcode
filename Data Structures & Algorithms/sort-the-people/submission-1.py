class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        people = zip(heights,names)
        people_sorted = sorted(people, reverse=True)
        
        return [name for height, name in people_sorted]