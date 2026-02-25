from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_sum = 0
        
        for customer in accounts:
            wealth = sum(customer)
            max_sum = max(max_sum, wealth)
            
        return max_sum
    
if __name__ == "__main__":
    example_accounts = [
        [1, 9, 3],
        [8, 4, 1]
    ]

    result = Solution().maximumWealth(example_accounts)
    print("Input:", example_accounts)
    print("Output:", result)