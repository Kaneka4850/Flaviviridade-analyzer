from src import analyzer, filtro_gc, grafico_gc

def rodar_analyzer():
    print("\n🔍 Executando análise dos genomas...")
    analyzer.analisar_genomas()

def rodar_filtro_gc():
    try:
        limite_gc = float(input("\n💡 Digite o limite mínimo de GC (%): "))
        filtro_gc.filtrar_gc(limite_gc)
    except ValueError:
        print("❌ Valor inválido. Por favor, digite um número.")

def gerar_grafico():
    print("\n📊 Gerando gráfico de distribuição GC...")
    grafico_gc.gerar_grafico_gc()

def executar_pipeline():
    print("\n=== 🧬 Genoma Analyzer ===")
    rodar_analyzer()

    aplicar_filtro = input("\n👉 Deseja aplicar filtro GC? (s/n): ").lower()
    if aplicar_filtro == "s":
        rodar_filtro_gc()

    gerar = input("\n👉 Deseja gerar gráfico GC? (s/n): ").lower()
    if gerar == "s":
        gerar_grafico()

    print("\n✅ Pipeline finalizado! Confira os arquivos na pasta 'results/'")

def main():
    while True:
        executar_pipeline()
        escolha = input("\n🔁 Deseja realizar outra análise?\nDigite [1] para SIM ou [2] para ENCERRAR: ")

        if escolha == "1":
            continue
        elif escolha == "2":
            print("\nObrigado por usar o Genoma Analyzer! Até a próxima")
            break
        else:
            print("\n❌ Entrada inválida. Encerrando por segurança.")
            break

if __name__ == "__main__":
    main()