#Dados do funcionário em forma de variáveis...
nome_funcionario = "Carlos Silva"
salario_bruto = 5000.00
taxa_inss = 0.10 # 10% de INSS
taxa_irrf = 0.15 # 15% IRRF

#Ajuste rápido para nova pessoa
nome_funcionario = "Ana Costa"
salario_bruto = 6200.00
# ... (o resto do código permanece igual!)


nome_funcionario = "João Santos"
salario_bruto =  3000.00


# Cálculo de descontos
desconto_inss = salario_bruto * taxa_inss
desconto_irrf = salario_bruto * taxa_irrf
salario_liquido = salario_bruto - desconto_inss - desconto_irrf

print(f"Funcionário: {nome_funcionario}")
print(f"Salário Bruto: R$ {salario_bruto:.2f}")
print(f"Desconto INSS: R$ {desconto_inss:.2f}")
print(f"Desconto IRRF: R$ {desconto_irrf:.2f}")
print(f"Salário Líquido: R$ {salario_liquido:.2f}")





