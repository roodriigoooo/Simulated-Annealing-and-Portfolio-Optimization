import random
import numpy as np

def initial_solution_optimized(size, amount, mean_std):
    # Generate an optimized initial solution based on the mean returns of companies.
    # Selects companies with the highest mean returns for asset allocation.
    mean = mean_std[:,0]
    attractive_companies = np.argsort(mean)[-amount:] # Select top companies by mean return
    solution = np.zeros(size)
    solution[attractive_companies] = 1 # Allocate assets to selected companies
    return solution

def get_neighbor_performance(sol, distributions):
    # Generate a neighbor solution by reallocating assets from the least to the most attractive company.
    # Attractiveness is determined by the ratio of mean return to standard deviation.

    risk_to_reward = distributions[:,0] / distributions[:,1] # Calculate risk-to-reward ratio
    company_min = np.argmin(risk_to_reward[sol > 0])
    company_max = np.argmax(risk_to_reward)

    if sol[company_min] == 0 or company_min == company_max:
        return sol

    neig = sol.copy()
    neig[company_min] -= 1
    neig[company_max] += 1

def get_neighbor_stochastic(sol, distributions, current_eval, objective_function=objective_function, num_neighbors = 8):
    # Generate multiple better neighbor solutions and select one randomly.
    # Stochastic approach to selecting a neighbor.
    neighbors = []
    for neig in range(num_neighbors):
        neighbor = get_neighbor_performance(sol, distributions)
        eval = objective_function(distributions, neighbor)
        if eval > current_eval:
            neighbors.append(neighbor)
    if neighbors:
        return random.choice(neighbors) # Return a better neighbor if found
    else:
        return sol
