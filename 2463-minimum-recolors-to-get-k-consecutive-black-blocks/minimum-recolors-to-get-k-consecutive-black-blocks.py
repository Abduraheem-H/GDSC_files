


class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # Sliding window aproach

        # Input: blocks = "WBBWWBBWBW", k = 7
        left = 0
        right = k - 1
        mini = float(inf)
        counter = 0
        while right < len(blocks):
            counter += 1
            minimum = 0
            while left <= right:
                if blocks[left] == "W":
                    minimum += 1
                left += 1
            left = counter
            right += 1
            mini = min(mini, minimum)
        return mini
#print(Solution.minimumRecolors("B", 1))
