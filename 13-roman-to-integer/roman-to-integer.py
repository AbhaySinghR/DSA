class Solution:
    def romanToInt(self, s: str) -> int:

        hmap={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

        num=0
        i=0
        while i<len(s)-1:
            if s[i] in ['I'] and s[i+1] in ['V','X']:
                num-=hmap[s[i]]
                num+=hmap[s[i+1]]
                i+=2
            elif s[i] in ['X'] and s[i+1] in ['L','C']:
                num-=hmap[s[i]]
                num+=hmap[s[i+1]]
                i+=2
            elif s[i] in ['C'] and s[i+1] in ['D','M']:
                num-=hmap[s[i]]
                num+=hmap[s[i+1]]
                i+=2
            else:
                num+=hmap[s[i]]
                i+=1
        if i==len(s)-1:
            num+=hmap[s[i]]
        return num 



        