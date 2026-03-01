import numpy as np

def verificar_comutativa_convolucao(sinal1, sinal2):
 
    # Calcular convolução: sinal1 * sinal2
    resultado1 = np.convolve(sinal1, sinal2, mode='full')
    
    # Calcular convolução: sinal2 * sinal1
    resultado2 = np.convolve(sinal2, sinal1, mode='full')
    
    # Verificar se são iguais (dentro de uma tolerância numérica)
    sao_iguais = np.allclose(resultado1, resultado2)
    
    return resultado1, resultado2, sao_iguais


# ============================================
# Teste 1: Sinais simples
# ============================================
print("=" * 50)
print("TESTE 1: Sinais Simples")
print("=" * 50)

sinal_a = np.array([1, 2, 3])
sinal_b = np.array([4, 5])

res1, res2, igual = verificar_comutativa_convolucao(sinal_a, sinal_b)

print(f"Sinal A: {sinal_a}")
print(f"Sinal B: {sinal_b}")
print(f"\nA * B = {res1}")
print(f"B * A = {res2}")
print(f"\nPropriedade comutativa verificada: {igual}")


# ============================================
# Teste 2: Sinais aleatórios
# ============================================
print("\n" + "=" * 50)
print("TESTE 2: Sinais Aleatórios")
print("=" * 50)

np.random.seed(42)
sinal_x = np.random.rand(5)
sinal_y = np.random.rand(3)

res1, res2, igual = verificar_comutativa_convolucao(sinal_x, sinal_y)

print(f"Sinal X: {sinal_x}")
print(f"Sinal Y: {sinal_y}")
print(f"\nX * Y = {res1}")
print(f"Y * X = {res2}")
print(f"\nPropriedade comutativa verificada: {igual}")


# ============================================
# Teste 3: Sinais com valores negativos
# ============================================
print("\n" + "=" * 50)
print("TESTE 3: Sinais com Valores Negativos")
print("=" * 50)

sinal_p = np.array([-1, 0, 1, -2])
sinal_q = np.array([2, -1, 3])

res1, res2, igual = verificar_comutativa_convolucao(sinal_p, sinal_q)

print(f"Sinal P: {sinal_p}")
print(f"Sinal Q: {sinal_q}")
print(f"\nP * Q = {res1}")
print(f"Q * P = {res2}")
print(f"\nPropriedade comutativa verificada: {igual}")


# ============================================
# Verificação com diferença numérica
# ============================================
print("\n" + "=" * 50)
print("ANÁLISE DA DIFERENÇA NUMÉRICA")
print("=" * 50)

diferenca = np.abs(res1 - res2)
print(f"Máxima diferença absoluta: {np.max(diferenca)}")
print(f"Diferença total: {np.sum(diferenca)}")