class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # initialize an object for the operations
        # [1, 2, 3, 3]
        self.k = k
        self.nums = nums

    def add(self, val: int) -> int:
        # add the given value to the nums 
        # return the kth largest integer in the stream
        # append the number to the end of nums
        # sort nums and return -kth element
        self.nums.append(val)
        self.nums.sort()
        return self.nums[-self.k]


