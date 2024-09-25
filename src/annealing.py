import numpy as np
import matplotlib.pyplot as plt

def load_data():
    """
    Loads data from a CSV file, excluding the first row and column
    :return: Ready to use numpy array of data
    """
    file = 'https://raw.githubusercontent.com/jnin/information-systems/main/data/SP500_data.csv'
    all_data = np.genfromtxt(file, delimiter=",")
    data = all_data[1:, 1:]
    return data
    # Implement a function to load all data except the first row and first column in your code.
    # We strongly encourage you to store your data in a NumPy array.

    # return the data


def aggregate_data(data):
    """
    Aggregates stock values by computing the log-ratio of values 5 days apart.
    :param data: numpy array, 2D array of stock data
    :return: weekly_data, 2D array of the aggregated log ratio data
    """
    # Aggregate the stock value of each company in blocks of 5 days (approx. a week).
    # Note that The stock markets close during weekends.

    # The aggregation consists of computing the LogRatio (either a gain or a loss)
    # of the stock value of each company between two days, with a time lag of 5 days.
    # For instance, the first entry of the aggregate data is the LogRatio of the stock
    # market price of each company between October 13, 2006, and October 6, 2006.
    # The second entry will be the LogRatio between October 20 and October 13, and so on.

    # return the aggregated data called weekly_data
    weekly_data = np.log(data[5::5] / data[:-5:5])
    return weekly_data


def calculate_mean_std(data):
    """
    Calculates the mean and standard deviation for each column of data.
    :param data: 2D Array of aggregated data.
    :return: mean_std: Array containing means and standard deviations.
    """
    # Compute the aggregated data mean and the standard deviation for each company
    # Store them in a matrix called mean_std containing column-wise.
    # Column 0 should contain all companies' means,
    # and column 1 its corresponding standard deviation
    mean = np.mean(data, axis=0)
    deviation = np.std(data, axis=0)
    mean_std = np.vstack((mean, deviation)).T
    # Return this matrix mean_std
    return mean_std


def initial_solution(size, amount):
    """
    Generates an initial random solution for asset allocation.
    :param size: int, the number of companies.
    :param amount: int, the total units of money to allocate.
    :return: solution: a numpy array of initial allocation of assets.
    """
    # Compute the initial solution
    # Giving the 100 units of money, generate the initial asset allocation
    # assigning 1 unit to random companies

    # return the initial solution
    solution = np.zeros(size)
    solution[:amount] = 1
    np.random.shuffle(solution)
    return solution

def objective_function(distributions, sol):
    """
    Calculates the Value at Risk (VaR) for an asset allocation.
    :param distributions: A 2D numpy array where each row reprsents a company with columns for mean and standard deviation of stock returns.
    :param sol: A 1D numpy array representing the current allocation of assets.
    :return: VaR: float, Value at Risk for the allocation.
    """
    num_trials = 100
    #generate random gains for each company based on their distribution
    random_gains = np.random.normal(distributions[:, 0].reshape(-1,1), distributions[:, 1].reshape(-1,1), (distributions.shape[0], num_trials)) + 1
    total_gains = np.sum(random_gains * sol[:, np.newaxis], axis = 0)
    VaR = np.percentile(total_gains, 5) #Calculate 5th percentile
    return VaR

    # Giving the mean and standard deviation of each company computed over the aggregated data
    # and the current solution sol, compute:
    # 1. For each company, draw a random value following a normal distribution with its mean and standard deviation.
    # 2. Use these random values and the current assets allocated to each company to compute the total gain
    # 3. Repeat 100 times points 1 and 2.
    # Compute the 95% one-tailed Value at Risk over the 100 total gains


def objective_function_sharp(distributions, sol):
    """
    Calculates the Sharpe Ratio for an asset allocation.
    :param distributions: A 2D numpy array where each row reprsents a company with columns for mean and standard deviation of stock returns.
    :param sol: A 1D numpy array representing the current allocation of assets.
    :return: sharp: float, sharpe ratio for the allocation.
    """
    # Giving the mean and standard deviation of each company computed over the aggregated data
    # and the current solution sol, compute:
    # 1. For each company, draw a random value following a normal distribution with its mean and standard deviation.
    # 2. Use these random values and the current assets allocated to each company to compute the total gain
    # 3. Repeat 100 times points 1 and 2.
    # Compute the (adapted) Sharp Ratio over the 100 total gains
    # 1. Compute the mean of the gains
    # 2. Compute the standard deviation of the gains
    # 3. Apply the adapted formula for the Sharp Ratio

    # Return the sharp ratio
    # generate random gains for all companies and all trials at once
    num_trials = 100
    init_investment = np.sum(sol) #initial total investment
    total_gains = np.zeros(num_trials)

    for i in range(num_trials):
        random_gains = np.random.normal(distributions[:,0], distributions[:,1]) + 1
        total_gain = np.dot(random_gains, sol)
        total_gains[i] = total_gain

    gains_mean = np.mean(total_gains)
    gains_std = np.std(total_gains - init_investment)

    sharp = (gains_mean - init_investment) / gains_std if gains_std != 0 else 0
    return sharp


