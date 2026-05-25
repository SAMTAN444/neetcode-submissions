class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = {}

        for s in strs:
            t = [0] * 26
            for c in s:
                t[ord(c)-ord('a')] += 1
            if tuple(t) in m:
                m[tuple(t)].append(s)
            else:
                m[tuple(t)] = [s]
        return list(m.values())
            