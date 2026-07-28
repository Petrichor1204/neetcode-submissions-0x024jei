class Solution:
    def tribonacci(self, n: int) -> int:
        # goal: return the value of Tn which is the sum of the three terms before it
        # Tn = T(n - 1) +  (T(n - 1) - T(n - 4))
        # to get the val of Tn, we need to get the sum of the three vals
        # before it which is the term right before it plus the tow before it
        # the term right before it already has the sum of of the tree vals so we can just deduct the n - 3 term
        #[0,1,1,0,0,0]
        #       i 
        terms = [0] * (n + 1  )
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1 
        
        terms[0:4] = [0, 1, 1, 2] 
        
        for i in range(4, n + 1):
            terms[i] = terms[i - 1] + terms[i - 2] + terms[i - 3]

        return terms[n]
