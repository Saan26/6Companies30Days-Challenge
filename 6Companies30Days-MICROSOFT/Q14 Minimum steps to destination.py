# Minimum steps to destination ----------------------------------------------------------------

class Solution:
    def minSteps(self, target):
        if target == 0:
            return 0
        ans = 0
        steps = 0
        target = abs(target)
        while ans < target:
            ans += steps
            steps += 1
        while ((ans - target) % 2 == 1):
            ans += steps
            steps += 1
        return steps-1
