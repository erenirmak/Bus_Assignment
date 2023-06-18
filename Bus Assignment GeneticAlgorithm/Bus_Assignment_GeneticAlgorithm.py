
import numpy as np
import random

from RouteData import *

# Define a function to calculate the total cost of a bus schedule
def calculate_cost(schedule):
    total_cost = 0 # Initialize the total cost to zero
    current_location = 1 # Initialize the current location to zero (depot)
    current_time = 0 # Initialize the current time to zero (start of the day)
    prev_trip = 0
    tripped = []
    for trip in schedule: # Loop through each trip in the schedule
        if trip == -1: # If the trip is -1, it means the bus is idle for the rest of the day
            break # Break out of the loop
        else: # If the trip is not -1, it means the bus is assigned to a trip route
            trip_data = trips[trip] # Get the corresponding trip data from the trips dictionary
            tripped.append(trip) # Store information of trip route whether it is used or not
            if current_location != trip_data["start_location"]: # If the current location is not equal to the start location of the trip route
                total_cost += trip_data["cost_without_passengers"] * abs(current_location - trip_data["start_location"]) # Add the cost without passengers for moving from the current location to the start location of the trip route (assuming linear distance)
                current_time += abs(current_location - trip_data["start_location"]) # Update the current time by adding the travel time from the current location to the start location of the trip route (assuming linear distance and unit speed)
            if current_time < trip_data["start_time"]: # If the current time is less than the start time of the trip route
                total_cost += trip_data["cost_for_waiting"] * (trip_data["start_time"] - current_time) # Add the cost for waiting for the start time of the trip route
                current_time = trip_data["start_time"] # Update the current time to be equal to the start time of the trip route
            total_cost += trip_data["cost_with_passengers"] * trip_data["time_duration"] # Add the cost with passengers for performing the trip route 
            current_time += trip_data["time_duration"] # Update the current time
            current_location = trip_data["end_location"] # Update the current location to be equal to the end location of the trip route
        if current_time > MAX_TIME: # If the current time exceeds the maximum travel time
            total_cost += PENALTY # Add a large penalty cost to the total cost
        if current_location != trip_data["start_location"]:
            total_cost += PENALTY
        if trip in tripped: # if the trip route used before, add penalty
            total_cost += PENALTY

    return total_cost # Return the total cost of the schedule

# Define a function to initialize a random population of bus schedules
def initialize_population():
    population = np.empty((POP_SIZE, NUM_BUSES, NUM_TRIPS), dtype=int) # Initialize an empty numpy array for the population with shape (POP_SIZE, NUM_BUSES, NUM_TRIPS) and integer type
    for i in range(POP_SIZE): # Loop through each individual in the population
        for j in range(NUM_BUSES): # Loop through each bus in the individual
            available_trips = set(range(NUM_TRIPS)) # Initialize a set of available trips from 0 to NUM_TRIPS - 1
            for k in range(NUM_TRIPS): # Loop through each trip in the schedule
                trip = random.choice(list(available_trips) + [-1]) # Randomly choose a trip from the available trips or -1 (idle)
                if trip == -1: # If the trip is -1, it means the bus is idle for the rest of the day
                    population[i][j][k:] = -1 # Assign -1 to the rest of the schedule
                    break # Break out of the loop
                else: # If the trip is not -1, it means the bus is assigned to a trip route
                    population[i][j][k] = trip # Assign the trip to the schedule
                    available_trips.remove(trip) # Remove the trip from the available trips
    return population # Return the population

# Define a function to evaluate a population of bus schedules and return their fitness values and total costs
def evaluate_population(population):
    fitness_values = np.empty(POP_SIZE) # Initialize an empty numpy array for the fitness values with shape (POP_SIZE)
    total_costs = np.empty(POP_SIZE) # Initialize an empty numpy array for the total costs with shape (POP_SIZE)
    for i in range(POP_SIZE): # Loop through each individual in the population
        total_cost = 0 # Initialize the total cost to zero
        for j in range(NUM_BUSES): # Loop through each schedule in the individual
            total_cost += calculate_cost(population[i][j]) # Add the cost of the schedule to the total cost
        total_costs[i] = total_cost # Assign the total cost to the total costs array
        fitness_value = 1 / (total_cost + 1) # Calculate the fitness value as the inverse of the total cost plus one (to avoid division by zero)
        fitness_values[i] = fitness_value # Assign the fitness value to the fitness values array
    return fitness_values, total_costs # Return the fitness values and total costs

# Define a function to select two parents from a population based on their fitness values using roulette wheel selection
def select_parents(population, fitness_values):
    parent1 = random.choices(population, weights=fitness_values, k=1)[0] # Randomly choose one parent from the population with probability proportional to their fitness values using random.choices function (returns a list of k elements)
    parent2 = random.choices(population, weights=fitness_values, k=1)[0] # Randomly choose another parent from the population with probability proportional to their fitness values using random.choices function (returns a list of k elements)
    return parent1, parent2 # Return the two parents

