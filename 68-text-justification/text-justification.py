class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        i = 0

        while i < len(words):
            # Find all words that fit in this line
            j = i
            line_length = 0

            while j < len(words):
                word_length = len(words[j])

                # Minimum 1 space between words
                if line_length + word_length + (j - i) > maxWidth:
                    break

                line_length += word_length
                j += 1

            # Words in this line
            line_words = words[i:j]
            num_words = len(line_words)

            # Last line OR only one word
            if j == len(words) or num_words == 1:
                line = " ".join(line_words)

                # Left justify
                line += " " * (maxWidth - len(line))

                result.append(line)

            else:
                # Total spaces that need to be distributed
                total_spaces = maxWidth - sum(len(word) for word in line_words)

                gaps = num_words - 1

                # Minimum spaces per gap
                spaces = total_spaces // gaps

                # Extra spaces
                extra = total_spaces % gaps

                line = ""

                for k in range(gaps):
                    line += line_words[k]
                    line += " " * (spaces + (1 if k < extra else 0))

                # Add last word
                line += line_words[-1]

                result.append(line)

            i = j

        return result