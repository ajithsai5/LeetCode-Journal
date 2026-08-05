class Solution:
    def countAndSay(self, n: int) -> str:
        ans = "1"

        for _ in range(n - 1):
            temp = []
            count = 1

            for i in range(1, len(ans)):
                if ans[i] == ans[i - 1]:
                    count += 1
                else:
                    temp.append(str(count))
                    temp.append(ans[i - 1])
                    count = 1

            # Append the last group
            temp.append(str(count))
            temp.append(ans[-1])

            ans = "".join(temp)

        return ans
        