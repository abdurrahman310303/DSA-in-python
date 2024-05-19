import random
import string

# Target string
target_string = "Gate Smashers"

# Genetic algorithm parameters
population_size = 100
mutation_rate = 0.01
generations = 1000

# Function to generate a random individual
def generate_individual():
    return ''.join(random.choice(string.ascii_letters + " ") for _ in range(len(target_string)))

# Function to calculate fitness of an individual
def calculate_fitness(individual):
    return sum(1 for i in range(len(target_string)) if individual[i] == target_string[i])

# Function to perform crossover
def crossover(parent1, parent2):
    crossover_point = random.randint(0, len(target_string) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

# Function to perform mutation
def mutate(individual):
    mutated_individual = list(individual)
    for i in range(len(mutated_individual)):
        if random.random() < mutation_rate:
            mutated_individual[i] = random.choice(string.ascii_letters + " ")
    return ''.join(mutated_individual)

# Initialize population
population = [generate_individual() for _ in range(population_size)]

# Evolution loop
for generation in range(generations):
    # Calculate fitness for each individual
    fitness_scores = [calculate_fitness(individual) for individual in population]

    # Find the best individual in the population
    best_individual = population[fitness_scores.index(max(fitness_scores))]
    
    # Print best individual in the current generation
    print(f"Generation {generation}: {best_individual} (Fitness: {max(fitness_scores)})")

    # Check for termination condition
    if max(fitness_scores) == len(target_string):
        break

    # Selection
    selected_parents = random.choices(population, weights=fitness_scores, k=2)

    # Crossover
    child1, child2 = crossover(selected_parents[0], selected_parents[1])

    # Mutation
    child1 = mutate(child1)
    child2 = mutate(child2)

    # Replace old population with new population
    population = population + [child1, child2]

print("Evolution completed.")
