class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        #Build a set of words O(n)
        word_set = set(wordList)
        neighbors = {}

        # No possible sequence
        if endWord not in word_set:
            return 0
        # Single word sequence
        if beginWord == endWord and beginWord in word_set:
            return 1
        
        # Get neighbors of a word via character replacement
        # exclude the word from being its own neighbor
        def get_neighbors(word) -> list: # O(m^2)
            if word in neighbors:
                return neighbors[word]
            new_word_neighbors = []
            for pos in range(len(word)): # O(m)
                curr_letter = word[pos]
                for i in range(26): # O(26)
                    new_letter = chr(ord('a') + i)                    
                    if new_letter != curr_letter:
                        new_word = word[0:pos] + new_letter # O(m)
                        if pos < len(word) - 1:
                            new_word += word[pos+1:] # O(m)
                        if new_word in word_set:
                            new_word_neighbors.append(new_word)
            return new_word_neighbors

        # Map each word to its neighbors
        for word in wordList: # O (n)
            neighbors[word] = get_neighbors(word)

        # Add neighbors of beginWord to the queue and visited
        q = deque()
        visited = set()
        for neighbor in get_neighbors(beginWord):
            q.append((neighbor, 2))
            visited.add(neighbor)

        # BFS - if queue empty, return 0, else first solution
        while q: # O(n)
            word, length = q.popleft()
            # print(word)
            if word == endWord: # O(w)
                return length
            for neighbor in neighbors[word]:
                if neighbor not in visited:
                    q.append((neighbor, length+1))
                    visited.add(neighbor)
        return 0


# cat -> sag
# ["bat","bag","sag","dag","dot"]

# cat
# bat
# bag
# sag

# bat: bag
# bag: bat, sag, dag
# sag: bag, dag
# dot:
# dag: bag, sag

# q = (sag, 4)
# visited = bat, bag, dag, sag
# word = bat -> bag
# length = 2 -> 3 -> 4

# ["bat","bag","sag","dag","dot", "sat"]

# cat
# sat (x bat)
# sag

# want to compare the words to see that one letter is off - O(w) time where w is the length of the words

# from the starting word, branch off to all the viable options (breadth first)

# you don't want to repeat words you've already seen (would be a loop and only push you further from min sol)

# the first level where you reach the end word, you have the solution

# if there are no viable options that aren't already visited, then return 0

# for each word will at most search through all words and do that many comparisons between words so O(n * n * m) runtime with O(n) space for visited

# what if we represent one-off words as neighbors in a graph

# edge case: if end is not in the wordList, then return 0

# instead of searching through all the words, we can cycle through every character replacement for each position
# - build a set of words
# - for each word, build its neighbors via character replacement
# - build neighbors of beginWord
# - BFS, queue, visited set, if queue empty, return 0, else first solution
