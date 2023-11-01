

def possible_sec_draw(T, expected, i, j):
    all_horizontal_max = 0
    all_vertical_max = 0
    all_vertical_max = all_vertical(T, i, j)[1]
    all_horizontal_max = all_horizontal(T, i, j)[1]

   
    if(expected <= all_horizontal_max or expected <= all_vertical_max): return True
    
    
    return False

def all_vertical(T, indexI, indexJ):
    current_max = 0
    j = indexJ
    if(T[indexI][indexJ] != '.'):
        return (T, current_max)
    tmp = T
    for i in range(indexI, len(T)):
        if(T[i][j] == '.'): 
            tmp[i][j] = '?'
            current_max+=1
        else: return (tmp, current_max)
    return (tmp, current_max)

def all_horizontal(T, indexI, indexJ):
    current_max = 0
    i = indexI
    tmp = T
    
    if(T[indexI][indexJ] != '.' ):
        return (T, current_max)
    for j in range(indexJ, len(T[i])):
        if(T[i][j] == '.'): 
            tmp[i][j] = '?'
            current_max+=1
        else:
            if(T[i][j] == '?'): current_max -= 1
            
            return (tmp, current_max)
    return (tmp, current_max)

def clear_tab(T):
    for i in range(0, len(T)):
        for j in range(0, len(T)): 
            if(T[i][j] == '?'): T[i][j] = '.'
    return T

def print_tab(T):
    for i in T:
        print(i, end='\n')

T = [
    ['.', '.', 'X', '.'],
    ['.', '.', '.', '.'],
    ['X', 'X', 'X', '.'],
    ['X', '.', 'X', '.']
]

Tab = [
    ['.', '.', 'X', '.'],
    ['.', '.', '.', '.'],
    ['X', 'X', 'X', '.'],
    ['X', '.', 'X', '.']
]


            

        

Tmp_hor, tmp_max_hor = all_horizontal(Tab, 0, 0)
Tab = clear_tab(Tab)
print(Tmp_hor)