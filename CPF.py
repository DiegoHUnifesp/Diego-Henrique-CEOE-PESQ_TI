import random

def geraCPF():
    #Gera uma lista e armezena 9 numeros aleatorios nessa lista
    listaCPF = [random.randrange(10) for i in range(9)]
    
    #Processamento logico para gerar o primeiro digito validador
    soma1 = sum(i * j for i, j in zip(listaCPF, range(10, 1, -1)))
    digito1 = 11 - (soma1 % 11)
    if digito1 >= 10:
        digito1 = 0
    listaCPF.append(digito1)
    
    #Processamento logico para gerar o segundo digito validador
    soma2 = sum(i * j for i, j in zip(listaCPF, range(11, 1, -1))) 
    digito2 = 11 - (soma2 % 11)
    if digito2 >= 10:
        digito2 = 0
    listaCPF.append(digito2)
    
    #Transforma a lista em uma string e exibe o cpf separado por ponto e traço
    cpfStr = "".join(map(str, listaCPF))
    return cpfStr[:3] + '.' + cpfStr[3:6] + '.' + cpfStr[6:9] + '-' + cpfStr[9:] 


def checaCPF(strCPF):
    listaCPFuse = []
    cpfUser = str(strCPF)
    valido = True
    
    #verifica se o cpf tem 11 ou 14 caracteres
    if len(cpfUser) == 11 or len(cpfUser) == 14:
           
        #ignora os pontos e virgulas, e retorna falso caso aja letras
        for car in cpfUser:
            if car != '.' and car!= '-':
                if car not in '0123456789':
                    print("Cpf invalido")
                    valido = False
                    break    
                listaCPFuse.append(car)
            
        #caso nao tenha letras começa o processamento logico
        if valido and len(listaCPFuse) == 11:            
            listaCPFint = list(map(int, listaCPFuse))
            digValidos1 = True
            digValidos2 = True
            
            #gera um numero verificador com base nos valores passados pelo usario, e caso o digito verificador gerado seja igual do usario, True
            somaUser1 = sum(u * i for u, i in zip(listaCPFint, range(10, 1, -1)))
            digitoUser1 = 11 - (somaUser1 % 11)
            if digitoUser1 >= 10:
                digitoUser1 = 0
            if listaCPFint[9] != digitoUser1:
                digValidos1 = False
                
            else:
                digValidos1 = True
            
            # mesma coisa mas para o segundo digito verificador
            somaUser2 = sum(u * i for u, i in zip(listaCPFint, range(11, 1, -1)))
            digitoUser2 = 11 - (somaUser2 % 11)
            if digitoUser2 >= 10:
                digitoUser2 = 0
            if listaCPFint[10] != digitoUser2:
                digValidos2 = False
                
            else:
                digValidos2 = True
            
            # se tiver tudo certo, exibe o cpf
            if digValidos1 == False or digValidos2 == False:
                return False
            
            else:
                return True
            
        else:
            return False
        
    else:
        return False
