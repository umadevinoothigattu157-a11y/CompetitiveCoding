class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub=""
        max_len = 0
        for ch in s:
            if ch in sub:
                sub = sub[sub.index(ch)+1:]
            sub += ch
            max_len = max(max_len,len(sub))
        return max_len
