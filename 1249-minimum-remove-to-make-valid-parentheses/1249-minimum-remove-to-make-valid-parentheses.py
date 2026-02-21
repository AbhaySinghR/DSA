class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:


        st=[]
        for i in range(len(s)):
            if s[i] == '(':
                st.append(i)
            elif s[i]==')':
                if st and s[st[-1]]=='(':
                    st.pop()
                else:
                    st.append(i)
        a=set(st)
        res=''
    
        for i in range(len(s)):
            if i not in a:
                res+=s[i]
        
        return res

        