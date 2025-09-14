print("Digite 10 números (um deles tem que ser o da chamada)")

numeros = [int(input(f"Digite o {i+1}º número: ")) for i in range(10)]

print("\nOriginal:", numeros)
print("Ordenada:", sorted(numeros))
print("Sem repetições:", sorted(set(numeros)))
