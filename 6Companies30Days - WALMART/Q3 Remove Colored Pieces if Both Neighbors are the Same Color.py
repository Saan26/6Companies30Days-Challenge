# Remove Colored Pieces if Both Neighbors are the Same Color

class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        count = collections.Counter()
        
        for x, t in groupby(colors):
            count[x] += max(len(list(t))-2, 0)
        if count['A'] > count['B']:
            return True
        return False