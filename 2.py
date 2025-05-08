from heapq import heappush, heappop

class AStar:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])

    def heuristic(self, current, goal):
        return abs(current[0] - goal[0]) + abs(current[1] - goal[1])

    def is_valid(self, x, y):
        return 0 <= x < self.rows and 0 <= y < self.cols and self.grid[x][y] == 0

    def a_star(self, start, goal):
        open_set = []
        heappush(open_set, (0, start))

        g_cost = {start: 0}
        f_cost = {start: self.heuristic(start, goal)}
        came_from = {}

        while open_set:
            _, current = heappop(open_set)

            if current == goal:
                return self.reconstruct_path(came_from, current)

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  
                neighbor = (current[0] + dx, current[1] + dy)
                if self.is_valid(neighbor[0], neighbor[1]):
                    tentative_g_cost = g_cost[current] + 1

                    if neighbor not in g_cost or tentative_g_cost < g_cost[neighbor]:
                        g_cost[neighbor] = tentative_g_cost
                        f_cost[neighbor] = tentative_g_cost + self.heuristic(neighbor, goal)
                        heappush(open_set, (f_cost[neighbor], neighbor))
                        came_from[neighbor] = current

        return None  

    def reconstruct_path(self, came_from, current):
        path = []
        while current in came_from:
            path.append(current)
            current = came_from[current]
        path.append(current)
        return path[::-1]  


if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0],
        [1, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 1, 0, 1],
        [0, 0, 0, 0, 0],
    ]

    start = (0, 0)  
    goal = (4, 4)  

    astar = AStar(grid)
    path = astar.a_star(start, goal)

    if path:
        print("Path found: \n", path)
    else:
        print("No path found")