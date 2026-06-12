class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        starts = deque()
        starts.append(0)
        word_set = set(wordDict)
        visited_starts = set()
        while starts:
            start = starts.pop()
            visited_starts.add(start)
            for i in range(21):
                new_start = start+i+1
                if new_start > len(s):
                    break
                word = s[start:new_start]
                if word in word_set:
                    if new_start == len(s):
                        return True
                    if new_start not in visited_starts:
                        visited_starts.add(new_start)
                        starts.append(new_start)
        return False