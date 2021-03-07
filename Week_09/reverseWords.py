class Solution:
    """
    @param: s: A string
    @return: A string
    """
    def reverseWords(self, s):
        # write your code here
        list1 = s.split()
        str1 = ''
        if len(list1) == 0:
            return str1
        if len(list1) == 1:
            str1 += list1[0]
            return str1
        
        i = len(list1)
        str1 = list1[-1]
        while i > 1:
            str1 += ' ' + list1[i - 2]
            i = i - 1
            
        print(len(str1))
        return str1
