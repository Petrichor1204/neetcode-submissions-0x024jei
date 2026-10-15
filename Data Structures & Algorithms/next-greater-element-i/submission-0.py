class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # goal: return an array of indexes where each index is the index of the next greater element of that num1 element in nums2
        # nums1 = [4,1,2], nums2 = [1,3,4,2,5,6]
        #                                   j
        #            i
        # [4,2]
        # {4:0, 1:1, 2:2}
        # [-1,3,-1]

        # dict for indexes, stack for next greater element
        res = [-1] * len(nums1)
        stack = []
        indices = {}
        for i, n in enumerate(nums1):
            indices[n] = i

        for i, n in enumerate(nums2):
            while stack and n > stack[-1]:
                index = indices[stack[-1]]
                res[index] = n
                stack.pop()
            if n in indices:
                stack.append(n)
                
        return res