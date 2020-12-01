import random,time

#Respostas válidas
YES = ["sim", "s", "yes", "y", "oui", "claro", "sure", "biensur", "hai", "sm", "si"]
NO = ["não", "no", "nein", "nao", "non", "nope", "nunca", "n", "iee"]
YES_NO = YES + NO

def welcome():
    print("Você está pronto para criar um herói com o Gerador de Super Heróis 3000?")
    while True:
        answer = input()
        if answer.lower() in YES:
            print("Ótimo, vamos começar!\n")
            time.sleep(1)
            break
        elif answer.lower() in NO:
            answer2 = input("Você tem certeza?\n")
            if answer2.lower() in YES_NO:
                print("Sabia que você ia mudar de ideia. Vamos começar!\n")
                time.sleep(2)
                break
        else:
            print("Não entendi, tente novamente!")

def generate_name():
    print("Gerando nome... Aguarde um momento.\n")
    first_name = ["Le ", "The ","Hiper ","Super ","Capitão ","Capitã ", "Rabino "]
    last_name = ["Fréxi","Fruta","Pomba","Queijo","Franja","Nojo", "Koala", "Abelha", "Porta", "Náusea", "Leitinho", "Peixe"]
    hero_name = random.choice(first_name) + random.choice(last_name)
    return hero_name

def suspense():

    fills = ["Aposto que você não está aguentando o suspense", "Quase lá...", "Só mais um momento", "Vou preparar um café"]

    print("...........")
    time.sleep(4)
    print(random.choice(fills))
    time.sleep(3)
    print("...........")
    time.sleep(4)

def choose_name():
    like_hero = 'não'
    while like_hero in NO:
        name = generate_name()
        suspense()
        print("O nome do seu super herói é:", name)
        answer = input("Você gostou do nome?\n")
        if answer in YES:
            print("Ótimo \o/ vamos continuar!\n")
            like_hero = "sim"
            time.sleep(2)
            break
        elif answer in NO:
            print("Que pena =/ Vamos tentar de novo!\n")
            time.sleep(2)
        else:
            print("Não entendi o que você falou! Acho que você está bravo...")
            print("Vou gerar outro nome")
            time.sleep(3)

# Inspirações no site: https://powerlisting.fandom.com/wiki/List_of_Supernatural_Powers_and_Abilities
def powers_and_weaknesses():
    powers = ["Visão de Raio-X", "Cinto de Utilidades", "Super Velocidade", "Invisibilidade", "Conhecimentos em Programação", "Comunicação com os Animais", "Telepatia", "Autorregeneração"]
    weaknesses = ["Tímido", "Cego", "Fala demais", "Fedido", "Intolerante à lactose", "Umbigo sensível", "Surdo", "Manco", "Arrogante", "Gago"]
    return (random.choice(powers),random.choice(weaknesses))

def choose_powers():
    print("Agora é o momento que vamos gerar seus super poderes! Uhuuuullll")
    time.sleep(2)
    print("Gerando poderes...\n")
    pw = powers_and_weaknesses()
    suspense()
    print("\nO seu super poder é:", pw[0])
    time.sleep(2)
    print("E a sua fraqueza é:", pw[1])
    time.sleep(2)
    print("")
    input("Tudo bem até agora! Aperte ENTER para continuar")

def generate_stats():
    print("Agora só falta gerar os seus atributos")
    time.sleep(2)
    #Gerando as estatísticas do personagem
    strength = random.randint(1,100)
    intelligence = random.randint(1,100)
    endurance = random.randint(1,100)
    wisdom = random.randint(1,100)
    agility = random.randint(1,100)
    #Armazenando tudo em listas
    stats_name = ["Força","Inteligência","Resistência", "Sabedoria", "Agilidade"]
    stats_value = [strength, intelligence, endurance, wisdom, agility]
    #Criando um dicionário
    stats_dict = dict(zip(stats_name, stats_value))
    return stats_dict

def print_stats(stats_dict):
    print("Os atributos do seu personagem são:\n")
    #Loop que imprime status por status
    for k,v in stats_dict.items():
        sent = "{0} - {1}".format(k, v)
        print(sent)
        time.sleep(1)
    print("\n")

def comment_stats(stats_dict):
    #Respostas válidas
    answer=''
    #Loop de interrogação
    while answer not in YES_NO:
        print("Você quer que eu comente os seus atributos?")
        answer = input().lower()
        #Se a resposta for afirmativa comenta
        if answer in YES:
            print("YHAAAAAAAAAAAA! Aííí vaaaaiiii \o/ \n")
            time.sleep(2)
            for k, v in stats_dict.items():
                if v>=1 and v<20:
                    print("Nunca confie na sua {0} medíocre".format(k))
                    time.sleep(2)
                elif v>=20 and v<40:
                    print("{0} é baixa. Use-a só para meter o louco".format(k))
                    time.sleep(2)
                elif v>=40 and v<60:
                    print("{0} razoável. Só não abuse dos dados!".format(k))
                    time.sleep(2)
                elif v>=60 and v<80:
                    print("{0} boa. Sua party pode confiar em você".format(k))
                    time.sleep(2)
                elif v>=80 and v<=100:
                    print("{0} excelente! Fracasso só com roll 1".format(k))
                    time.sleep(2)
                else:
                    print("Você trapaceou na geração dos status, não é sabixão?")
            print()
            break
        #Se a resposta for negativa, não comenta
        if answer in NO:
            print("Snif, snif. Ok, eu nem queria mesmo...\n")
            time.sleep(2)
            break



def bye():
    print("=================================================")
    print("Obrigado por usar o gerador de Super-Heróis 3000")
    print("=================================================")
    time.sleep(2)
    print("Nos vemos em alguma mesa de RPG por aí! ;D")
    print("=================================================")
    time.sleeO(2)

#Programa principal
welcome()
choose_name()
choose_powers()
stats = generate_stats()
suspense()
print_stats(stats)
comment_stats(stats)
bye()