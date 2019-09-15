
import math
a = float(input('ângulo em radianos: '))
Vx = 50*math.cos(a) #velocidade eixo x
Vy = 50*math.sin(a) #velocidade eixo y
#H = (-Vy**2)/-20 #altura maxima
tempo = (-2*Vy)/-10 #tempo até encostar no chão
fotos = (tempo*5)
fotos_inteiras = int(fotos)
tempo_fotos = tempo/fotos
alcance = Vx*tempo #onde ela para no eixo x
alcance_foto = (alcance/fotos)
Haltura = (-Vy**2)/-20
altura_foto = Haltura/(fotos/2)
metade_das_fotos = int(fotos_inteiras/2)
print('Vy: {}, Vy: {}, tempo: {}, alcance: {}, Haltura: {} '.format(Vx,Vy,tempo,alcance,Haltura))
print(f'fotos{fotos}, ')
cont = 0
print('+'*7,'alcance X') 

eixoX = []
eixoY = []

alcance_por_foto = 0
cont = 0
cont2 = 0

while alcance_por_foto <= alcance:
#for foto in range(fotos_inteiras): #tragetoria eixo x
    print(alcance_por_foto, 'metros')
    alcance_por_foto = alcance_por_foto + alcance_foto
    cont += 1
    posição = Vy*cont - 10*(((cont)**2)/2)
    if posição < 0:
        break
    eixoX.append(alcance_por_foto)
    eixoY.append(posição)
print(alcance_por_foto, 'metros')   




print('+_+_+_+_+ agora vai putaria +_+_+_+_')

  
#print(altura_por_foto, 'metros')
print(f'contX {cont}')
print(f'contY {cont2}')
print(f'eixoX: {eixoX}')
print(f'eixoY: {eixoY}')
for eixo in range(0,len(eixoX)):
    for c in range(0,len(eixoY)):
        if eixo == c:
            print(f'eixoX: {eixoX[eixo]}, eixoY: {eixoY[c]}')
