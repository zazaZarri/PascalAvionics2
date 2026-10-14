aeromobili = [
    {"codice": "I-ABC", "modello": "A320", "ore_volo": 1240, "controlli_ok": True},
    {"codice": "I-XYZ", "modello": "B737", "ore_volo": 850, "controlli_ok": False},
    {"codice": "I-TEST", "modello": "ATR72", "ore_volo": 1100, "controlli_ok": False},
    {"codice": "I-DEMO", "modello": "A350", "ore_volo": 450, "controlli_ok": True}
]

def stampa_riepilogo(lista_aeromobili):
    if not lista_aeromobili:
        print("lista vuota")
        return
    
    for a in lista_aeromobili:
        print(f"- Codice: {a['codice']} | Modello: {a['modello']} | Ore: {a['ore_volo']}")
        
        
def filtra_controlli_non_validi(lista_aeromobili):
    return [a for a in lista_aeromobili if not a["controlli_ok"]]
  
def filtra_oltre_soglia(lista_aeromobili, soglia):
    return [a for a in lista_aeromobili if a["ore_volo"] > soglia]
