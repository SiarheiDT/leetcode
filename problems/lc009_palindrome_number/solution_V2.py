class Solution:
    def isPalindrome(self, x: int) -> bool:
        # LeetCode-style behavior:
        if x < 0:
            return False
        if x % 10 == 0 and x != 0:
            return False

        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + (x % 10)
            x //= 10

        # Even digits: x == reversed_half
        # Odd digits:  x == reversed_half // 10 (middle digit dropped)
        return x == reversed_half or x == reversed_half // 10

if __name__ == "__main__":
    s = Solution()
    print("Manual run example:")
    print(s.isPalindrome(123456))
