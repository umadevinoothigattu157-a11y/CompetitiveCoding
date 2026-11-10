class Solution:
    def findMismatchedSegments(self, s1: str, s2: str) -> list[list[str]]:
        result = []
        i = 0
        n = len(s1)

        while i < n:

            if s1[i] == s2[i]:
                i += 1

            else:
                start = i

                while i < n and s1[i] != s2[i]:
                    i += 1

                result.append([s1[start:i], s2[start:i]])

        return result
