class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        char_freq_map = Counter(tasks)
        heap = [(-freq, char) for char, freq in char_freq_map.items()]
        heapq.heapify(heap)
        queue = deque()
        i = 0
        while heap or queue:
            # Can we move heap max to queue
            if heap:
                freq, char = heapq.heappop(heap)
                freq *= -1
                if freq > 1:
                    queue.append((char, freq-1, i))
            # Can we remove from queue
            if queue:
                char, freq, xi = queue[0]
                if i-xi == n:
                    queue.popleft()
                    heapq.heappush(heap, (-freq, char))
            i+=1
        return i

# tasks=["A","A","A","B","C"] n=3
# i = 9
# heap =
# queue = 

# Use a max heap for the maximum element (freq, letter)
# use a queue for cooldown
# pop top from heap -> insert to queue with n
# dont re-insert into heap until cooldown has passed
# heap: (1,X)
# queue: (X, i)
# res: X

# # X X, n = 2
# # 1 - X
# # 2 
# # 3 
# # 4 - X

# # X X Y, n = 2
# # 1 - X
# # 2 - Y
# # 3 
# # 4 - X

# # X X Y Z A, n = 2
# # 1 - X
# # 2 - Y
# # 3 - Z
# # 4 - X
# # 5 - A

# # ["X","X","Y","Y"], n = 2
# # Y: 1
# # X: 1
# # maintain a set of size n to see the n most recent tasks 
# # (want to skip these tasks when choosing)
# # queue: (x, y, idle) once queue is of size n, need to popleft from it
# # set: ()
# # 1 - X
# # 2 - Y
# # 3 
# # 4 - X
# # 5 - Y

# heap - (1, A) 
# queue- 
# res - ABCAXXA
# # ["A","A","A","B","C"], n = 3
# # 1 - A
# # 2 - B
# # 3 - C
# # 4 
# # 5 - A
# # 6 
# # 7 
# # 8 
# # 9 - A

# # A: 3
# # B: 1

# # nlogn to sort all the tasks and their frequencies 

# # A B
