import matplotlib.pyplot
from math import sqrt
from time import sleep


def grafico1(xrobo,yrobo,xbola,ybola):

    #Gráfico das trajetórias da bola e do robô em um plano 𝑥𝑦, até o ponto de interceptação
    matplotlib.pyplot.plot(xrobo, yrobo, label='robô') 
    matplotlib.pyplot.plot(xbola,ybola, label='bola')
    matplotlib.pyplot.title('Movimentação Bola-Robô até o ponto de interceptação\nTrajetória dentro do campo')
    matplotlib.pyplot.legend()
    matplotlib.pyplot.show()


def grafico2(xrobo,xbola,trobo,tbola,yrobo,ybola):

    #Gráfico das coordenadas 𝑥 e 𝑦 da posição da bola e do robô em função do tempo 𝑡 até o instante de interceptação;

    matplotlib.pyplot.plot(trobo, xrobo , label='x robô' )
    matplotlib.pyplot.plot(tbola, xbola , label='x bola' )
    matplotlib.pyplot.plot(trobo, yrobo, label='y robô')
    matplotlib.pyplot.plot(tbola, ybola, label='y bola')

    matplotlib.pyplot.ylabel('Posição')
    matplotlib.pyplot.xlabel('Tempo')
    matplotlib.pyplot.title('Posições X e Y , do Robô e Bola, em função do tempo')

    matplotlib.pyplot.legend()
    matplotlib.pyplot.show()

def grafico3(vxbola, tbola, vybola, vxrobo, trobo, trobovely, vyrobo):
    
    
    #componentes da velocidade x e y do robô e da bola
    
    matplotlib.pyplot.plot(tbola, vxbola , label='Vx bola' )
    matplotlib.pyplot.plot(tbola, vybola, label='Vy bola')
    matplotlib.pyplot.plot(trobo, vxrobo , label='Vx robô' )
    matplotlib.pyplot.plot(trobovely, vyrobo, label='Vy robô')
    
    matplotlib.pyplot.ylabel('Velocidade')
    matplotlib.pyplot.xlabel('Tempo')
    matplotlib.pyplot.title('Velocidades X e Y , do Robô e Bola, em função do tempo')

    matplotlib.pyplot.legend()
    matplotlib.pyplot.show()


def grafico4(axbola,axrobo,aybola,ayrobo,tempo):

    #componentes da aceleração x e y do robô e da bola
    matplotlib.pyplot.plot(tempo, axrobo , label='ax robô' )
    matplotlib.pyplot.plot(tempo, axbola , label='ax bola' )
    matplotlib.pyplot.plot(tempo, ayrobo, label='ay robô')
    matplotlib.pyplot.plot(tempo, aybola, label='ay bola')

    matplotlib.pyplot.ylabel('Aceleração')
    matplotlib.pyplot.xlabel('Tempo')
    matplotlib.pyplot.title('Acelerações X e Y , do Robô e Bola, em função do tempo')

    matplotlib.pyplot.legend()
    matplotlib.pyplot.show()

def grafico5(dist, t):

    #distância relativa em função do tempo
    matplotlib.pyplot.plot(t, dist)

    matplotlib.pyplot.ylabel('Distância')
    matplotlib.pyplot.xlabel('Tempo')
    matplotlib.pyplot.title('Distância relativa, entre o Robô e a Bola, em função do tempo')

    matplotlib.pyplot.show()







