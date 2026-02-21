class Solution:
    def calculate(self, s: str) -> int:

        res=0
        sign=1
        st=[]
        num=0
        for i in s:
            if i.isdigit():
                num=num*10+int(i)
            elif i == '+':
                res+=num*sign
                num=0
                sign=1
            elif i =='-':
                res+=num*sign
                num=0
                sign=-1
            elif i=='(':
                st.append(res)
                st.append(sign)
                res=0
                sign=1
            elif i==')':
                res+=sign*num
                num=0
                p_sign=st.pop()
                p_res=st.pop()
                res=p_res+p_sign*res
        res += sign * num
        return res




        