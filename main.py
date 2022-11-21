import time
import os
import webbrowser
bot = ["Ver os ChatBots prontos","Adicionar suas informações no ChatBot","Sair do ChatBot"]

perguntas = ["ChatBot do Alan","Para você como é estudar no IFAL?","Qual curso você faz?","tem instagram?","O que você aprende no seu curso?","Voltar ao menu do ChatBot?"]

user = ["Alan"]

Alan = ["na maioria do tempo é super cansativo, mas, é muito gratificante quando se consegue fazer algo que nunca pensou em fazer, como seu próprio jogo da cobrinha ou um site, por exemplo.", "Eu curso o Ensino Médio com Técnico integrado para Desenvolvimento de Sistemas", "@alan_santos_360","no curso é ensinado Programação de diferentes especialidades, como: Programação web, Programação Orientada a Objetos, etc."]

print("Oi, eu sou seu ChatBot, escolha entre as opções")

#def para printar a tabela
def tabela(lista,y):
    chave = 0
    p = 0
    for x in (lista):
      if len(lista[p]) > chave:
        chave = len(lista[p]) 
      p += 1
    for p,z in enumerate(lista):
      espaco = chave - len(lista[p])
      print(f'| %d | %s'%(p+y,z),espaco * " ","|")

#def para printar a opção escolhida
def opções(opc,chave,resposta):
    if opc == chave:
      print(resposta)
ChatBot = True
inicio = True


def erro(opc):
  if opc != "1" and opc != "2" and opc != "3":
    print("Insira uma das opções validas.")
    inicio == True
    break

while ChatBot == True:
    if inicio == True:
      #chama o def da linha 15
      tabela(bot,1)
      opc1 = input('R: ')
      inicio = False
      #caso o usuário digite 2 ele irá fazer um novo ChatBot
      erro(opc1)
      if opc1 == "2" :
        user_perguntas = []
        user_respostas = []
        nome = input("digite seu nome: ")
        user.append(nome)
        user_perguntas.append(f"ChatBot de {nome}")
        num_perguntas  = int(input("digite o numero de perguntas que você vai fazer seu bot\nR: "))
        cont = 0
        #faz a introdução das perguntas e das respostas
        while cont < num_perguntas:
          perguntas_bot = input("digite as perguntas que você quer que o seu bot faça\nR: ")          
          user_perguntas.append(perguntas_bot)
          respostas_bot = input("digite as respostas que o seu bot irá responder ao usário!\nR: ")
          user_respostas.append(respostas_bot)
          cont += 1
        user_perguntas.append("Voltar ao menu do ChatBot? ")    
        inicio = True 
        #caso o usuário digite 1 ela irá aparecer os bots prontos
      elif opc1 == "1":
        tabela(user,1)
        usuario = input("R: ")
        
        # chama o bot padrão
        if usuario == "1":
          while True:
            tabela(perguntas,0)
            opc2=int(input('R: ')) 
            opções(opc2,1,Alan[0])
            opções(opc2,2,Alan[1])
            opções(opc2,4,Alan[3])
            if opc2 == 5 :
              inicio = True
              break
            elif opc2 == "3":
              webbrowser.open("https://www.instagram.com/alan_santos_360/?hl=pt")
        #chama o bot criado pelo usuário
        elif usuario == "2":
          while True:
            #deixando o titulo simetrico de acordo com a variavél
            tabela(user_perguntas,0)
            opc2 = int(input("R: "))
            indice = 0
            chave = len(user_perguntas) - 2
            while indice < chave:
              opções(opc2,indice+1,user_respostas[indice])
              indice+=1
            if opc2 + 1 == len(user_perguntas):
              inicio = True
              break
      elif opc1 == 3:
        print("========= Finalizando chatbot =========")
        exit()