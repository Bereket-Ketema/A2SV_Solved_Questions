class Solution:
    def romanToInt(self, s: str) -> int:
        y=list(s)
        for i in range(len(y)):
            if y[i]=='I':
                y[i]=1
            elif y[i]=='V':
                y[i]=5
            elif y[i]=='X':
                y[i]=10
            elif y[i]=='L':
                y[i]=50
            elif y[i]=='C':
                y[i]=100
            elif y  [i]=='D':
                y[i]=500
            elif y[i]=='M':
                y[i]=1000
        for i in range(len(y)-1):
            if y[i]<y[i+1]:
                y[i]=-y[i]
        y=sum(y)
        return y
