def merge_sort(lista:list) -> None:
    #Se a lista só possuir um item, já está oredenada
    if len(lista) <= 1:
        return
    
    #Cria a variavel meio que divide a lista original em duas
    meio = len(lista) // 2
    left = lista[:meio]
    right = lista[meio:]
    
    #Usa recursividade para ordenar os lados da lista
    merge_sort(left)
    merge_sort(right)
    
    #define a posição inicial para percorrer as listas novas
    i, j, k = 0, 0, 0
    
    #Enquanto houver lista para percorrer   
    while i < len(left) and j < len(right):

        if len(left[i]) >= len(right[j]):
            lista[k] = left[i]
            i += 1
        else:
            lista[k] = right[j]
            j += 1
        k += 1
    
    #Continua ordenando mesmo se a metade da direita acabar
    while i < len(left):
        lista[k] = left[i]
        i += 1
        k += 1
    
    #Continua ordenando mesmo se a metade da esquerda acabar
    while j < len(right):
        lista[k] = right[j]
        j += 1
        k += 1

def main():	
    casos = int(input())
    for _ in range(1, casos +1):
        lista = input().split()
        merge_sort(lista)
        print(" ".join(lista))

if __name__ == '__main__':
    main()