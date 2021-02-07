def countSubstrings(self, s: str) -> int:
    n = len(s)
    res = 0
    for i in range(n):
        for j in range(i, n):
            cur_s = s[i:j+1]
            left = 0
            right = len(cur_s)-1
            while left <= right:
                if cur_s[left] != cur_s[right]:
                    break
                left += 1
                right -= 1
            if left > right:
                res += 1
    return res