def main():
    print(" ________________________")
    print("|Centro Universitário FEI|")
    print("|   PROJETO ORA BOLAS    |")
    print("|________________________|")
    print("|Gabriel Lopez Vendramini|")
    print("|   22.121.015-6         |")
    print("|Juan Lira Estevão       |")
    print("|   22.121.033-9         |")
    print("|Lorena Cardoso Sanches  |")
    print("|   22.121.060-2         |")
    print("|________________________|")

    sleep(2)
    print("AJUDE ROBERT, O ROBÔ, A FAZER O GOL!")
    sleep(1)
    print("Onde ele está no campo?")
    sleep(1)
    x_inicial = float(input("Digite a posição inicial do robô em x: "))
    y_inicial = float(input("Digite a posição inicial do robô em y: "))

    #______________
    #Trajetória da bola: abrindo os dados
    dados_x=[]
    dados_y=[]

    arqx = open("./dados/x.txt","r")
    arqy = open("./dados/y.txt","r")

    leitorx = arqx.readlines()
    leitory = arqy.readlines()
    
  


    for x in range(len(leitorx)):
        numx = leitorx[x]
        numx = numx.replace(',','.')
        numx = float(numx)
        dados_x.append(numx)

        numy = leitory[x]
        numy = numy.replace(',','.')
        numy = float(numy)

        dados_y.append(numy)

    #fim da abertura dos dados
    #______________
    i = 0
    a = 2.8
    deltat = [0]
    r = 0.03
    #___________________________________________________________
    #o que acontece se o raio de interceptação for reduzido
    #rodando o código na posição (1,1), temos

    # COM RAIO ORIGINAL (3CM)
    # robô encontra a bola em (4.930 ; 3.070)
    # robô precisa de 1.775s e a bola 1.780s

    # COM RAIO REDUZIDO PELA METADE (1,5CM)
    # robô encontra a bola em (4.930 ; 3.070)
    # robô precisa de 1.778s e a bola 1.780s
    # Ou seja, o robô consegue encontrar a bola no mesmo ponto
    # que conseguiria com r = 3cm, mas ele demora um pouquinho mais 
    # Pra chegar lá


    # SEM RAIO
    # robô encontra a bola em (4.967 ; 3.092)
    # robô preciso de 1.790 s e a bola de 1.800 s

    # CONCLUSÃO
    # O raio de intercep é como se a bola inflasse alguns centímetros
    # E por isso a distância entre o robô e a bola diminui levemente
    # Fazendo com que, quanto maior o raio, menor o tempo
    # Por isso demora alguns milisegundos a mais sem ele
    #______________________________________________________________


    #para o gráfico da posição
    # 4 variáveis que vão guardar o delta s até a interceptação 
    mov_x_robo = [x_inicial]
    mov_y_robo = [y_inicial]
    esp_x_robo =  [x_inicial] 
    esp_y_robo =  [y_inicial]
    esp_x_bola = []
    esp_y_bola = []

    # listas que guardam o tempo até o ponto de interceptação
    t_bola_intercep = []
    t_robo_intercep = [0]
    t_robo_vel = [0]
    t_robo_vely = [0]

    # listas que guardam a velocidade até a interceptação
    v_x_bola = []
    v_y_bola = []
    v_x_robo = [0]
    v_y_robo = [0]

    #listas que guardam a aceleração até a intercep
    a_x_bola = []
    a_y_bola = []
    a_x_robo = []
    a_y_robo = []

    #distancia relativa
    dist_rel = []


    #LEITURA DOS DADOS PARA VERIFICAR O PRIMEIRO PONTO ONDE O ROBÔ CHEGA ANTES DA BOLA
    while i<=len(dados_x):
        pos_bola_x = dados_x[i]
        pos_bola_y = dados_y[i]
        t_bola = i*(0.02) #tempo para a bola chegar a essa posição

        #distancia entre o robô e o ponto onde a bola está
        dist_pontos = sqrt(((pos_bola_x-x_inicial)**2)+((pos_bola_y-y_inicial)**2))-r
        
        #muv
        t_robo = sqrt((2*dist_pontos)/a)

        #guardando posições e tempo até o encontro
        esp_x_bola.append(pos_bola_x)
        esp_y_bola.append(pos_bola_y)
        t_bola_intercep.append(t_bola) 


        #VELOCIDADE DA BOLA

        vxbola = (-0.52)*t_bola + 2.91
        v_x_bola.append(vxbola)

        vybola = (-0.4)*t_bola +1.8
        v_y_bola.append(vybola)


       
        

        if(t_robo<t_bola): #no primeiro momento onde o robo chega antes da bola

            deltat.append(t_robo)

            #POSIÇÕES
            pos_robo_x = x_inicial + (a*((0.5*t_robo)**2))/2
            esp_x_robo.append(pos_robo_x)

            pos_robo_y = y_inicial + (a*((0.5*t_robo)**2))/2
            esp_y_robo.append(pos_robo_y)

            t_robo_intercep.append(0.5*(t_robo))

            esp_x_robo.append(dados_x[i]) #guardando a coordenada do robo no encontro
            esp_y_robo.append(dados_y[i])     
            t_robo_intercep.append(t_robo) #guardando t final do robô   
            mov_x_robo.append(dados_x[i])
            mov_y_robo.append(dados_y[i])


            #DISTANCIA RELATIVA
            dist_inicial = sqrt(((x_inicial-1)**2)+((y_inicial-0.5)**2))
            dist_rel.append(dist_inicial)
            dist_rel.append(r) # A dist final é o raio de intercep
            tempodist = [0,t_robo]
          
            #________________________________

            #VELOCIDADE DO ROBÔ
            vxfrobo = (esp_x_robo[2]-esp_x_robo[1])/(0.5*t_robo)
            vyfrobo = (esp_y_robo[2]-esp_y_robo[1])/(0.5*t_robo)


            #para o caso da velocidade passar do 3
            if vxfrobo>a/2:
              t_robo_vel.append(1)
              t_robo_vel.append(t_robo)
              v_x_robo.append(a)
              v_x_robo.append(a)
              v_y_robo.append(vyfrobo-0.000001) 
              v_y_robo.append(vyfrobo)          
              t_robo_vely.append(t_robo-0.00001)
              t_robo_vely.append(t_robo)

            else:
              t_robo_vel.append(t_robo)
              v_x_robo.append(vxfrobo)
              v_y_robo.append(vyfrobo)
              t_robo_vely.append(t_robo) 

            #ACELERAÇÃO DO ROBÔ
            axrobo = v_x_robo[1]/t_robo
            ayrobo = v_y_robo[1]/t_robo

            a_x_robo.append(axrobo)
            a_x_robo.append(axrobo)
            a_y_robo.append(ayrobo)
            a_y_robo.append(ayrobo)

            #ACELERAÇÃO DA BOLA
            a_x_bola.append(-0.52)
            a_x_bola.append(-0.52)
            a_y_bola.append(-0.4) 
            a_y_bola.append(-0.4)   

            #Aprofundamento informações dinamica e cinematica
            
            Vel_m_bola = vxbola + vybola
    
            Vel_m_robo = vxfrobo + vyfrobo

            # a velocidade desejada do robô é 2.8 
            
            ac_m_bola = (Vel_m_bola / t_bola)*-1

            ac_m_robo = 2.8
            
            if (Vel_m_robo > 2.8):
              Vel_m_robo = 2.8
            
    
            
          

            print("___________________\n- GOLAÇO!\n")
            print("O robô encontra a posição da bola nos pontos")
            print("x: %.3f"%dados_x[i])
            print("y: %.3f"%dados_y[i])
            print("___________________")

            sleep(4)

            print("- TEMPO NECESSÁRIO\n")
            print("Robert precisou de %.3f segundos para chegar até a bola, acertando um belo chute. Sem chance para o goleiro!"%t_robo)
            print("___________________")

            sleep(6)

            print("- INFORMAÇÕES ADICIONAIS\n")
            print("O robô se encontra a %.2f metro(s) da bola no início."%dist_inicial)
            print("O robô precisou de %.3f segundos para chegar na posição futura da bola."%t_robo)
            print("Enquanto a bola precisou de %.3f segundos."%t_bola)
            print("velocidade Média do robô: %.2f m/s."%Vel_m_robo)
            print("velocidade Média da bola: %.2f m/s."%Vel_m_bola)
            print("aceleração Média do robô: %.2f m/s."%ac_m_robo)
            print("aceleração Média do bola: %.2f m/s."%ac_m_bola)
            print("___________________")

            sleep(10)


            break
        else: 
            i+=1
    print("__________________________________________________")
    print("O QUE DESEJA FAZER?")

    print("1. Exibir gráfico da trajetória da bola e do robô no campo, até o ponto de encontro\n")

    print("2. Exibir gráfico das coordenadas x e y (bola e robô) até o ponto de encontro\n")

    print("3. Exibir gráfico das velocidades x e y (bola e robô) até o ponto de encontro\n")

    print("4. Exibir gráfico das acelerações x e y (bola e robô) até o ponto de encontro\n")

    print("5. Exibir gráfico da distância relativa entre o robô e a bola em função do tempo\n")

    print("0. Voltar ao início")
    print("__________________________________________________")
    sleep(1)

    while(True):

        escolha = int(input("Digite a opção desejada: "))

        if(escolha==1):
            print("OBS: Para ver outro gráfico, feche o gráfico atual")            
            grafico1(mov_x_robo , mov_y_robo ,esp_x_bola , esp_y_bola)
            
        

        elif(escolha==2):
            print("OBS: Para ver outro gráfico, feche o gráfico atual") 
            grafico2(esp_x_robo , esp_x_bola , t_robo_intercep , t_bola_intercep, esp_y_robo, esp_y_bola)
            
        elif(escolha==3):
            print("OBS: Para ver outro gráfico, feche o gráfico atual") 
            grafico3(v_x_bola, t_bola_intercep ,v_y_bola, v_x_robo, t_robo_vel, t_robo_vely, v_y_robo)


        elif(escolha==4):
            print("OBS: Para ver outro gráfico, feche o gráfico atual") 
            grafico4(a_x_bola, a_x_robo, a_y_bola, a_y_robo, deltat)


        elif(escolha==5):
            print("OBS: Para ver outro gráfico, feche o gráfico atual") 
            grafico5(dist_rel, tempodist)

        elif(escolha==0):
            main()
        
        else:
            print("Valor inválido! Digite um valor entre 0 e 5")
        
        

main()