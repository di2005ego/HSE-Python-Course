# https://leetcode.com/problems/find-all-anagrams-in-a-string/


class Solution(object):
    def findAnagrams(self, s, p):
        s_length, p_length = len(s), len(p)
        anagram_indices = []
        if s_length < p_length:
            return anagram_indices
        p_char_count = Counter(p)
        s_window_count = Counter(s[: p_length - 1])
        for i in range(p_length - 1, s_length):
            s_window_count[s[i]] += 1
            if p_char_count == s_window_count:
                anagram_indices.append(i - p_length + 1)
            s_window_count[s[i - p_length + 1]] -= 1
            if s_window_count[s[i - p_length + 1]] == 0:
                del s_window_count[s[i - p_length + 1]]
        return anagram_indices
        