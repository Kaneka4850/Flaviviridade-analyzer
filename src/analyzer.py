from Bio import SeqIO
from Bio.SeqUtils import gc_fraction

def analisar_genomas():
    arquivo = "data/Flaviviridae-genomes.fasta"
    saida = "results/resumo.tsv"
    dados = []

    with open(saida, "w") as out:
        out.write("ID\tNome\tTamanho\tGC\n")
        for registro in SeqIO.parse(arquivo, "fasta"):
            nome = registro.description.replace(registro.id + " ", "")
            tamanho = len(registro.seq)
            gc = gc_fraction(registro.seq) * 100
            out.write(f"{registro.id}\t{nome}\t{tamanho}\t{gc:.2f}\n")
            dados.append({"id": registro.id, "nome": nome, "tamanho": tamanho, "gc": gc})

    print(f"\n✅ Foram analisados {len(dados)} genomas.\n")
    print("📏 Top 5 genomas mais longos:")
    for item in sorted(dados, key=lambda x: x["tamanho"], reverse=True)[:5]:
        print(f"{item['id']} → {item['nome']} | {item['tamanho']} nt")

    print("\n📏 Top 5 genomas mais curtos:")
    for item in sorted(dados, key=lambda x: x["tamanho"])[:5]:
        print(f"{item['id']} → {item['nome']} | {item['tamanho']} nt")

    print("\n🧬 Top 5 vírus com maior conteúdo GC:")
    for item in sorted(dados, key=lambda x: x["gc"], reverse=True)[:5]:
        print(f"{item['id']} → {item['nome']} | GC = {item['gc']:.2f}%")
    
    print("\n🧬 Top 5 vírus com menor conteúdo GC:")
    for item in sorted(dados, key=lambda x: x["gc"])[:5]:
        print(f"{item['id']} → {item['nome']} | GC = {item['gc']:.2f}%")