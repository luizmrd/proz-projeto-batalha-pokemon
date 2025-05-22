import random


print("===== INICIE SUA BATALHA ======")
print("===== ESCOLHA SEU POKEMON =====")
print(" 1 - Charmander")
print(" 2 - Squirtle")
print(" 3 - Bulbasaur")
print("===============================")

pokemonUsuario = int(input("Escolha seu Pokémon!"))

while True:
    if pokemonUsuario == 1:
        print("Você escolheu Charmander")
        break
    elif pokemonUsuario == 2:
        print("Você escolheu Squirtle")
        break
    elif pokemonUsuario == 3:
        print("Você escolheu Bulbasaur")
        break
    else:
        print("Pokémon invalido!!")
        break

Charmander = 1 
charmanderVida = 100
pokemonUsuario = charmanderVida
charmanderAtaque = 35
charmanderDefesa = 15

Squirtle = 2
squirtleVida = 120
squirtleAtaque = 20
squirtleDefesa = 30

Bulbasaur = 3
bulbasaurVida = 160
bulbasaurAtaque = 15
bulbasaurDefesa = 20



pokemonAleatorio = random.randint(1,3)
if pokemonAleatorio == 1:
    print("Seu adversario é Charmander")    
elif pokemonAleatorio == 2:
    print("Seu adversario é Squirtle")
elif pokemonAleatorio == 3:
    print("Seu adversario é Bulbasaur")

Charmander = 1 
charmanderVidaInimigo = 105
pokemonAleatorio = charmanderVidaInimigo
charmanderAtaqueInimigo = 40
charmanderDefesaInimigo = 20

Squirtle = 2
squirtleVidaInimigo = 125
pokemonAleatorio = squirtleVidaInimigo
squirtleAtaqueInimigo = 25
squirtleDefesaInimigo = 35

Bulbasaur = 3
bulbasaurVidaInimigo = 160
pokemonAleatorio = bulbasaurVidaInimigo
bulbasaurAtaqueInimigo = 15
bulbasaurDefesaInimigo = 20
    

print("=====  SUA BATALHA INICIOU ======")
# turno = 0 tentar pensar em como colocar o turno
while True:
    print("Sua vida: ", pokemonUsuario, "|" " Vida do inimigo", pokemonAleatorio)
    print("=====  Escolha uma ação ======")
    print(" 1 - Atacar")
    print(" 2 - Defender")
    print(" 3 - Fugir")

    acaoUsuario = int(input("Digite o numero"))

    if acaoUsuario == 1:
        print("Você atacou!!")
        break
    elif acaoUsuario == 2:
        print("Você se defedeu!!")
        break
    elif acaoUsuario == 3:
        print("Você fugiu!!")
        break
    
        
