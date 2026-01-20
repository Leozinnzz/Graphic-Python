import pandas as pd
import matplotlib.pyplot as plt

data = {
    "nomes": ["Joao", "Maria", "Pedro", "Jose", "Leo"],
    "idades": [22, 46, 31, 35, 19],
    "salarios": [1700, 2800, 800, 950, 1500]
}

df = pd.DataFrame(data)

media = df["salarios"].mean()
maior = df["salarios"].max()
menor = df["salarios"].min()

acima_idade = df[df["idades"] > 30]
acima_media = df[df["salarios"] > media]

#grafico 1
plt.figure(figsize=(8,5))
plt.bar(df["nomes"], df["salarios"], label="Salario")
plt.axhline(media, linestyle="--", label="Media salarial")

plt.title("Salario dos funcionarios e media salarial")
plt.xlabel("Funcionário")
plt.ylabel("Salario (R$)")


#grafico 2
plt.figure(figsize=(8,5))
plt.bar(acima_idade["nomes"], acima_idade["idades"], label="Idade (maior que 30)")


plt.title("Funcionarios com idade acima de 30 anos")
plt.ylabel("Funcionario")
plt.xlabel("Idade (Anos)")

plt.legend()
plt.show()