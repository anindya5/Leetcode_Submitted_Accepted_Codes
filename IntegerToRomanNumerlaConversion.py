#Problem at https://leetcode.com/problems/integer-to-roman/

import numpy as np
class Solution:
    def intToRoman(self, num: int) -> str:
        
        out=''
        if(np.floor(num/1000)):
            numerator=np.floor(num/1000)
            out=out+'M'*numerator.astype(int)
            num=num%1000
        
        num=np.floor(num%1000)
        if(np.floor(num/100)):
            numerator=np.floor(num/100)
            if(numerator==9):
                out=out+'CM'
            elif(numerator==4):
                out=out+'CD'
            elif(numerator==5):
                out=out+'D'
            elif(numerator>5):
                out=out+'D'+'C'*(numerator.astype(int)-5)
            else:
                out=out+'C'*numerator.astype(int)
                
        num=np.floor(num%100)
        if(np.floor(num/10)):
            numerator=np.floor(num/10)
            if(numerator==9):
                out=out+'XC'
            elif(numerator==4):
                out=out+'XL'
            elif(numerator==5):
                out=out+'L'
            elif(numerator>5):
                out=out+'L'+'X'*(numerator.astype(int)-5)
            else:
                out=out+'X'*numerator.astype(int)
                
        num=np.floor(num%10)
        if(num):
            numerator=num
            if(numerator==9):
                out=out+'IX'
            elif(numerator==4):
                out=out+'IV'
            elif(numerator==5):
                out=out+'V'
            elif(numerator>5):
                out=out+'V'+'I'*(numerator.astype(int)-5)
            else:
                out=out+'I'*numerator.astype(int)

        return out
