class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num=0
        n=len(digits)-1
        for i in digits:
            num+=i*pow(10,n)
            n-=1

        num+=1
        li=[]
        s=str(num)
        for i in s:
            li.append(int(i))
        return li
