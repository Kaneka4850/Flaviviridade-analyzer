import pandas as pd
import matplotlib.pyplot as plt
import os

def gerar_grafico_gc():
    arquivo = "results/resumo.tsv"
    df = pd.read_csv(arquivo, sep="\t")

    os.makedirs("results", exist_ok=True)

    plt.figure(figsize=(10, 6))
    plt.hist(df["GC"], bins=20, color="#ff69b4", edgecolor="black")
    plt.title("Distribuição do conteúdo GC nos genomas de Flavivírus")
    plt.xlabel("GC (%)")
    plt.ylabel("Número de genomas")
    plt.grid(True)

    grafico = "results/grafico_gc.png"
    plt.savefig(grafico)
    plt.close()

    print(f"✅ Gráfico gerado com sucesso e salvo em: {grafico}")