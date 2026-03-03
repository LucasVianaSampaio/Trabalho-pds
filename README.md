# Verificação Numérica da Propriedade de Convolução

Este projeto é um script em Python desenvolvido para verificar numericamente a **propriedade comutativa da convolução** discreta. Através do uso da biblioteca `NumPy`, o código calcula a convolução de dois sinais em ordens diferentes e compara os resultados para confirmar se $x * y = y * x$.

## 📋 Funcionalidades

- **Função de Verificação:** Implementação da função `verificar_comutativa_convolucao` que retorna os resultados das duas ordens de convolução e um booleano indicando se são iguais.
- **Testes Diversificados:**
  1.  **Sinais Simples:** Arrays inteiros pequenos para verificação manual.
  2.  **Sinais Aleatórios:** Arrays com valores de ponto flutuante gerados aleatoriamente.
  3.  **Sinais com Negativos:** Arrays contendo valores negativos para testar robustez.
- **Análise de Erro:** Cálculo da diferença absoluta máxima e total entre os resultados para análise de precisão numérica.

## 🛠️ Pré-requisitos

Para executar este projeto, você precisará ter instalado:
- Python 3.x
- Biblioteca `numpy`

## 📦 Instalação

1.  Clone ou baixe este repositório.
2.  Instale as dependências necessárias:

```bash
pip install numpy
```

## 🟰 Resultados
<img width="697" height="581" alt="image" src="https://github.com/user-attachments/assets/96ae5963-627a-4127-8d7d-0fb2f019a579" />
