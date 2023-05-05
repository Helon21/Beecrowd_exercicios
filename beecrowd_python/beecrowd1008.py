numeroFunc = int(input()) #número do funcionário
horasTrab = int(input()) #horas trabalhadas
recebimentoPorHora = float(input()) #quanto ele recebe por hora?

salario = horasTrab * recebimentoPorHora

print("NUMBER = %i" %numeroFunc)
print("SALARY = U$ {:.2f}".format(salario))