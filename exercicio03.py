notas = [8.5, 9.0, 6.5, 10.0, 7.5]
soma = 0

for nota in notas:
    soma = soma + nota

    media = soma / len(notas)
    print("A soma total das notas é:", {soma})
    print("A média da turma é:", {media})

