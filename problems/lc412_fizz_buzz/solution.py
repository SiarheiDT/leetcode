from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []

        if not isinstance(n, int):
            raise TypeError("Input must be an integer")
        
        if n <= 0 :
            raise ValueError("Input must be positive")
        
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                result.append('FizzBuzz')
            elif i % 3 == 0:
                result.append('Fizz')
            elif i % 5 == 0:
                result.append('Buzz')
            else:
                result.append(str(i))
        
        return result
    
if __name__ == "__main__":
    n = 30
    output = Solution().fizzBuzz(n)
    print(output)