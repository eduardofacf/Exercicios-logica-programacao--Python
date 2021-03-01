n = int(input("Quantos numeros voce vai digitar? "))

vet = [0 for x in range(n)]

soma = 0
for i in range(0, n):
    vet[i] = float(input("Digite um numero: "))
    soma = soma + vet[i]

print()
print("VALORES = ", end="")
for i in range(0, n):
    print(f"{vet[i]:.1f} ", end="")

print()
print(f"SOMA = {soma:.2f}")

media = soma / n
print(f"MEDIA = {media:.2f}")
