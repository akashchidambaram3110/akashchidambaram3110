class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        beauty = 0
        divisor = num
        i = 0
        j = k
        str_div = str(num)
        n = len(str_div)
        while j <= n:
            dividend = int(str_div[i:j])
            print(dividend)
            if dividend > 0:
                if divisor % dividend == 0:
                    beauty += 1
            i += 1
            j += 1
        return beauty
