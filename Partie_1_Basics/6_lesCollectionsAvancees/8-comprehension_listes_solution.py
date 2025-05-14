# Liste de températures en Celsius
temperatures_celsius = [20, 25, 30, 15, 10, 35, 40]

# On garde uniquement celles > 25°C et on les convertit en Fahrenheit
temperatures_fahrenheit = [temp * 1.8 + 32 for temp in temperatures_celsius if temp > 25]

print(temperatures_fahrenheit)
# Résultat : [86.0, 95.0, 104.0]
