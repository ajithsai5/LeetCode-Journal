class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words

        need = Counter(words)
        ans = []

        for offset in range(word_len):
            left = offset
            seen = defaultdict(int)
            count = 0

            for right in range(offset, len(s) - word_len + 1, word_len):
                word = s[right:right + word_len]

                if word in need:
                    seen[word] += 1
                    count += 1

                    while seen[word] > need[word]:
                        left_word = s[left:left + word_len]
                        seen[left_word] -= 1
                        left += word_len
                        count -= 1

                    if count == num_words:
                        ans.append(left)

                        left_word = s[left:left + word_len]
                        seen[left_word] -= 1
                        left += word_len
                        count -= 1

                else:
                    seen.clear()
                    count = 0
                    left = right + word_len

        return ans