import matplotlib.pyplot as plt
import numpy as np


from .annealing import simulated_annealing_optimize, objective_function, objective_function_sharp, objective_function_mdd


def temperature_effect(data, distributions, sol, num_iter, temp_range, num_simulations, objective_function, label):
    avg_final_values = []
    temps = np.linspace(temp_range[0], temp_range[1], 30)

    for temp in temps:
        temp_values = []
        for i in range(num_simulations):
            i, best_eval = simulated_annealing_optimize(data, distributions, sol, num_iter, temp, objective_function)
            temp_values.append(best_eval)

        avg_final_values.append(np.mean(temp_values))

    plt.figure(figsize = (10,6))
    plt.plot(temps, avg_final_values, marker = "o", linestyle = "-", color = "b")
    plt.title(f"Final {label} vs Initial Temperatures")
    plt.xlabel("Initial Temperatures")
    plt.ylabel(f"{label}")
    plt.grid(True)
    plt.show()


def beta_vs_final_value(data, distributions, sol, num_iter, betas, temperatures, objective_function=objective_function):
    results = {temp: [] for temp in temperatures}
    for beta in betas:
        for temp in temperatures:
            _, best_eval = simulated_annealing_optimize(
                data, distributions, sol, num_iter, temp, objective_function, beta=beta)
            results[temp].append(best_eval)

    plt.figure(figsize=(12,8))
    for temp in temperatures:
        plt.plot(betas, results[temp], marker = "o", linestyle = "-", label = f"Temp: {temp}")
    plt.title('Beta vs. Final Optimized Value for Different Initial Temperatures')
    plt.xlabel('Beta Value')
    plt.ylabel('Final Optimized Value')
    plt.xscale('log')  # Since beta is better explored on a logarithmic scale
    plt.legend()
    plt.grid(True)
    plt.show()