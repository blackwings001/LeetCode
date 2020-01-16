class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if not s or len(s) <= 10:
            return []

        sub_seq_hash = {}
        sub_seq = s[:10]

        for i in range(10, len(s) + 1):
            sub_seq_hash[sub_seq] = sub_seq_hash.get(sub_seq, 0) + 1
            sub_seq = sub_seq[1:] + s[i:i+1]  # 不使用s[i]会造成越界

        res = [k for k, v in sub_seq_hash.items() if v > 1]

        return res


if __name__ == '__main__':
    s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    res = Solution().findRepeatedDnaSequences(s)
    print(res)
