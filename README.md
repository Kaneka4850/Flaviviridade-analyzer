# 🧬 Flaviviridade Analyzer

Ferramenta interativa para análise de genomas da família *Flaviviridae*, com funcionalidades de filtragem por conteúdo GC e geração de gráficos. Ideal para estudos virológicos, bioinformática e exploração de sequências.

---

## 🚀 Tecnologias Utilizadas

- Python 3.x  
- [Biopython](https://biopython.org/)
- Pandas, NumPy  
- Matplotlib  
- Jupyter Notebook (para exploração adicional)

---

---

## ⚙️ Como Executar

### 1. Clone o repositório

bash:
git clone https://github.com/Kaneka4850/Flaviviridade-analyzer.git
cd Flaviviridade-analyzer

2. Instale as dependências

3. Inicie o Pipeline
bash:
python main.py

A partir daqui, o terminal guiará o usuário pelas seguintes etapas:
- 🔍 Análise dos genomas (.fasta)
- 🧪 Aplicação de filtro por conteúdo GC (opcional)
- 📊 Geração de gráfico GC (opcional

🔬 Funcionalidades
Análise Genômica (src/analyzer.py)
- Calcula tamanho e conteúdo GC de cada genoma
- Gera arquivo results/resumo.tsv com resumo tabular
- Exibe no terminal rankings dos maiores, menores e mais ricos em GC
Filtro GC (src/filtro_gc.py)
- Filtra genomas acima de determinado percentual de GC
- Salva o resultado como genomas_gc_acima_<valor>.tsv
Gráfico GC (src/grafico_gc.py)
- Cria histograma do conteúdo GC
- Salva a imagem como results/grafico_gc.png

🗂 Exemplos de Saída
Terminal:

✅ Foram analisados 38 genomas.

📏 Top 5 genomas mais longos:
NC_001477.1 → Dengue virus 1 | 10723 nt
...

🧬 Top 5 vírus com maior conteúdo GC:
NC_001417.1 → Yellow fever virus | GC = 52.40%
...

Gráfico
📁 O gráfico gerado será salvo como imagem em results/grafico_gc.png

📬 Autor
Projeto desenvolvido por Cleber Augusto Muniz Cunha de Souza / "Kaneka"
💡 Para dúvidas, sugestões ou colaborações: kaneka4850@gmail.com

📜 Licença
Este projeto está sob a licença MIT — sinta-se livre para usar e contribuir!




