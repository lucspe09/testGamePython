import random

posiblesRazas = ("orco","humano","elfo")

orco = {
    "raza": posiblesRazas[0],
    "fuerza" : random.randint(50,70),
    "vida" : 110,
    "agilidad" : 20,
    "magia" : 10
}

humano = {
    "raza":posiblesRazas[1],
    "fuerza" : random.randint(40,60),
    "vida" : 70,
    "agilidad" : 50,
    "magia" : 30
}

elfo = {
    "raza":posiblesRazas[2],
    "fuerza" : random.randint(35,45),
    "vida" : 80,
    "agilidad" : 100,
    "magia" : 60
}

def attackfisica(P1,P2):
    resultdoattack = P1["vida"]-P2["fuerza"]
    P1["vida"] = resultdoattack
    print(P1,P2)
    checkLife()
    
def contrattackf(P1,P2):
    resultadocontr = (P1["vida"]-P2["fuerza"])
    P1["vida"] = resultadocontr
    print(P1,P2)
    checkLife()

def attackM(P1,P2):
    resultadoattackM = (P2["vida"]-P1["magia"])
    P2["vida"] = resultadoattackM
    print(P1,P2)
    checkLife()

def checkLife():
    if orco["vida"] <= 0:
        print("orco murio")
    elif elfo ["vida"] <= 0:
        print("elfo murio")
    elif humano["vida"] <= 0:
        print("humano murio")


attackfisica(elfo, humano)
contrattackf(humano,elfo)
attackM(humano,elfo)
