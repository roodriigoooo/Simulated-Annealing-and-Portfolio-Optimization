# Simulated Annealing and Portfolio Optimization
This project implements and employs simulated annealing and Monte Carlo simulations to optimize asset allocation inside a given portfolio. 

## Authors
**Carlos Arcusa, Marc Cano, Carl Graf von Moltke and Rodrigo Sastré**

## Table of Contents

## Installation
### Prerequisites
- Python 3.x
- pip

### Steps:
1. Clone the repository.
```bash
git clone https://github.com/roodriigoooo/Simualted-Annealing-and-Portfolio-Optimization
```
2. Navigate to the project directory. 
```bash
cd Simualted-Annealing-and-Portfolio-Optimization
```
3. (Optional but recommended) Create a virtual environment
```bash
python -m venv venv
```
4. Activate the virtual environment
- On windows:
```bash
venv\Scripts\activate
```
- On macOS/Linux:
```bash
source venv/bin/activate
```
5. Install the required packages
```bash
pip install -r requirements.txt
```
## Usage
Run the main script to run the simulation:
```bash
python main.py
```
The program will create an initial, random allocation of assets and iteratively optimize it using temperature-based simmulated annealing. Note: Ensure that you have all dependencies installed and that the virtual environment, if using one, is activated. 

## Project Structure
```bash
Simulated-Annealing-and-Portfolio-Optimization/
|--main.py
|--src/
    |--__init__.py
    |--annealing.py
    |--graphs.py
    |--improvements.py
```
- **main.py**: Entry point of the project. Executes the simulation. 
- **src/**: Contains the source code modules.
  - **annealing.py**: Data pre-processing and simulated annealing functions. 
  - **graphs.py**: Functions for generating relevant graphs and visualizations. 
  - **improvements.py**: Ideas for improvements to optimize solution generation. 

## Temperature in Simulated Annealing and Exploration-Exploitation
The concept of temperature in simulated annealing is analogous to the physical process of annealing in metallurgy. Higher temperatures will allow the algorithm to explore a wider range of states, with the aim of escaping local optima. This is particularly important in the early stages of the simulation, where the goal is to explore as diverse the solution space as thoroughly as possible. In the context of investment portfolios, which exhibit a noisy, volatile return structure, setting a high initial temperature will allow us to sample a broad spectrum of asset allocations, aiding us in identifying portfolios that relatively robust to unpredictable market movements.

Acknowledging the inherently noisy structure of investment returns, the goal was to identify an optimal starting temperature. A temperature range within which the optimized final values showed significant fluctuation was identified, and an empirical analysis within this range then guided us in pinpointing a temperature that balanced the need for wide-ranging exploration with the practical necessity of convergence towards an effective allocation. 

The graphs below show the optimized values vs. initial temperatures: 

**VaR vs. Init.Temp:**
![VaR vs. Init. Temp.](./drawdown_vs_temp.jpg)

**Sharpe Ratio vs. Init.Temp:**
![Sharpe Ratio vs. Init. Temp.](./sharpe_vs_temp.jpg)

**Max.Drawdown vs. Init. Temp:**
![Max. Drawdown vs. Init. Temp.](./drawdown_vs_temp.jpg)

The cooling schedule determines how the temperature decreases over time. In this project the Lundy and Mees cooling scheme is employed:

\( t_{i+1} = \frac{t_i}{1 + \beta t_i} \)

where \(t_i\) is the temperature at the current iteration and beta is a control parameter determining the rate of temperature decrease

The parameter beta needs to be small to ensure that the temperature decreases slowly when it is high, prompting exploration of the solution space. This temperature schedule is benefitial for many reasons:
- Adaptability: This scheme adapts to the optimization process.
- Exploration-Exploitation Balance: Given the inherent volatility and unpredictability of financial markets, the sceme offers a balanced approach, where the risk of getting trapped in a local optima early on is reduced, while ensuring that the search does not become too diffuse. 
- Empirical Tuning: The beta parameter can be tuned based on preliminary runs. 

![Beta vs. Optimized Values for Different Initial Temperatures](./diffbetavalues.jpg)

In the plot above, for instance, we can see that an initial temperature of 100 is more optimal than that of 50 or 150. More relevantly, we can visualize what beta values are more optimal for each one of our variables to optimize. 
Namely, the formula used for our cooling schedule is:

\( t_{i+1} = \frac{t_i}{1 + 10^{-3} t_i} \)

The choice of this cooling schedule is particulary justified by its alignment with the nature of financial markets. Investment returns can exhibit significant short-term fluctuations but tend to follow more predictable patterns over longer periods. 

## Results and Improvements
Our simulated annealing approach successfully minimized VaR, highlighting its potential to reduce downside risk. Key parameters such as initial temperature and beta influenced the results, with higher temperatures enabling a broader exploration of asset allocations, potentially involving higher risks but offering better diversification. VaR minimization tends to focus on loss prevention, often resulting in conservative portfolios that prioritize stability over growth.

When optimizing for the Sharpe Ratio, the algorithm balances risk and return more directly, guiding the optimization toward higher-risk allocations with potential for greater returns. This contrasts with VaR optimization, where the focus is purely on risk minimization. Sharpe Ratio optimization often leads to more aggressive asset allocations, showcasing a different risk-return trade-off.

Optimizing for Maximum Drawdown (MDD) shifts the focus toward resilience during downturns, avoiding significant losses from peak to trough. This often results in highly diversified portfolios, which may sacrifice growth for stability. MDD optimization yielded allocations distinct from both VaR and Sharpe Ratio approaches, prioritizing stability over potential gains.

Comparing asset allocations from each objective function reveals fundamental trade-offs in investment strategy. VaR leads to conservative, risk-averse strategies, Sharpe Ratio balances risk and return, and MDD focuses on avoiding significant losses. Each approach suits different investor profiles, whether focused on risk minimization, balanced growth, or stability.

Two major improvements to the portfolio optimization algorithm were implemented:
1. **Optimized Initial Solution Generation:** Instead of random allocation, the initial solution is based on historical performance, selecting top-performing companies for initial investments. This adjustment accelerates the algorithm’s convergence toward better portfolio allocations.
   
2. **Alternative Neighbor Generation Methods:**
   - **Performance-Based Reallocation:** Moves investments from low-performing to high-performing assets based on a risk-reward ratio.
   - **Stochastic Neighbor Selection:** Generates and selects better neighbor solutions stochastically, improving exploration of the solution space.

These strategies enhance the algorithm’s efficiency and effectiveness, leading to significant performance improvements:
- **VaR (95% Confidence Level):** Before: $99.55 → After: $99.75
- **Sharpe Ratio:** Before: 0.52 → After: 0.97
- **Maximum Drawdown:** Before: -0.0187 → After: -0.0170

## License
This project is licensed under the MIT license - see the [LICENSE](LICENSE.txt) file for details. 

## References
Lundy, M., & Mees, A. (1986). Convergence of an annealing algorithm. *Mathematical Programming, 34*(1), 111-124. https://doi.org/10.1007/BF01582166

 


