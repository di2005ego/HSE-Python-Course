# https://leetcode.com/problems/group-anagrams/


class Solution(object):
    def groupAnagrams(self, strs):
        dd = defaultdict(list)
        for s in strs:
            k = "".join(sorted(s))
            dd[k].append(s)
        return list(dd.values())
