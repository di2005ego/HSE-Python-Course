# https://leetcode.com/problems/permutation-in-string/


class Solution(object):
    def checkInclusion(self, s1, s2):
        pattern_length, text_length = len(s1), len(s2)
        if pattern_length > text_length:
            return False
        char_counter = Counter()
        for pattern_char, text_char in zip(s1, s2[:pattern_length]):
            char_counter[pattern_char] -= 1
            char_counter[text_char] += 1
        diff_count = sum(x != 0 for x in char_counter.values())
        if diff_count == 0:
            return True
        for i in range(pattern_length, text_length):
            char_out = s2[i - pattern_length]
            char_in = s2[i]
            if char_counter[char_in] == 0:
                diff_count += 1
            char_counter[char_in] += 1
            if char_counter[char_in] == 0:
                diff_count -= 1
            if char_counter[char_out] == 0:
                diff_count += 1
            char_counter[char_out] -= 1
            if char_counter[char_out] == 0:
                diff_count -= 1
            if diff_count == 0:
                return True
        return False
