vendas = [850, 1320, 940, 2000, 760, 400, 1890]

bons_dias = 0
dias_ruins = 0
total_vendas = 0

for valor in vendas:
    total_vendas += valor

    if valor > 1000:
        bons_dias += 1
    elif valor < 500:
        dias_ruins += 1

media = total_vendas / len(vendas)

print("===== RELATÓRIO DE VENDAS =====")
print("Total vendido na semana: R$", total_vendas)
print("Média de vendas diárias: R$", round(media, 2))
print("Dias com boas vendas:", bons_dias)
print("Dias com vendas baixas:", dias_ruins)



s = 0
for i in range(5):
    s += 3 * i
print("A resposta é:", s)
