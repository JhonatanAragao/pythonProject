import math
angulo = float(input('Digite o ângulo que você deseja:\n'))
anguloConvertido = math.radians(angulo)
seno = math.sin(anguloConvertido)  #NOTA IMPORTANTE: aqui nesse caso a função math.sin (seno) retorna um valor em graus por padrão. Por isso nesse caso utilizamos math.radius para realizar a conversão desse resultado em graus para radianos.
cosseno = math.cos(anguloConvertido)
tangente = math.tan(anguloConvertido)
print ('o ângulo de {} tem o SENO de {:.2f}, o COSSENO de {:.2f} e a TANGENTE igual a {:.2f}'.format(angulo,seno, cosseno,tangente))

