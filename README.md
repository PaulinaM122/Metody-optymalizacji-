# Optimization Methods Comparison

This script compares the performance of three optimization methods: gradient descent, simulated annealing, and random search. Each method aims to minimize the objective function \(f(x, y) = 4x^2 - 4xy + 2y^2\).

## Optimization Methods

### Gradient Descent

Gradient descent is an iterative optimization algorithm that aims to find the minimum of a function by taking steps proportional to the negative of the gradient of the function at the current point.

### Simulated Annealing

Simulated annealing is a probabilistic optimization algorithm inspired by the process of annealing in metallurgy. It randomly selects neighboring points and probabilistically accepts or rejects them based on the energy difference between the current and new points.

### Random Search

Random search is a simple optimization algorithm that randomly samples points from the search space and selects the point with the lowest function value.

## How to Run

To run the comparison between the three optimization methods, simply execute the `main.py` script.

```bash
python main.py
```

## Results

The script will print out the results of each optimization method, including the values of \(x\), \(y\), and the function \(f(x, y)\) at the optimal point found by each method.
