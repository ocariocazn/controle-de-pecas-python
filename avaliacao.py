CAPACIDADE_CAIXA = 10

pecas = []
caixas_fechadas = []
caixa_atual = []


def avaliar_peca(peso, cor, comprimento):
    aprovada = True
    motivo = ""

    if peso < 95 or peso > 105:
        aprovada = False
        motivo += "Peso fora do padrão; "

    cor = cor.lower()
    if cor != "azul" and cor != "verde":
        aprovada = False
        motivo += "Cor não permitida; "

    if comprimento < 10 or comprimento > 20:
        aprovada = False
        motivo += "Comprimento fora do padrão; "

    if aprovada:
        return "APROVADA", ""
    else:
        return "REPROVADA", motivo


def recalcular_caixas():
    global caixas_fechadas, caixa_atual

    caixas_fechadas = []
    caixa_atual = []

    caixa_temp = []

    for peca in pecas:
        if peca["status"] == "APROVADA":
            caixa_temp.append(peca["id"])

            if len(caixa_temp) == CAPACIDADE_CAIXA:
                caixas_fechadas.append(caixa_temp)
                caixa_temp = []

    caixa_atual = caixa_temp


def cadastrar_peca():
    print("\n=== CADASTRAR NOVA PEÇA ===")
    id_peca = input("ID da peça: ")
    peso = float(input("Peso (g): "))
    cor = input("Cor: ")
    comprimento = float(input("Comprimento (cm): "))

    status, motivo = avaliar_peca(peso, cor, comprimento)

    nova_peca = {
        "id": id_peca,
        "peso": peso,
        "cor": cor,
        "comprimento": comprimento,
        "status": status,
        "motivo": motivo
    }

    pecas.append(nova_peca)
    recalcular_caixas()

    print(f"\nPeça {id_peca} cadastrada como {status}.")
    if status == "REPROVADA":
        print("Motivo(s):", motivo)


def listar_pecas():
    print("\n=== LISTAR PEÇAS APROVADAS/REPROVADAS ===")
    if len(pecas) == 0:
        print("Nenhuma peça cadastrada.")
        return

    for p in pecas:
        print("---------------------------------")
        print(f"ID: {p['id']}")
        print(f"Peso: {p['peso']} g")
        print(f"Cor: {p['cor']}")
        print(f"Comprimento: {p['comprimento']} cm")
        print(f"Status: {p['status']}")
        if p["status"] == "REPROVADA":
            print("Motivo(s):", p["motivo"])


def remover_peca():
    print("\n=== REMOVER PEÇA CADASTRADA ===")
    if len(pecas) == 0:
        print("Nenhuma peça cadastrada.")
        return

    id_remover = input("Digite o ID da peça que deseja remover: ")

    encontrada = False
    for i in range(len(pecas)):
        if pecas[i]["id"] == id_remover:
            encontrada = True
            del pecas[i]
            recalcular_caixas()
            print(f"Peça {id_remover} removida com sucesso.")
            break

    if not encontrada:
        print("Peça não encontrada.")


def listar_caixas_fechadas():
    print("\n=== LISTAR CAIXAS FECHADAS ===")
    if len(caixas_fechadas) == 0:
        print("Nenhuma caixa fechada ainda.")
        return

    for indice, caixa in enumerate(caixas_fechadas, start=1):
        print(f"Caixa {indice}: {caixa}")


def gerar_relatorio_final():
    print("\n=== RELATÓRIO FINAL ===")

    total_aprovadas = 0
    total_reprovadas = 0
    reprov_peso = 0
    reprov_cor = 0
    reprov_comp = 0

    for p in pecas:
        if p["status"] == "APROVADA":
            total_aprovadas += 1
        else:
            total_reprovadas += 1
            if "Peso fora do padrão" in p["motivo"]:
                reprov_peso += 1
            if "Cor não permitida" in p["motivo"]:
                reprov_cor += 1
            if "Comprimento fora do padrão" in p["motivo"]:
                reprov_comp += 1

    print("Total de peças APROVADAS:", total_aprovadas)
    print("Total de peças REPROVADAS:", total_reprovadas)
    print("\nMotivos de reprovação:")
    print(" - Peso fora do padrão:", reprov_peso)
    print(" - Cor não permitida:", reprov_cor)
    print(" - Comprimento fora do padrão:", reprov_comp)
    print("\nQuantidade de caixas FECHADAS:", len(caixas_fechadas))
    print("Peças na caixa atual (aberta):", len(caixa_atual))


while True:
    print("\n========== MENU ==========")
    print("1 - Cadastrar nova peça")
    print("2 - Listar peças aprovadas/reprovadas")
    print("3 - Remover peça cadastrada")
    print("4 - Listar caixas fechadas")
    print("5 - Gerar relatório final")
    print("0 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_peca()
    elif opcao == "2":
        listar_pecas()
    elif opcao == "3":
        remover_peca()
    elif opcao == "4":
        listar_caixas_fechadas()
    elif opcao == "5":
        gerar_relatorio_final()
    elif opcao == "0":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida. Tente novamente.")
