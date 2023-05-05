a, b, c = map(float, input().split())

triangulo = a * c / 2.0
circulo = 3.14159 * c * c
trapezio = (a + b) * c / 2.0
quadrado = b * b
retangulo = a * b

print("Triangulo: {:.3f}".format(triangulo))
print("Circulo: {:.3f}".format(circulo))
print("Trapezio: {:.3f}".format(trapezio))
print("Quadrado: {:.3f}".format(quadrado))
print("Retangulo: {:.3f}".format(retangulo))
