class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # goal: is to return the k closest elements to x 
            # |a - x| < |b - x|, or
            # |a - x| == |b - x| and a < b
            
        # arr = [0], k = 1, x = 8
        #        l 
        #        r
        
        l = 0
        r = len(arr) - 1

        while l <= r:
            # if l is closer, move r
            if (r - l + 1) == k:
                return arr[l:r + 1]

            if abs(arr[l] - x) < abs(arr[r] - x):
                r -= 1

            # if r is closer, move l
            elif abs(arr[r] - x) < abs(arr[l] - x):
                l += 1

            # elif abs(arr[l] - x) == abs(arr[r] - x)
            else:
                if arr[l] < arr[r]:
                    r -= 1
                else:
                    l += 1




            


            
            # if window is == k: put them in a list and return them

        

