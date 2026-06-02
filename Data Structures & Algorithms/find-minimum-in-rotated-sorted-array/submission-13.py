class Solution:
    def findMin(self, nums: List[int]) -> int:
        # we have to return the minimum element in an array that
        # has been rotated n times => for n times, took num from end 
        # and put at beginning
        # [1,2,3,4,5,6]

        # [4,5,0,1,2,3]
        #      l
        #    m
        #      r
        # [3,4,5,6,1,2]
        #        l
        #        m
        #       r
        # total_min = 100000
        # we have to check if it's been rotated
            # nums[l] > nums[h]
        # if not rotated, normal binary search
        # if rotated, we have two halves to search
        # we have to determine which half to search
            # compare l and h, find smaller value
            # if h <= l:
                # l = m 
            # else:
                # r = m - 1
        # perform binary search on that half
        # how to find minimum 
            # total_min = min(total_min, nums[mid])
        # nums=[1]
        curr_min = nums[0]
        l, r = 0, len(nums)-1
        while l <= r: 
            if nums[l] < nums[r]:
                curr_min = min(curr_min, nums[l])
            mid = l + (r - l) // 2
            curr_min = min(curr_min, nums[mid])
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        return curr_min
            
            
        



                





        
        