# -*-
# 1. Calcular o IMC dos funcionário
#
# 2. Classificar according to OMS
#
# 3. Gerar relatórios personalizados
#
# 4. Armazenar os resultados -*-




# MÓDULO: saúde_corporativa.py
# -*- coding: utf-8 -*-

def calcular_imc(peso, altura):
    """
    Calcula o Índice de Massa Corporal (IMC)
    """
    return peso / (altura ** 2)

def classificar_imc(imc):
    """
    Classifica o IMC according to padrões OMS
    """
    if imc < 18.5:
        return "Baixo peso"
    elif 18.5 <= imc < 25:
        return "Peso adequado"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidade"

def gerar_relatorio(nome, imc, classificacao):
    """
    Gera um relatório formatado para o funcionário
    """
    relatorio = f"""
    RELATÓRIO DE SAÚDE - {nome.upper()}
    IMC: {imc:.2f}
    Classificação: {classificacao}
    """
    return relatorio

def armazenar_resultado(nome, dados, arquivo="dados_saude.txt"):
    """
    Armazena os resultados em um arquivo
    """
    with open(arquivo, 'a') as file:
        file.write(f"{nome}: {dados}\n")

# Função principal que orquestra o processo
def analisar_saude_funcionario():
    """
    Fluxo principal de análise de saúde
    """
    print("=== SISTEMA DE ANÁLISE DE SAÚDE ===")

    # Entrada de dados
    nome = input("Nome do funcionário: ")
    peso = float(input("Peso (kg): "))
    altura = float(input("Altura (m): "))

    # Cálculos
    imc = calcular_imc(peso, altura)
    classificacao = classificar_imc(imc)

    # Saída
    relatorio = gerar_relatorio(nome, imc, classificacao)
    print(relatorio)

    # Armazenamento
    armazenar_resultado(nome, f"IMC: {imc:.2f} - {classificacao}")
    print("Dados armazenados com sucesso!")

# Execução do programa
if __name__ == "__main__":
    analisar_saude_funcionario()