def objective_function_mdd(distributions, sol):
    """
    Compute the Maximum Drawdown (MDD) for a given solution.
    :param distributions: A 2D numpy array where each row reprsents a company with columns for mean and standard deviation of stock returns.
    :param sol: A 1D numpy array representing the current allocation of assets.
    :return: mdd: The Maximum Drawdown (MDD) calculated for the given solution.
    The MDD measures the largest single drop from peak to bototm in the value of a portfolio.
    """
    # Giving the mean and standard deviation of each company computed over the aggregated data
    # and the current solution sol, compute:
    # 1. For each company, draw a random value following a normal distribution with its mean and standard deviation.
    # 2. Use these random values and the current assets allocated to each company to compute the total gain
    # 3. Repeat 100 times points 1 and 2.
    # Compute the (adapted) maximum drawdow (mdd) over the 100 total gains
    # 1. Find the minimum gain
    # 2. Find the maximum gain
    # 3. Apply the adapted formula for mdd

    # Return the mdd
    num_trials = 100
    total_gains = np.zeros(num_trials)

    #simulate the total gains for each trial
    for i in range(num_trials):
        random_gain = np.random.normal(distributions[:, 0], distributions[:, 1]) + 1
        total_gain = np.dot(random_gain, sol)
        total_gains[i] = total_gain

    #calculate maximum drawdown
    peak = np.max(total_gains)
    trough = np.min(total_gains)
    mdd = (trough - peak) / peak
    return mdd

def get_neighbor(sol):
    """
    Generate a neighbor solution by reallocating one unit of investment from one company to another.
    :param sol: A 1D numpy array representing the current allocation of assets.
    :return: neig: A 1D numpy array representing the neighbor solution with one unit of assets reallocated.
    This function identifies companies with investments and randomly selects
    one to move a unit of investment from a valid company and to another company.
    """
    # generate a new neighbor solution
    # move one unit from one of the companies in the asset to another whatever company
    # the company receiving the unit has to be different than the company moving the unit
    # but it could be either a company already having some units or a company with 0 units

    # return the neighbor solution
    companies_with_investments = np.where(sol > 0)[0]
    company_moving = np.random.choice(companies_with_investments)
    company_pool = np.arange(len(sol))[np.arange(len(sol)) != company_moving]
    company_receiving = np.random.choice(company_pool)

    neig = sol.copy()
    neig[company_moving] -= 1
    neig[company_receiving] += 1

    return neig


def evaluate_sol(distributions, neig_sol, current_eval, best_eval, temperature, objective_function = objective_function):
    """
    Evaluate a neighbor solution and decide whether to accept it based
    on its performance and the current temeperature.
    :param distributions: A 2D numpy array of companies distributions.
    :param neig_sol: The neighbor solution to evaluate.
    :param current_eval: The evaluation score of the current solution.
    :param best_eval: The evaluation score of the best solution found so far.
    :param temperature: The current temperature in the simulated annealing process.
    :param objective_function: The objective function to be used for evaluation.
    :return: accept_neig: A boolean indicating whether the neighbor solution should be accepted.
    :return: current_eval: The updated current evaluation score after considering neighbor solution
    This function uses the metropolis criteron to decide on the acceptance
    of the neighbor solution, allowing for exploration of solution space.
    """
    neig_eval = objective_function(distributions, neig_sol) # Evalute neighbor solution
    diff = neig_eval - current_eval
    if diff > 0:
        # If the neighbor solution is better than the current solution, accept it.
        accept_neig = True
        current_eval = neig_eval
    else:
        # If the neighbor solution is worse, accept it with a probability according to the Metropolis criterion.
        p = np.random.rand()
        if p < np.exp(-diff / temperature): # metropolis criterion
            accept_neig = True
            current_eval = neig_eval
        else:
            accept_neig = False
    return accept_neig, current_eval


def simulated_annealing_optimize(data, distributions, sol, num_iter, temperature, objective_function=objective_function, beta = 1e-3):
    """
    Perform simulated annealing optimization over a given number of iterations.
    :param data: The 2D numpy array of weekly aggregated data.
    :param distributions: A 2D numpy array of companies distributions.
    :param sol: The initial solution.
    :param num_iter: The number of iterations to perform.
    :param temperature: The starting temperature for the simulated annealing process.
    :param objective_function: The objective function to optimize.
    :return: best: The best solution found during the optimization.
    :return: best_eval: The evaluation score of the best solution.
    This function iteratively explores the solution space by generating neighbor solutions.
    """
    init_eval = objective_function(distributions, sol)
    best = sol.copy()
    best_eval = init_eval
    current_sol = sol.copy()
    current_eval = init_eval

    for i in range(num_iter):
        temperature = temperature / (1 + beta * temperature)
        neighbor_sol = get_neighbor(current_sol)
        accept_neig, updated_eval = evaluate_sol(distributions, neighbor_sol, current_eval, best_eval, temperature, objective_function)

        if accept_neig:
            current_sol = neighbor_sol
            current_eval = updated_eval
            # Update best solution if the current solution is better than the best solution found so far.
            if current_eval > best_eval:
                best = current_sol.copy()
                best_eval = current_eval

    return best, best_eval