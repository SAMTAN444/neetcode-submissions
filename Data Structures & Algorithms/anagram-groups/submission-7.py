class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        t = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                a = ord(c) - ord("a")
                count[a] += 1
            t[(tuple(count))].append(s)
        return list(t.values())