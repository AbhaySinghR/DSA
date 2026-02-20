class Solution:
    def isValid(self, s: str) -> bool:

        st=[]
        hmap={'(':')','{':'}','[':']'}
        i=0
        while i<len(s):
            if s[i] in hmap:
                st.append(s[i])
            else:
                if not st:
                    return False
                if hmap[st[-1]]!=s[i]:
                    return False
                st.pop()
            i+=1
        return not st
        