class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if target == '0000':
            return 0
        if '0000' in deadends:
            return -1
        # set of deadends and visited combinations
        deadends_set = set(deadends)
        visited_set = set()
        visited_set.add('0000')
        # have a queue of combinations, start with (0000, 0)
        queue = deque()
        queue.append(('0000', 0))
        
        def enqueue(combo):
            if combo not in visited_set and combo not in deadends_set:
                if combo == target:
                    return turns+1
                visited_set.add(combo)
                queue.append((combo, turns+1))
            return 0
        
        def get_new_combo(combo, i, delta):
            digit = int(combo[i]) + delta
            if digit == 10:
                digit = 0
            elif digit == -1:
                digit = 9
            return combo[:i] + str(digit) + combo[i+1:]
        
        while queue:
            combo, turns = queue.popleft()
            for i in range(4):
                # plus 1
                plus = get_new_combo(combo, i, 1)
                # minus 1
                minus = get_new_combo(combo, i, -1)
                # enqueue plus and minus if valid
                min_turns = enqueue(plus) or enqueue(minus)
                if min_turns:
                    return min_turns

        return -1
