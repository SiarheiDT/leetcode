class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Early exit optimization
        if len(ransomNote) > len(magazine):
            return False

        # Frequency array for 26 lowercase letters
        counts = [0] * 26

        # Count characters in magazine
        for char in magazine:
            counts[ord(char) - ord('a')] += 1

        # Validate ransomNote characters
        for char in ransomNote:
            idx = ord(char) - ord('a')
            if counts[idx] == 0:
                return False
            counts[idx] -= 1

        return True

if __name__ == "__main__":
    s = Solution()

    print(s.canConstruct("a", "b"))      # False
    print(s.canConstruct("aa", "ab"))    # False
    print(s.canConstruct("aa", "aab"))   # True