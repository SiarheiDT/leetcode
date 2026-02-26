class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if not isinstance(x, int):
            raise TypeError("Input must be an integer")
        
        if x < 0 :
            raise ValueError("Input must be positive")  

        s = str(x)

        while len(s)>=2:
            if s[-1] != s[0]:
                return False
            s = s[:-1]  
            s = s[1:] 
        return True 

if __name__ == "__main__":
    s = Solution()
    print("Manual run example:")
    print(s.isPalindrome(123456))
