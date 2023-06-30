import model

def iniciar():
    jogo = {
        "tabela_resultados": {},
        "controlador_jogo": False,
        "jogadores_em_jogo": []
    }
    return jogo

def registar_jogador(jogo, player):
    if len(jogo["tabela_resultados"]) == 0:
        jogo["tabela_resultados"][player] = {"jogos":0, "vitorias":0, "empates":0, "derrotas":0}
        return True
    else:
        jogadores_existentes = jogo["tabela_resultados"].keys()
        if player in jogadores_existentes:
            return False
        else:
            jogo["tabela_resultados"][player] = {"jogos":0, "vitorias":0, "empates":0, "derrotas":0}
            return True

def listar_jogadores(jogo):
    if len(jogo["tabela_resultados"]) == 0:
        return False
    else:
        db_sorted = sorted(jogo["tabela_resultados"].items(), key=lambda row: (-row[1]["vitorias"], row[0]))
        return db_sorted

def iniciar_jogo(jogo, jogador_a,jogador_b):
    jogo["controlador_jogo"] = True
    jogo["tabela_resultados"][jogador_a]["jogos"] +=1
    jogo["tabela_resultados"][jogador_b]["jogos"] +=1
    jogo["jogadores_em_jogo"].append(jogador_a)
    jogo["jogadores_em_jogo"].append(jogador_b)
    return True