# Define a function to perform crossover between two parents and produce two offspring using uniform crossover
def crossover(parent1, parent2):
    offspring1 = np.empty((NUM_BUSES, NUM_TRIPS), dtype=int) # Initialize an empty numpy array for the first offspring with shape (NUM_BUSES, NUM_TRIPS) and integer type
    offspring2 = np.empty((NUM_BUSES, NUM_TRIPS), dtype=int) # Initialize an empty numpy array for the second offspring with shape (NUM_BUSES, NUM_TRIPS) and integer type
    for i in range(NUM_BUSES): # Loop through each bus
        mask = np.random.choice([True, False], size=NUM_TRIPS, p=[CROSS_RATE, 1 - CROSS_RATE]) # Randomly generate a boolean mask with size NUM_TRIPS and probability CROSS_RATE for True and 1 - CROSS_RATE for False using numpy.random.choice function
        offspring1[i] = np.where(mask, parent1[i], parent2[i]) # Assign the elements from parent1 or parent2 to the first offspring based on the mask using numpy.where function
        offspring2[i] = np.where(mask, parent2[i], parent1[i]) # Assign the elements from parent2 or parent1 to the second offspring based on the mask using numpy.where function
    return offspring1, offspring2 # Return the two offspring

# Define a function to perform mutation on an individual and produce a new individual using bit flip mutation
def mutation(individual):
    new_individual = individual.copy() 
    for i in range(NUM_BUSES): 
        if random.random() < MUT_RATE: 
            index = random.randint(0, NUM_TRIPS - 1) 
            trip = individual[i][index] 
            bit = random.randint(0, 31) 
            mask = 1 << bit 
            new_trip = trip ^ mask 
            new_individual[i][index] = new_trip 
            if calculate_cost(new_individual[i]) > MAX_TIME: 
                new_individual[i][index] = trip
    return new_individual # Return the new individual

# Define a function to run the genetic algorithm and return the best individual and its total cost
def genetic_algorithm():
    population = initialize_population() # Initialize a random population of bus schedules
    best_individual = None # Initialize the best individual to None
    best_cost = float('inf') # Initialize the best cost to infinity
    for i in range(GENS): # Loop through each generation
        fitness_values, total_costs = evaluate_population(population) # Evaluate the population and get their fitness values and total costs
        new_population = [] # Initialize an empty list for the new population
        elite_size = int(ELITE_RATE * POP_SIZE) # Calculate the elite size as the elitism rate times the population size (assuming it is an integer)
        elite_indices = np.argsort(total_costs)[:elite_size] # Find the indices of the elite individuals in the total costs array using numpy.argsort function (returns a sorted array of indices) and slicing ([:elite_size] means taking the first elite_size elements)
        elite_individuals = population[elite_indices] # Get the corresponding elite individuals from the population using fancy indexing (passing an array of indices)
        new_population.extend(elite_individuals) # Extend the new population with the elite individuals
        for j in range((POP_SIZE - elite_size) // 2): # Loop through half of the remaining population size (assuming it is even)
            parent1, parent2 = select_parents(population, fitness_values) # Select two parents from the population based on their fitness values
            offspring1, offspring2 = crossover(parent1, parent2) # Perform crossover between the two parents and produce two offspring
            new_offspring1 = mutation(offspring1) # Perform mutation on the first offspring and produce a new offspring
            new_offspring2 = mutation(offspring2) # Perform mutation on the second offspring and produce a new offspring
            new_population.append(new_offspring1) # Append the new first offspring to the new population
            new_population.append(new_offspring2) # Append the new second offspring to the new population
        population = np.array(new_population) # Update the population with the new population (convert it to a numpy array)

        min_cost_index = np.argmin(total_costs) # Find the index of the minimum cost in the total costs array using numpy.argmin function (returns an integer)
        min_cost_individual = population[min_cost_index] # Get the corresponding individual from the population
        min_cost = total_costs[min_cost_index] # Get the corresponding cost from the total costs array
        if min_cost < best_cost: # If the minimum cost is less than the best cost
            best_individual = min_cost_individual.copy() # Update the best individual with the minimum cost individual
            best_cost = min_cost # Update the best cost with the minimum cost
        print(f"Generation {i + 1}: Best cost = {best_cost}") # Print the generation number and the best cost
    return best_individual, best_cost # Return the best individual and its total cost

# Run the genetic algorithm and get the best individual and its total cost
best_individual, best_cost = genetic_algorithm()
print(f"Best individual: {best_individual}") # Print the best individual
print(f"Best cost: {best_cost}") # Print the best cost












