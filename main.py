import itertools

def calculate_all_perms(T, perms):

    #['.', '.', 'X', '.'],
    #['.', '.', 'X', '.'],
    #['.', 'X', 'X', '.'],
    #['X', '.', 'X', '.']

    if(len(perms) == 0): return True
    else:
        if perms[0][0] == perms[0][1]:
            calculate_all_perms(T, perms.pop(0))
                
        
    return None

def all_horizontal(T, indexI, indexJ):
    current_max = 0
    i = indexI
    beginI = indexI
    beginJ = indexJ
    if(T[indexI][indexJ] == 'X'): return False
    for j in range(indexJ, len(T[i])):
        if(T[i][j] == '.'): current_max+=1
        else: return (current_max, beginI, beginJ, i, j)
    return (current_max, beginI, beginJ, i, j)


def group_(T):
    verts = T[0]
    hor = T[1]
    maps = {}
    for i in verts:
        if i[0] not in maps:
            maps[i[0]]=[i]
        else: maps[i[0]].append(i)
    for i in hor:
        if i[0] not in maps:
            maps[i[0]]=[i]
        else: maps[i[0]].append(i)
    return dict(sorted(maps.items(), reverse=True))

def all_vertical(T, indexI, indexJ):
    current_max = 0
    beginI = indexI
    beginJ = indexJ
    j = indexJ
    if(T[indexI][indexJ] == 'X'): return False
    for i in range(indexI, len(T)):
        if(T[i][j] == '.'): current_max+=1
        else: return (current_max, beginI, beginJ, i, j)
    return (current_max, beginI, beginJ, i, j)

def all_versions(T):
    all_vertical_ = []
    all_horizontal_ = []
    for i in range(0, len(T)):
        for j in range(0, len(T[i])):
            ver_tmp = all_vertical(T, i, j)
            hor_tmp = all_horizontal(T, i, j)
            
            if(type(ver_tmp)!= bool):   
                all_vertical_.append(ver_tmp)
            if(type(hor_tmp)!= bool):
                all_horizontal_.append(hor_tmp)
    return all_vertical_, all_horizontal_

def generate_permutations(arr, length):
    permutations = list(itertools.product(arr, repeat=length))
    return permutations

def create_perms(grouped, length):
    new_with_perms = {}
    for i in grouped:
        if(length == 1):
            return grouped[i]
       
        if(len(grouped[i]) > 1 and length <= len(grouped[i])):
            permutations = generate_permutations(grouped[i], length)
            new_with_perms[i] = permutations

    return new_with_perms

#pogrupuj to w grupy literowe -> w nich zrob wszystkie permutacje -> sprawdzaj od najwiekszych czy mozliwe jest takie ustawienie


T = [
    ['.', '.', 'X', '.'],
    ['.', '.', 'X', '.'],
    ['.', 'X', 'X', '.'],
    ['X', '.', 'X', '.']
]

grouped = group_(all_versions(T))
create_perms = create_perms(grouped, 2)
for i in create_perms:
    print(create_perms[i]) 
