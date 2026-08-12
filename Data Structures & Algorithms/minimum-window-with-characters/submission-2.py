class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from typing import List

        # your code goes here
        # goal: find the smallest substring that has all chars in arr
        # t = ['A','B','C'],'ADOBECODEBANCDDD'
        #                       l
        #                           r
        # {x: 1, y: 1, z: 1}
        # {x: 0, y: 0, z: 0}
        # smallest = (3, "zyx")
        # need = 3
        # have = 0
        # ['A'],'B'
        count_arr = {}
        for char in t:
            count_arr[char] = count_arr.get(char, 0) + 1
        
        l = 0
        have = 0
        count_str = {}
        need = len(count_arr) 
        result = [float('inf'), ""]
        
        for r in range(len(s)):

            curr = s[r]
            if curr in count_arr:
                count_str[curr] = count_str.get(curr, 0) + 1


                if count_str[curr] == count_arr[curr]:
                    have += 1

            # shrinking to find smaller
            while have == need:
                window_size = r - l + 1
                if window_size < result[0]:
                    result = [window_size, s[l: r + 1]]
                # print(result)
                if s[l] in count_str:
                    count_str[s[l]] -= 1
                    if count_str[s[l]] < count_arr[s[l]]:
                        have -= 1
                l += 1
            

        return result[1]






        


