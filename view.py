import model
import controller

def main():
    jogo = controller.iniciar_jogo()
    while True:
        opcao = input()
        valores = opcao.split(" ")
        match valores[0]:
            case "RJ":
                if controller.registar_jogador(jogo, valores[1]):
                    print("Jogador registado com sucesso.")
                else:
                    print("Jogador existente.")
            case "LJ":
                tabela_jogadores = controller.listar_jogadores(jogo)
                if tabela_jogadores != False:
                    for i in range(0,len(tabela_jogadores)):
                        print(tabela_jogadores[i][0], ' '.join(map(str,tabela_jogadores[i][1].values())))
                else:
                    print("Sem jogadores registados.")
            case "IJ":
                if model.controlador_jogo:
                    print("Existe um jogo em curso.")
                else:
                    jogadores_existentes = jogo["tabela_resultados"].keys()
                    if valores[1] in jogadores_existentes and valores[2] in jogadores_existentes:
                        if controller.iniciar_jogo(jogo, valores[1],valores[2]):
                            print("Jogo iniciado com sucesso.")
                    else:
                        print("Jogador inexistente.")
            case '':
                break
            case default:
                print("Instrução inválida.")