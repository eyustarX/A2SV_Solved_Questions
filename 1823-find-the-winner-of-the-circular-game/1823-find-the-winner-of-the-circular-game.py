class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        player = [i for i in range(1,n + 1)]

        def play(a,b, x = 0):
            if a == 1:
                return player[0]

            x = (x + k - 1) % a

            player.pop(x)
            a -= 1

            return play(a, b, x)

        return play(n, k)