class Solution:
    def climbStairs(self, n: int) -> int:
        f0 = 0
        f1 = 1
        f2 = 2
        if n<=0:
            return f0
        elif n==1:
            return f1
        elif n==2:
            return f2
        else:
            result = 0
            for i in range(3,n+1):
                result = f1+f2
                f1 = f2
                f2 = result
        return result
