class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        result = []
        j = len(S)-1
        for i in range(len(S)):
            if S[i].isalpha():
                while(not S[j].isalpha()):
                    j -= 1
                result.append(S[j])
                j -= 1
                continue
            result.append(S[i])
        result = "".join(result)
        return result
