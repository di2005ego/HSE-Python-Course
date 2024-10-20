# https://leetcode.com/problems/word-ladder/


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        words = set(wordList)
        queue = deque([beginWord])
        answer = 1
        while queue:
            answer += 1
            for _ in range(len(queue)):
                s = queue.popleft()
                s = list(s)
                for i in range(len(s)):
                    ch = s[i]
                    for j in range(26):
                        s[i] = chr(ord("a") + j)
                        t = "".join(s)
                        if t not in words:
                            continue
                        if t == endWord:
                            return answer
                        queue.append(t)
                        words.remove(t)
                    s[i] = ch
        return 0
