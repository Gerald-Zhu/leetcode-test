class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        count = 0
        output = [1]
        while count < rowIndex:
            output = [m+n for m,n in zip([0]+output,output+[0])]
            count += 1
        return output