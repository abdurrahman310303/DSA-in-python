import random
import math

class Lab10:

    def __init__(self) :

        self.greeting = "This is Lab Ten"

# You are given a set of cities and the distances between them. Use the simulated annealing 
# algorithm to find an approximate solution to the TSP(Traveling Sales man Problem. Write a
# Python code that performs the following steps:
# • Print the best solution found and its total distance.
# • Generate a random initial solution (i.e., a random permutation of the cities).
# • Define an objective function that calculates the total distance of a given route.
# • Initialize the current solution with the initial solution.
# • Set an initial temperature and cooling rate.
# • Perform iterations until a stopping condition is met: a. Generate a random
# neighboring solution by randomly swapping two cities in the current solution. b.
# Calculate the change in the objective function between the current and neighboring
# solution. c. If the neighboring solution is better (i.e., lower distance), accept it as the 
# new current solution. d. If the neighboring solution is worse, accept it with a 
# probability based on the change in distance and temperature. e. Decrease the
# temperature based on the cooling rate.
    
    def distance(self,city1, city2):
    # Example distances, you can replace this with actual distances
        distances = {
            ('A', 'B'): 2, ('A', 'C'): 9, ('A', 'D'): 10,
            ('B', 'C'): 6, ('B', 'D'): 4,
            ('C', 'D'): 7
        }
        if city1 == city2:
            return 0
        elif (city1, city2) in distances:
            return distances[(city1, city2)]
        else:
            return distances[(city2, city1)]
    def total_distance(self,route):
        return sum(self.distance(route[i], route[i+1]) for i in range(len(route) - 1)) + self.distance(route[-1], route[0])

    # Generate a random initial solution (i.e., a random permutation of the cities)
    def random_route(self,cities):
        route = cities[:]
        random.shuffle(route)
        return route

    # Simulated Annealing algorithm
    def simulated_annealing(self,cities, initial_temp, cooling_rate, stop_temp):
        # Initialize the current solution with the initial solution
        current_solution = self.random_route(cities)
        current_distance = self.total_distance(current_solution)
        best_solution = current_solution
        best_distance = current_distance
        temperature = initial_temp

        while temperature > stop_temp:
            # Generate a random neighboring solution by swapping two cities
            neighbor = current_solution[:]
            i, j = random.sample(range(len(cities)), 2)
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
            neighbor_distance = self.total_distance(neighbor)

            # Calculate the change in the objective function
            delta_distance = neighbor_distance - current_distance

            # Decide whether to accept the neighboring solution
            if delta_distance < 0 or random.random() < math.exp(-delta_distance / temperature):
                current_solution = neighbor
                current_distance = neighbor_distance

                # Update the best solution found
                if current_distance < best_distance:
                    best_solution = current_solution
                    best_distance = current_distance

            # Decrease the temperature
            temperature *= cooling_rate

        return best_solution, best_distance




lab6 = Lab10()
cities = ['A', 'B', 'C', 'D']
initial_temp = 10000
cooling_rate = 0.995
stop_temp = 1

# Run the algorithm and print the best solution found and its total distance
best_route, best_route_distance = lab6.simulated_annealing(cities, initial_temp, cooling_rate, stop_temp)
print("Best route found:", best_route)
print("Total distance:", best_route_distance)