class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        if not wordDict or not s:
            return []

        word_set = set(wordDict)
        interval = {}

        def word_break(start, end):
            if end - start == 1:
                if s[start] in word_set:
                    interval[(start, end)] = [s[start]]
                    return [s[start]]
                else:
                    interval[(start, end)] = []
                    return []

            cur = []
            if s[start: end] in word_set:
                cur.append(s[start:end])

            for i in range(start + 1, end):
                if (start, i) in interval:
                    pre = interval[(start, i)]
                else:
                    pre = word_break(start, i)

                if (i, end) in interval:
                    post = interval[(i, end)]
                else:
                    post = word_break(i, end)

                if pre and post:
                    cur.extend([pr + " " + po for pr in pre for po in post])
            interval[(start, end)] = cur

            print(interval)
            return list(set(cur))

        return word_break(0, len(s))


if __name__ == '__main__':
    s = "ab"
    wordDict = ["a", "b"]

    res = Solution().wordBreak(s, wordDict)
    print(res)
