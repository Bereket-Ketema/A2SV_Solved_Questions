class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix_sum = [0] * (len(s) + 1)

        for l, r, d in shifts:
            if d == 0:
                prefix_sum[l] -= 1
                prefix_sum[r + 1] += 1 
            else:
                prefix_sum[l] += 1
                prefix_sum[r + 1] -= 1

        accumlate = 0
        answer = ''
        for i, char in enumerate(s):
            char_ord = ord(char) - ord('a')
            accumlate += prefix_sum[i]
            char_ord = (char_ord + accumlate) % 26
            answer += chr(char_ord + ord("a"))

        return answer
