nome = str(input())
salarioFixo = float(input())
totalVendas = float(input())

totalReceber = (totalVendas * 0.15) + salarioFixo

print("TOTAL = R$ {:.2f}".format(totalReceber))
