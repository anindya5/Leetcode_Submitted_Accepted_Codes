#Problem at https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    import itertools
    def letterCombinations(self, digits: str) -> List[str]:
        digits=list(digits)
        
        num_dict={2:'abc',3:'def',4:'ghi',5:'jkl',6:'mno',7:'pqrs',8:'tuv',9:'wxyz'}
        str_replace=[]
        for pos,num in enumerate(digits):
            str_replace.append(num_dict[int(num)])
        output=[]
        for i in itertools.product(*str_replace):
            output.append(''.join(i))
        if(len(digits)==0):
            output=[]
        return output
