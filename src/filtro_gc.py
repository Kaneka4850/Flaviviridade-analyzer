import pandas as pd

def filtrar_gc(limite_gc):
    arquivo = "results/resumo.tsv"
    saida = f"results/genomas_gc_acima_{int(limite_gc)}.tsv"

    df = pd.read_csv(arquivo, sep="\t")
    filtrados = df[df["GC"] > limite_gc]
    filtrados.to_csv(saida, sep="\t", index=False)

    print(f"\n✅ Genomas com GC acima de {limite_gc:.2f}%: {len(filtrados)} encontrados\n")
    for _, row in filtrados.iterrows():
        print(f"{row['ID']} → {row['Nome']} | GC = {row['GC']:.2f}%")

    print(f"\n📁 Resultado salvo em: {saida}")