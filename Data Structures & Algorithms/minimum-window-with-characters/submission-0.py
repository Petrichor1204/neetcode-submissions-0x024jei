class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # sliding window - shrinking \\ expanding
        # s="AADDABECODEBANC"   # t="ABC"
        #      l
        #          r
        # shrink - found all letters
        # expand - to find all letters
        # minlen = 6     0, 5
        # have = 3
        # t = {a:1, b:1, c:1}
        # s= {a: 0, b:1, c:1}
        minLen = float('inf')
        resLen = [-1, -1]
        window = {}
        count_t = {}
        
        for char in t:
            count_t[char] = count_t.get(char, 0) + 1
        have = 0
        need = len(count_t)
        l = 0
        for r in range(len(s)):
            if s[r] in t:
                char = s[r]
                window[char] = window.get(char, 0) + 1
                if char in count_t and window[char] == count_t[char]:
                    have += 1
       
            while have == need:
                if (r - l + 1) < minLen:
                    minLen = (r - l + 1)
                    resLen = [l, r]
                curr = s[l]
                if curr in window:
                    window[curr] -= 1
                    if curr in count_t and window[curr] < count_t[curr]:
                        have -= 1 
                l += 1
                
        i, j = resLen
        res = s[i : j+1]
        return res if minLen != float('inf') else ""
            

