class Solution:
    def numberOfSteps(self, num: int) -> int:
        result = 0

        if not isinstance(num, int):
            raise TypeError("Input must be an integer")
        
        if num < 0 :
            raise ValueError("Input must be positive")  

        while num != 0:
            if num % 2 == 0:
                result += 1
                num = num / 2 
            else: 
                num -= 1 
                result += 1

        return result

if __name__ == "__main__":
    num = 0
    output = Solution().numberOfSteps(num)
    print(output)
