import math
a = float(input("digite o angulo que deseja: "))
sen = math.sin(math.radians(a))
print("o angulo de {} tem o seno de {:.2f}".format(a, sen))
cos = math.cos(math.radians(a))
print("o angulo de {} tem o cosseno de {:.2f}".format(a, cos))
tan = math.tan(math.radians(a))
print('o angulo de {} tem a tangente de {:.2f}'.format(a, tan))
