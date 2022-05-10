def computador_escolhe_jogada(n, m):

    global peçapc
    cont = 0
    x = 1
    
    
    if n <= m:
        
        print("O computador tirou" , n , "peça")
        peçapc = 0
        print("Fim do jogo! O computador ganhou!")
       
        
    else:
        
        if (n - x) % (m+1) != 0:

            while (n - x) % (m+1) != 0:
                x = x + 1
                
            peçapc = n - x
            print("O computador tirou" , x , "peça")
                        
            
        else:

            peçapc = n - 1
            print("O computador tirou" , 1 , "peça")
            
    return x
    
def usuario_escolhe_jogada(n, m):

    global peça
    peça = int(input("Quantas peças você vai tirar?: "))
    
    if peça <= m and peça > 0:
        
        print("Você tirou ", peça, "peças.")
    else:
        while peça > m or peça <= 0:
            print("Oops! Jogada inválida! Tente de novo.")
            peça = int(input("Quantas peças você vai tirar?: "))

        print("Você tirou ", peça, "peças.")
    return peça
            
def partida():

    

    n = int(input("Quantas peças: "))
    m = int(input("Limite de peças por jogada: "))
        
        
    if n % (m+1) == 0:
        print("Você começa!")

        while n > 0:
                        
            usuario_escolhe_jogada(n, m)
            n = n - peça
            
            if n == 0:
                print("Você venceu")

            print("Agora resta" , n, "no tabuleiro")         

            computador_escolhe_jogada(n, m)
            n = peçapc

            if n > 0:
                print("Agora resta" , n, "no tabuleiro")
            else:
                n = 0
                
    else:

        print("Computador começa!")

        while n > 0:
            computador_escolhe_jogada(n, m)
            n = peçapc

            if n > 0:
                print("Agora resta" , n, "no tabuleiro")
            else:
                n = 0
                break
            
            usuario_escolhe_jogada(n, m)
            n = n - peça
            
            if n == 0:
                print("Você venceu")

            print("Agora resta" , n, "no tabuleiro")

def campeonato():

    contador = 0
       
    print("Bem-vindo ao jogo do NIM! Escolha:")

    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato")

    escolha = int(input())

    if escolha == 2:
        print("Você escolheu um campeonato!")

        while contador < 3:
            contador = contador + 1
            print("**** Rodada", contador,"****")
            partida()
                       
            
        print("**** Final do campeonato! ****")
        print("Placar: Você 0 X 3 Computador")
    
    else:
        print("Você escolheu uma partida isolada!")
            
        partida()

campeonato()
    
