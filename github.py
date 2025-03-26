def calcular_media(n1, n2, n3, n4):
    total = n1 + n2 + n3 + n4
    media = total/4
    return media

def exibir_media(media):
    media = calcular_media(n1, n2, n3, n4)
    print(f"Sua média foi: {media}")

n1 = int(input("Digite sua nota: "))
n2 = int(input("Digite sua nota: "))
n3 = int(input("Digite sua nota: "))
n4 = int(input("Digite sua nota: "))

media = calcular_media(n1, n2, n3, n4)
exibir_media(media)

if media > 6:
    print("Você foi aprovado.")
else:
    print("Você foi reprovado.")
