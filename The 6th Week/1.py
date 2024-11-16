# https://leetcode.com/problems/repeated-dna-sequences/


class Solution(object):
    def findRepeatedDnaSequences(self, s):
        sequence_count = Counter()
        repeated_sequences = []
        num_substrings = len(s) - 10
        for i in range(num_substrings + 1):
            subsequence = s[i : i + 10]
            sequence_count[subsequence] += 1
            if sequence_count[subsequence] == 2:
                repeated_sequences.append(subsequence)
        return repeated_sequences
