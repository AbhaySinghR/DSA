class Solution:
    def compress(self, chars: List[str]) -> int:
        
        if len(chars)==1:
            return 1

        s=''
        i,j=0,0
        while j<len(chars):
            if chars[j]!=chars[i]:
                if j-i==1:
                    s+=chars[i]
                    i=j
                else:
                    s+=chars[i]+str(j-i)
                    i=j
            j+=1

        if j-i==1:
            s+=chars[i]
        else:
            s+=chars[i]+str(j-i)
        
        for i in range(len(s)):
            chars[i]=s[i]
        return len(s)

