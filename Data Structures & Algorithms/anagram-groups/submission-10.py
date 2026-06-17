class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list)

        for s in strs:
            test = [0] * 26
            for c in s:
                test[ord(c) - ord('a')] += 1
            
            head = tuple(test)
            res[head].append(s)
        
        return list(res.values())