class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        st=[]
        for i in tokens:
            if i in ['+','-','*','/']:
                b=int(st.pop())
                a=int(st.pop())
                if i =='+':
                    st.append(a+b)
                elif i=='-':
                    st.append(a-b)
                elif i=='*':
                    st.append(a*b)
                else:
                    st.append(a/b)
            else:
                st.append(i)
        
        return int(st[-1])
        