def get_max_people(N, E, S):
    
    max_people = []

    if not E or not S:
        return 0
    
    if not 1 <= N <= 100:
        return 0

    for i in range(N):
        entry_1 = E[i]               # nesta linha, vamos pegar o índice 0 da lista E
        exit_1 = S[i]                # e aqui, vamos pegar também o índice 0 mas dessa vez, da lista S, e como resultado dos dois índices, a saída será (1,9)
        people_in_room = 1           # nesta linha, captamos a quantidade inicial de pessoas na sala

        for j in range(i+1, N):      # i+1 = evita a repetição do elemento (neste caso, o horário) anterior 
            entry_2 = E[j]

            if entry_1 < entry_2 < exit_1:
                people_in_room += 1  # Equivale a people_in_room = people_in_room + 1

        max_people.append(people_in_room)
    
    return max(max_people)

# Se necessário, os valores abaixo podem ser alterados
N = 3
E = [1, 5, 7]
S = [9, 13, 12]

print(get_max_people(N, E, S))


