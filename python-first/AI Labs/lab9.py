from queue import PriorityQueue

# Define the goal state
goal_state = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]]

# Define the initial state
initial_state = [[2, 8, 3],
                  [1, 6, 4],
                  [7, 0, 5]]

# Define the Manhattan distance heuristic
def manhattan_distance(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                target_i, target_j = divmod(state[i][j] - 1, 3)
                distance += abs(i - target_i) + abs(j - target_j)
    return distance

# Define the Node class
class Node:
    def __init__(self, state, parent, action, cost):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost

# Define the A* search algorithm
def astar_search(initial_state):
    frontier = PriorityQueue()
    frontier.put(Node(initial_state, None, None, 0))
    explored = set()

    while not frontier.empty():
        current_node = frontier.get()
        current_state = current_node.state

        if current_state == goal_state:
            path = []
            while current_node.parent is not None:
                path.append((current_node.action, current_node.state))
                current_node = current_node.parent
            path.reverse()
            return path

        explored.add(tuple(map(tuple, current_state)))

        # Find the position of the empty tile
        for i in range(3):
            for j in range(3):
                if current_state[i][j] == 0:
                    empty_i, empty_j = i, j

        # Generate child nodes
        for action in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            new_i, new_j = empty_i + action[0], empty_j + action[1]
            if 0 <= new_i < 3 and 0 <= new_j < 3:
                new_state = [row[:] for row in current_state]
                new_state[empty_i][empty_j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[empty_i][empty_j]
                if tuple(map(tuple, new_state)) not in explored:
                    new_node = Node(new_state, current_node, action, current_node.cost + 1 + manhattan_distance(new_state))
                    frontier.put(new_node)

    return None

# Solve the 8-puzzle problem
solution = astar_search(initial_state)

# Print the solution path
if solution is None:
    print("No solution found")
else:
    print("Solution found:")
    for step, state in enumerate(solution):
        print(f"Step {step + 1}: {state[0]}")
        for row in state[1]:
            print(row)
        print()
