# https://leetcode.com/problems/longest-repeating-character-replacement/


class Solution(object):
    def characterReplacement(self, s, k):
        frequency_counter = [0] * 26
        left = right = 0
        max_frequency = 0
        while right < len(s):
            frequency_counter[ord(s[right]) - ord("A")] += 1
            max_frequency = max(
                max_frequency, frequency_counter[ord(s[right]) - ord("A")]
            )
            if (right - left + 1) > max_frequency + k:
                frequency_counter[ord(s[left]) - ord("A")] -= 1
                left += 1
            right += 1
        return right - left