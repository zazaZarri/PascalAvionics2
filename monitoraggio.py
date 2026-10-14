def filtra_controlli_non_validi(lista_aeromobili):
    return [a for a in lista_aeromobili if not a["controlli_ok"]]

def filtra_oltre_soglia(lista_aeromobili, soglia):
    return [a for a in lista_aeromobili if a["ore_volo"] > soglia]


    