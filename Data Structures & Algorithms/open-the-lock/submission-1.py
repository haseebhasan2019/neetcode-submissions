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
        while queue:
            combo, turns = queue.popleft()
            for i in range(4):
                # plus 1
                digit = int(combo[i]) + 1
                if digit == 10:
                    digit = 0
                plus = combo[:i] + str(digit) + combo[i+1:]
                # minus 1
                digit = int(combo[i]) - 1
                if digit == -1:
                    digit = 9
                minus = combo[:i] + str(digit) + combo[i+1:]
                if plus not in visited_set and plus not in deadends_set:
                    if plus == target:
                        return turns+1
                    visited_set.add(plus)
                    queue.append((plus, turns+1))
                if minus not in visited_set and minus not in deadends_set:
                    if minus == target:
                        return turns+1
                    visited_set.add(minus)
                    queue.append((minus, turns+1))

        return -1
        # enqueue the 8 possibilities if not visited and not deadend


# Input: deadends = ["4443","4445","4434","4454","4344","4544","3444","5444"], target = "4444"

# 0000 = 0
# 1111 = 4
# 2222 = 8
# 3333 = 12

