class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        k=len(s1)
        hmaps1={}
        for i in range(len(s1)):
            hmaps1[s1[i]]=hmaps1.get(s1[i],0)+1
        
        hmap2={}
        
        i,j=0,0
        while j<len(s2):

            hmap2[s2[j]]=hmap2.get(s2[j],0)+1
            if j-i+1>k:
                if hmap2[s2[i]]>1:
                    hmap2[s2[i]]-=1
                else:
                    del hmap2[s2[i]]
                i+=1


            if j-i+1==k:
                if hmaps1==hmap2:
                    return True
                
            j+=1


        return False    



        