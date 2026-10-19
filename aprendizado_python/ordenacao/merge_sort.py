def merge_sort(lista: list) -> None:
    
    """
    Ordena uma lista de inteiros em ordem crescente utilizando o algoritmo Merge Sort.
    
    Complexidade de Tempo: O(n log n) em todos os casos (melhor, pior e médio).
    Complexidade de Espaço: O(n) devido às sublistas criadas na memória.
    """
    
    if len(lista) <= 1:
        return
    
    meio = len(lista) // 2
    left = lista[:meio]
    right = lista[meio:]
    
    merge_sort(left)
    merge_sort(right)
    
    i, j, k = 0, 0, 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            lista[k] = left[i]
            i += 1
        else:
            lista[k] = right[j]
            j += 1
        k += 1
        
    while i < len(left):
        lista[k] = left[i]
        i += 1
        k += 1
       
    while j < len(right):
        lista[k] = right[j]
        j += 1
        k += 1

def main():
    while True:
        
        try:
            print('Digite os valores, para ordena-los de forma crescente: ')
            lista = list(map(int, input().split()))
            print(f'Lista original = {lista}')
            merge_sort(lista)
            print(f'Lista ordenada = {lista}')
            break
        
        except ValueError:
            print('Digite apenas números inteiros!')
        
if __name__ == '__main__':
    main()
    