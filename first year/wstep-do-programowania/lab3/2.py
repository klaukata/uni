"""
zadanie 2
Napisz program, który wyświetli wartości funkcji 𝑦 = 2𝑥2 − 5𝑥 − 8, dla 𝑥 ∈ [−4, 4], z
krokiem 0.5
"""

x = -4
while x <= 4:
    y = (2*x)**2 - 5*x - 8
    print(y, end=" ")
    x = x + 0.5