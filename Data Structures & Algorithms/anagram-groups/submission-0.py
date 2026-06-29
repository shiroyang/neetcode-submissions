class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # key: sorted_str; val: str
        d = defaultdict(list)
        for item in strs:
            d[str(sorted(list(item)))].append(item)
        ans = []
        for key, val in d.items():
            ans.append(val)
        return ans