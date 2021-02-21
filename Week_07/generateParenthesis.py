class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def generate(A):
            if len(A) == 2*n:
                if(valid(A)):
                    res.append(''.join(A))
            else:
                A.append('(')
                generate(A)
                A.pop()
                A.append(')')
                generate(A)
                A.pop()
        def valid(A):
            balanced = 0
            for c in A:
                if c=='(':
                    balanced += 1
                else:
                    balanced -= 1
                if balanced < 0:
                    return False
            return balanced == 0
 
        res = []
        A = []
        generate(A)
        return res
