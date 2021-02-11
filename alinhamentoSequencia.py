seq1 = ['G','A','A','T','T','C','A','G','T','T','A']
seq2 = ['G','G','A','T','C','G','A']

matriz = [[' ','-','G','A','A','T','T','C','A','G','T','T','A'],
          ['-','0','0','0','0','0','0','0','0','0','0','0','0'],
          ['G','0',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
          ['G','0',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
          ['A','0',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
          ['T','0',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
          ['C','0',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
          ['G','0',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
          ['A','0',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']]


def preencherMatriz():  + escore, M[i][j-1] + W, M[i-1][j] + W , 0]<<<<<? dividi eles em variaveis em q 'M[i-1][j-1] + escore' é MF1, ' M[i][j-1] + W' é MF2 e assim por diante
    MF1 = 0 
    MF2 = 0 
    MF3 = 0 
    
    for i in range(2,9):
        for j in range (2,13): 
                                                                                           
            MF1 = int(matriz[i-1][j-1]) + escore(seq1[j-2], seq2[i-2])  
            MF2 = int(matriz[i][j-1]) - 4 
            MF3 = int(matriz[i-1][j]) - 4 

  
            if 0 > MF1 and 0 > MF2 and 0 >MF3: 
                matriz[i][j] = '0'
            elif MF1 > MF2 and MF1 > MF3:   
                matriz[i][j] = str(MF1)
            elif MF2> MF1 and MF2 > MF3:     
                matriz[i][j] = str(MF2)
            elif MF3> MF1 and MF3> MF2:     
                matriz[i][j] = str(MF3) 
            elif MF1 == MF2 and MF2 > MF3: 
                matriz[i][j] = str(MF2)
            elif MF1 == MF3 and MF3 > MF2:
                matriz[i][j] = str(MF1)
            elif MF2 == MF3 and MF2 > MF1:
                matriz[i][j] = str(MF2)
            elif MF2 == MF3 and MF1 == MF3 and MF1 == MF2:
                matriz[i][j] = str(MF2)
                
            

                
def backtracking(a):
    aux = 0 
    lista_alinhada1 = [] 
    lista_alinhada2 = [] 
    caminho = ''  
    for i in range(2,9):
            for j in range (2,13): 
                if aux <= int(matriz[i][j]): 
                    aux = int(matriz[i][j])
                    inicio_linha = i 
                    inicio_coluna = j

    
    lista_alinhada1.append(matriz[0][inicio_coluna]) 
    lista_alinhada2.append(matriz[inicio_linha][0])
    caminho = str(aux)
    
                
    while matriz[inicio_linha - 1][inicio_coluna - 1] != '0':   
        caminho = caminho + ' --> ' + matriz[inicio_linha - 1][inicio_coluna - 1] 
        
        if matriz[0][inicio_coluna-1] == matriz[inicio_linha-1][0]: 
            lista_alinhada1.append(matriz[0][inicio_coluna-1])
            lista_alinhada2.append(matriz[inicio_linha-1][0])
            
            inicio_linha -= 1
            inicio_coluna -= 1
                
        elif matriz[0][inicio_coluna-1] == matriz[inicio_linha][0]: 
            
            lista_alinhada1.append('-')
            lista_alinhada2.append(matriz[0][inicio_coluna-1])
              
            inicio_coluna -= 1
            
        else:
            lista_alinhada1.append(matriz[inicio_linha-1][0]) 
            lista_alinhada2.append('-')
                  
            inicio_linha -= 1
       
    print('\n')
    print(lista_alinhada1)
    print(lista_alinhada2) 
    print(caminho) 
    print('\n')


def escore(a, b): 
    if a == b:              
        return 5
    elif a == '-' or b == '-': 
        return -4
    else:                  
        return -3
    
            
for i in range(4):
    seq2.append('-')

preencherMatriz()

backtracking(matriz)

print(matriz[0]) 
print(matriz[1])
print(matriz[2])
print(matriz[3])
print(matriz[4])
print(matriz[5])
print(matriz[6])
print(matriz[7])
print(matriz[8])
