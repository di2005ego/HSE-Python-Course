#https://leetcode.com/problems/substring-with-concatenation-of-all-words/

class Solution(object):
    def findSubstring(self, s, words):
        numChars = len(words[0])
        numWords = len(words)
        answer = []
        counter = dict()
        for i in range (numWords):
            if words[i] in counter:
                counter[words[i]] += 1
            else:
                counter[words[i]] = 1
        totalChars = numChars*numWords
        for i in range (len(s) - totalChars + 1):
            pair = s[i:i+totalChars]
            noticed = dict()
            index = 0
            j = 0
            while index < numWords:
                word = pair[j:j+numChars]
                if word in noticed:
                    noticed[word] += 1
                else:
                    noticed[word] = 1
                j += numChars
                index += 1
            if noticed == counter:
                answer.append(i)
        return answer