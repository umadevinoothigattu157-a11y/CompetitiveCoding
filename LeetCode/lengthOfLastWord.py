class Solution:
    def lengthOfLastWord(self, s: str) -> int:
       li = list(s.split(" "))
       nli=[item for item in li if item.strip()]
       return len(nli[-1])
