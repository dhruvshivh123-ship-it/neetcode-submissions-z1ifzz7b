class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        has=defaultdict(list)
        for i in strs:
            k=''.join(sorted(i))
            has[k].append(i)
        return list(has.values())