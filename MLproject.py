import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

#definindo o df
dados = {
    "marca": ["Fiat","Fiat","Ford","Ford","VW","VW","Nissan","Nissan","Toyota","Toyota"],
    "modelo": ["Uno","Palio","Focus","Mustang","Golf","Voyage","Sentra","Skyline","Corolla","Yaris"],
    "ano": [2010, 2012, 2015, 2018, 2014, 2016, 2017, 2019, 2016, 2020],
    "km": [90000, 70000, 50000, 20000, 60000, 40000, 30000, 15000, 35000, 10000],
    "combustivel": ["Flex","Flex","Gasolina","Gasolina","Flex","Flex","Gasolina","Gasolina","Flex","Flex"],
    "preco": [15000, 18000, 50000, 200000, 48000, 52000, 34000, 360000, 70000, 80000]
}

df = pd.DataFrame(dados)

x = pd.get_dummies(df.drop("preco", axis=1))
y = df[["preco"]]

#treinar o modelo 
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.3, random_state=42)


modelo = LinearRegression()
modelo.fit(x_train, y_train)

#previsao
previsao = modelo.predict(x_test)
print(previsao)
erro = np.mean(np.abs(y_test - previsao) / y_test) * 100
print(f"Porcentagem de erros: {erro:.2f}%")


plt.figure(figsize=(8,5), facecolor="#2c2c2cff")
plt.scatter(y_test, previsao, color="#00ff0dff")

minV = min(y_test.values.min(), previsao.min())
maxV = max(y_test.values.max(), previsao.max())

plt.plot([minV, maxV], [minV, maxV], color="#ffee00ff")
plt.gca().set_facecolor("#320096ff")
plt.title("Preco real vs preco previsto", color="#ffee00ff")
plt.xlabel("Preco Real", color="#ffee00ff")
plt.ylabel("Preco Previsto", color="#ffee00ff")
plt.tick_params(axis="both", labelcolor="#ffee00ff")
plt.show()