
      




tempoSegundos = int(input())

restoSegundos = tempoSegundos % 60
tempoMinutos = tempoSegundos // 60
RestoMinutos = tempoMinutos % 60
tempoHoras = tempoMinutos // 60

totalMinutos = tempoMinutos - tempoHoras * 60

print(f"Este valor corresponde a {tempoHoras} hora(s) {totalMinutos} minuto(s) e {restoSegundos} segundo(s).")

distancia= float(input())
vMedia = float(input())
tempo = distancia / vMedia
print(f"O tempo estimado de viagem é {tempo} horas.")


