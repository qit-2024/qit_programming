
class LeetcodeSolution:
    @staticmethod
    def countPrimes(n: int) -> int:
        lst = [True for i in range(n)]
        count = 1 if n > 2 else 0
        lim = n**0.5
        for i in range(3, len(lst), 2):
            if lst[i] and i%2!=0:
                count+=1
                if i<= lim:
                    for j in range(i+i, len(lst),i):
                        lst[j] = False

        return count