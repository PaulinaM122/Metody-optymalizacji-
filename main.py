import math
import random

# Funkcja obliczająca wartość funkcji f(x, y)
def f(x, y):
    return 4 * x**2 - 4 * x * y + 2 * y**2

# Metoda gradientowa
def gradient_descent():
    # Początkowe wartości x i y
    x = random.uniform(-10, 10)
    y = random.uniform(-10, 10)
    learning_rate = 0.1
    precision = 0.0001

    while True:
        # Obliczanie gradientu
        gradient_x = 8 * x - 4 * y
        gradient_y = -4 * x + 4 * y

        # Aktualizacja wartości x i y
        x = x - learning_rate * gradient_x
        y = y - learning_rate * gradient_y

        # Sprawdzenie warunku stopu
        if math.sqrt(gradient_x**2 + gradient_y**2) < precision:
            break

    return x, y

# Metoda symulowanego wyżarzania
def simulated_annealing():
    # Początkowe wartości x i y
    x = random.uniform(-10, 10)
    y = random.uniform(-10, 10)
    temperature = 100.0
    cooling_rate = 0.02

    while temperature > 0.1:
        # Generowanie nowych punktów wokół obecnej pozycji
        new_x = random.uniform(-1, 1) + x
        new_y = random.uniform(-1, 1) + y

        # Obliczanie różnicy energii (wartości funkcji) pomiędzy obecnym a nowym punktem
        energy_diff = f(new_x, new_y) - f(x, y)

        # Akceptacja nowego punktu z pewnym prawdopodobieństwem
        if energy_diff < 0 or random.random() < math.exp(-energy_diff / temperature):
            x = new_x
            y = new_y

        # Obniżanie temperatury
        temperature *= 1 - cooling_rate

    return x, y

# Metoda szukania przypadkowego
def random_search():
    best_x = None
    best_y = None
    best_value = float('inf')
    num_iterations = 100

    for _ in range(num_iterations):
        x = random.uniform(-10, 10)
        y = random.uniform(-10, 10)
        value = f(x, y)

        # Aktualizacja najlepszego wyniku
        if value < best_value:
            best_x = x
            best_y = y
            best_value = value

    return best_x, best_y

# Porównanie wyników dla trzech metod
gradient_result = gradient_descent()
sa_result = simulated_annealing()
random_result = random_search()

print("Metoda gradientowa:")
print("x =", gradient_result[0])
print("y =", gradient_result[1])
print("Wartość funkcji =", f(gradient_result[0], gradient_result[1]))
print()

print("Metoda symulowanego wyżarzania:")
print("x =", sa_result[0])
print("y =", sa_result[1])
print("Wartość funkcji =", f(sa_result[0], sa_result[1]))
print()

print("Metoda szukania przypadkowego:")
print("x =", random_result[0])
print("y =", random_result[1])
print("Wartość funkcji =", f(random_result[0], random_result[1]))
