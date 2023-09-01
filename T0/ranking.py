
def ordenar(user_and_points):
    primer = -1
    if user_and_points != "\n":
        user_and_points = user_and_points.split("->")

        primer = int(user_and_points[1])

    return primer

def ordenar_rank():
    open_txt = open("rankings/puntajes.txt", "r")
    rank = open_txt.readlines()
    open_txt.close()
    rank.sort(reverse=True, key=ordenar)
    return rank

def actualizar_rank(jugador):
    open_txt = open("rankings/puntajes.txt", "r")
    rank = open_txt.readlines()
    open_txt.close()
    anadir = str(jugador.user_name) + "-> " + str(jugador.user_points)

    esta= False


    for i in range(0,len(rank)):
        if "->" in rank[i]:
            minilista = rank[i].split("->")
            if minilista[0] == str(jugador.user_name):
                esta = True
                rank[i] = anadir


    if esta == False:

        rank.append(anadir)

    rank.sort(key=ordenar)
    with open('rankings/puntajes.txt', 'w') as f:
        for elem in rank:
            if "->" in elem:
                print(elem, file=f)

def imprimir_ranks():
    rank = ordenar_rank()
    posicion = 1


    while posicion < 11:
        texto = str(posicion) + " " + rank[posicion-1]
        posicion += 1
        print(texto)