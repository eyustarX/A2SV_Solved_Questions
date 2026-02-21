class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        count = 0
        primes = {2, 3, 5, 7, 11, 13, 17, 19}

        for i in range(left, right + 1):
            k = list(map(int, bin(i)[2:]))
            if sum(k) in primes:
                count += 1
        
        return count