class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        self.word1 = list(word1)
        self.word2 = list(word2)

        length = 0
        if len(self.word1) > len(self.word2):
            length = len(self.word1)
        else:
            length = len(self.word2)

        merged = []

        for i in range(length):
            try:
                merged.append(self.word1[i])
            except IndexError:
                merged.append('')
            try:
                merged.append(self.word2[i])
            except IndexError:
                merged.append('')

        result = ''.join(merged)
        return result


word1 = "abcd"
word2 = "pq"

solution = Solution()

print(solution.mergeAlternately(word1, word2))
