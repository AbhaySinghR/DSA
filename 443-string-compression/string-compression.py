class Solution:
    def compress(self, chars: List[str]) -> int:

        cnt=0
        i,j=0,0
        if len(chars)==1:
            return 1
        s=''
        while j<len(chars):
            if chars[j]!=chars[i]:
                if cnt>1:
                    s+=chars[i]+str(cnt)
                else:
                    s+=chars[i]
                cnt=1
                i=j
            else:
                cnt+=1
            j+=1
        
        if cnt>1:
            s+=chars[i]+str(cnt)
        else:
            s+=chars[i]
       

        for i in range(len(s)):
            chars[i]=s[i]

        return len(s)
        