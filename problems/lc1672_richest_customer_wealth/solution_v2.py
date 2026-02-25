from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(map(sum, accounts))


if __name__ == "__main__":
    example_accounts = [
        [1, 2, 3],
        [3, 2, 1]
    ]

    result = Solution().maximumWealth(example_accounts)
    print("Input:", example_accounts)
    print("Output:", result)