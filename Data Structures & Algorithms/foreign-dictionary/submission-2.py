class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # assemble in-degree and children maps
        in_deg = defaultdict(int) # letter -> in-deg
        children = defaultdict(list) # prereq -> letter
        letters = set() # total unique letters in the alien language
        # Track all unique letters
        for word in words:
            for letter in word:
                letters.add(letter)
        # Compare all adjacent word pairs to find pre-req letter
        for i in range(1, len(words)):
            first = words[i-1]
            second = words[i]
            if len(first) > len(second) and first.startswith(second):
                return ""
            smaller_len = min(len(first), len(second))
            j = 0
            while j < smaller_len:
                first_letter = first[j]
                second_letter = second[j]
                if first_letter != second_letter:
                    children[first_letter].append(second_letter)
                    in_deg[second_letter]+=1
                    break
                j+=1
        # topological sort
        queue = deque()
        order = []
        # Enqueue all letters with in-degree of 0
        for letter in letters:
            if in_deg[letter] == 0:
                queue.append(letter)
        # Add letters to the queue when their in-degree reaches 0
        while queue:
            letter = queue.popleft()
            order.append(letter)
            for child in children[letter]:
                in_deg[child]-=1
                if in_deg[child] == 0:
                    queue.append(child)
        return "".join(order) if len(order) == len(letters) else ""
