class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = {}

        for s in strs:
            t = [0] * 26
            for c in s:
                t[ord(c) - ord('a')] += 1
            tt = tuple(t)
            if tt in m:
                m[tt].append(s)
            else:
                m[tt] = [s]
        return list(m.values())