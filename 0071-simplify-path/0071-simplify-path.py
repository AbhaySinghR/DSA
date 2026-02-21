class Solution:
    def simplifyPath(self, path: str) -> str:

        split_path=path.split("/")
        st=[]
        for i in split_path:
            if i == '' or i=='.':
                continue
            elif i == '..':
                if st:
                    st.pop()
                else:
                    continue
            else:
                st.append(i)

        c_path='/'
        for i in range(len(st)):
            if i==len(st)-1:            
                c_path+=st[i]
            else:
                c_path+=st[i]    
                c_path+='/'
        return c_path

        