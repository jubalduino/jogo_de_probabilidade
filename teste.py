import random

# O computador escolhe um número aleatório
numero_secreto = random.randint(1, 100)

print("🎮 Bem-vindo ao jogo!")
print("Tente adivinhar o número entre 1 e 100.")

# Loop do jogo
while True:
    try:
        palpite = int(input("Digite seu palpite: "))
    except ValueError:
        print("⚠️ Ei, digite apenas números inteiros!")
        continue  # Faz o loop voltar para o começo sem quebrar o jogo
    palpite = int(input("Digite seu palpite: "))

    if palpite == numero_secreto:
        print("🎉 Parabéns! Você acertou!")
        break
    elif palpite < numero_secreto:
        print("🔼 Tente um número maior.")
    else:
        print("🔽 Tente um número menor.")