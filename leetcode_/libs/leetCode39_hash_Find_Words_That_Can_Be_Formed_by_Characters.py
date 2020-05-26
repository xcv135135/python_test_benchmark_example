#!/usr/bin/python3

from collections import Counter

class Solution():
    def init(self, words, chars):
        self.words = words
        self.chars = chars
        self.totalLength = 0
        print("chars", self.chars)
        print("words", self.words)
    def count(self):
        counterChars = Counter(self.chars)
        for word in self.words:
            counterWord = Counter(word)
            flagPass = True
            for charactor in counterWord:
                needCharLen = counterWord[charactor]
                if not charactor in counterChars or counterChars[charactor] < needCharLen:
                    flagPass = False
                    break

            if flagPass == True:
                self.totalLength += len(word)
                print("word", word, len(word))

        print(self.totalLength)
        print("finish")
        return self.totalLength

if __name__ == "__main__":
    words = ["cat", "bt", "hat", "tree"]
    chars = "atach"
    solution = Solution()
    solution.init(words, chars)
    solution.count()
