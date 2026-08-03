class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # find the minimum number of boats it will take to carry weights
        # people = [5,1,4,2], limit = 4
        #          [3]
        #           l
        #         r
        # boats = 1

        people.sort()

        l = 0
        r = len(people) - 1
        boats = 0

        while l <= r:
            if people[l] + people[r] <= limit:
                boats += 1
                l += 1
                r -= 1
            else:
                boats += 1
                r -= 1

        return boats


