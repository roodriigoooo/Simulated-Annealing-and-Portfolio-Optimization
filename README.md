# Simulated-Annealing-and-Portfolio-Optimization
This Python programs implements fin. data analysis for stock price movements using the S&amp;P 500 dataset. It simulates portfolio allocation strategies through the employment of optimization techniques to enhance asset allocation.

Overview
This program is designed for analyzing and optimizing stock investment strategies based on historical S&P 500 data. It uses NumPy for data manipulation and Matplotlib for visualizations. The primary functionalities include data loading, data aggregation into weekly changes, statistical analysis, and implementation of several financial metrics to assess investment risks and returns. The program also incorporates a simulated annealing algorithm to optimize portfolio allocations under different risk and return metrics.


Components
Data Loading:
load_data(): Fetches historical stock data from a CSV file hosted online, specifically formatted to exclude the first row and column which typically contain non-numerical data.

Data Aggregation:
aggregate_data(data): Converts daily stock prices into weekly data by calculating the logarithmic ratio of prices 5 days apart.

Statistical Calculations:
calculate_mean_std(data): Computes the mean and standard deviation for each stock over the aggregated data, useful for understanding the overall volatility and average returns.

Portfolio Simulation Tools:
initial_solution(size, amount): Generates a random initial asset allocation across different stocks.
objective_function(distributions, sol): Calculates the Value at Risk (VaR) for a given portfolio.
objective_function_sharp(distributions, sol): Computes the Sharpe Ratio to assess the risk-adjusted return.
objective_function_mdd(distributions, sol): Determines the Maximum Drawdown, indicating potential losses.

Optimization Algorithm:
simulated_annealing_optimize(data, distributions, sol, num_iter, temperature): Applies simulated annealing to find an optimal asset allocation, minimizing risk and maximizing returns under the given objective function.

Visualization Functions:
temperature_effect(...): Visualizes how the initial temperature in the simulated annealing process impacts the optimization results.
beta_vs_final_value(...): Shows the effect of the cooling rate (beta) on the final optimized values under varying temperatures.

Usage
Run the program to load data, perform analyses, and optimize portfolio strategies. The outputs include initial and optimized financial metrics such as VaR, Sharpe Ratio, and Maximum Drawdown, along with visualizations that demonstrate the effects of various parameters in the simulated annealing process.


This program offers a comprehensive toolkit for quantitative analysis and optimization of investment strategies in the stock market using advanced computational techniques. It allows users to make informed decisions based on historical data and statistical analysis.
