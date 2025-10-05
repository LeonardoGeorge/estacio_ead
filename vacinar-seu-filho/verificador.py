idade = int(input("Informe a idade da criança: "))

if idade < 5:
    print("A criança deve ser vacinada")
    print("Procure o posto de saúde mais proximo")
    print("A Saúde vem em primeiro lugar")
elif idade == 5:
    print("Se a criança não foi vacinada, deve vaciná-la o mais rápido possível")
    print("Procure o posto de saúde mais proximo")
    print("A Saúde vem em primeiro lugar")
else:  # idade > 5
    # Precisamos perguntar se a criança foi vacinada
    vacinada = input("A criança já foi vacinada? (sim/não): ").strip().lower()
    if vacinada == 'sim':
        print("Parabéns você vacinou seu filho")
    else:
        print("Vacine seu filho imediatamente")
        print("Procure o posto de saúde mais proximo")
        print("A Saúde vem em primeiro lugar")