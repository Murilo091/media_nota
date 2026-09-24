def calcular_media(media):

    notas = []

    media_notas = int(input("digite o numero de notas: "))
    for i in range(media_notas):

        nota = float(input("digite a nota {i + 1}: "))
        notas.append(notas)
                     
        media = sum(notas) / media_notas
        print(f"a media das notas é: {media}")

calcular_media()
