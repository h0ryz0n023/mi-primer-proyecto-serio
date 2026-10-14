import random
integrantes = ["Rosé", "Jisoo", "Lisa", "Jennie"]

edad = int(input("¿Que edad tienes?"))

bias = random.choice(integrantes)

print(f"\nTienes {edad} años.")
print(f"Este es tu Bias de BLACKPINK: {bias }!")

if edad < 13:
        print("Eres muy joven, pero ya tienes buen gusto.")
elif edad < 18:
        print("Edad perfecta para ser fan de blackpink.!")
elif edad < 30:
        print("Fan de toda la vida, se nota.")
else:
    print("El K-Pop no tiene edad")

print(f"\nEste es tu Bias de Blackpink: {bias}")
print("========================================")

