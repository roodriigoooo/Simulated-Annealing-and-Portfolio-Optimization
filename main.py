import numpy as np

from src.annealing import (load_data, aggregate_data, calculate_mean_std, initial_solution, objective_function,
                           objective_function_sharp, objective_function_mdd, simulated_annealing_optimize)

# Constants
initial_amount = 100
max_iters = 100  # Number of generated random values for the calculation
# of the 95% VaR in objective function
temperature = 110

repetitions = 100  # Main loop of the simulated annealing

np.random.seed(0)  # For reproducibility, i.e.,
# different executions of the same code
# will generate the same random numbers
# Keep it to check if the code works
# Comment it to check it the code is able
# to optimise any combination of randon numbers


data = load_data()
print("Data shape ", data.shape)

# MAIN
data = load_data()
print("Data shape ", data.shape)

data_week = aggregate_data(data)
print("Weekly data shape ", data_week.shape)

data_mean_std = calculate_mean_std(data_week)

isolution = initial_solution(data_week.shape[1], initial_amount)
print("Selected companies: ", isolution)

VaR_95 = objective_function(data_mean_std, isolution)
sharp = objective_function_sharp(data_mean_std, isolution)
drawdown = objective_function_mdd(data_mean_std, isolution)

print(f"\nValue at Risk (VaR) at 95% confidence level: ${VaR_95:,.2f}")

print(f"\nInitial Sharpe Ratio: {sharp:,.2f}")

print(f"\nInitial Maximum Drawdown: {drawdown:,.4f}")

best, best_var_eval = simulated_annealing_optimize(data_week, data_mean_std, isolution,
                                                   repetitions, temperature, objective_function)
best_sharpe, best_sharpe_eval = simulated_annealing_optimize(data_week, data_mean_std, isolution,
                                                             repetitions, temperature, objective_function_sharp)
best_mdd, best_mdd_eval = simulated_annealing_optimize(data_week, data_mean_std, isolution,
                                                       repetitions, temperature, objective_function_mdd)
print("Selected companies: ", best)

print("Selected companies for optimized Sharpe Ratio: ", best_sharpe)

print("Selected companies for optimized Drawdown: ", best_mdd)

print(f"\nValue at Risk (VaR) at 95% confidence level: ${best_var_eval:,.2f}")

print(f"\n Optimized Sharpe Ratio: {best_sharpe_eval:,.2f}")

print(f"\n Optimized Maximum Drawdown: {best_mdd_eval:,.4f}")