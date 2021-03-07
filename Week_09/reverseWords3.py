class Solution:
    def reverseWords(self, s: str) -> str:
        flag=0
        res=''
        for i in range(0,len(s)):
            if s[i]==' ':  
                t=s[flag:i]#将空格前的单词赋给t
                t=t[::-1]#反转单词
                print(t)
                res=res+t+' '
                flag=i+1#记录下一个单词的第一个字母索引
        t=s[flag:]#最后一个单词
        t=t[::-1]
        res=res+t
        return res
