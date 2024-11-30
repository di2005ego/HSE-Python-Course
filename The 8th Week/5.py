# https://leetcode.com/problems/swap-for-longest-repeated-character-substring/


class Solution(object):
    def maxRepOpt1(self, text):
        char_count = Counter(text)
        text_length = len(text)
        max_length = current_index = 0
        while current_index < text_length:
            start_index = current_index
            while (
                start_index < text_length and text[start_index] == text[current_index]
            ):
                start_index += 1
            left_sequence_length = start_index - current_index
            next_index = start_index + 1
            while next_index < text_length and text[next_index] == text[current_index]:
                next_index += 1
            right_sequence_length = next_index - start_index - 1
            total_length = min(
                left_sequence_length + right_sequence_length + 1,
                char_count[text[current_index]],
            )
            max_length = max(max_length, total_length)
            current_index = start_index
        return max_length
