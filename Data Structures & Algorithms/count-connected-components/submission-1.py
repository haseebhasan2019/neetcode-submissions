class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        visited_sets = []
        visiting = set()
        current_visited = set()

        def dfs(node):
            if node in visiting or node in current_visited:
                return
            visiting.add(node)
            for neighbor in graph[node]:
                dfs(neighbor)
            visiting.remove(node)
            current_visited.add(node)

        for node in range(n):
            if any(node in s for s in visited_sets):
                continue
            dfs(node)
            visited_sets.append(current_visited)
            current_visited = set()
        
        return len(visited_sets)
