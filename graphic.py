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
plt.figure(figsize=(8,5), facecolor="#2c2c2cff")
plt.gca().set_facecolor("#000072ff")
plt.bar(df["nomes"], df["salarios"], label="Salario", color="#00ffe1ff")
plt.axhline(media, linestyle="--", label="Media salarial", color="red")

plt.title("Salario dos funcionarios e media salarial", color="#d9ff00ff")
plt.xlabel("Funcionário", color="#d9ff00ff")
plt.ylabel("Salario (R$)", color="#d9ff00ff")
plt.legend(facecolor="#d9ff00ff", labelcolor="#000000ff")
plt.tick_params(axis="both", labelcolor="#ffee00ff")

#grafico 2
plt.figure(figsize=(8,5), facecolor="#2c2c2cff")
plt.bar(acima_idade["nomes"], acima_idade["idades"], label="Idade (maior que 30)", color="#ffee00ff")
plt.gca().set_facecolor("#0c0063ff")
plt.title("Funcionarios com idade acima de 30 anos", color="#d9ff00ff")
plt.ylabel("Funcionario", color="#d9ff00ff")
plt.xlabel("Idade (Anos)", color="#d9ff00ff")
plt.tick_params(axis="both", labelcolor="#ffee00ff")

plt.legend(facecolor="white")
plt.show()