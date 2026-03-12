import matplotlib.pyplot as plt
import pandas as pd
import requests

url = "https://randomuser.me/api/?results=100"

respuesta = requests.get(url, timeout=10)
data = respuesta.json()
usuarios = data["results"]

registros = []

for usuario in usuarios:
    registros.append(
        {
            "pais": usuario["location"]["country"],
            "edad": usuario["dob"]["age"],
        }
    )

df_usuarios = pd.DataFrame(registros)

df_promedio_edades = (
    df_usuarios.groupby("pais", as_index=False)["edad"]
    .mean()
    .rename(columns={"edad": "promedio_edad"})
    .sort_values("promedio_edad", ascending=False)
)

print(df_promedio_edades)

plt.figure(figsize=(12, 6))
plt.bar(df_promedio_edades["pais"], df_promedio_edades["promedio_edad"], color="steelblue")
plt.title("Promedio de edad por pais")
plt.xlabel("Pais")
plt.ylabel("Promedio de edad")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()
