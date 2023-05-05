peca1 = input().split()

cod1 = int(peca1[0])
numero1 = int(peca1[1])
valorUnit1 = float(peca1[2])

peca2 = input().split()

cod2 = int(peca2[0])
numero2 = int(peca2[1])
valorUnit2 = float(peca2[2])

valor_pagar = (valorUnit1 * numero1) + (valorUnit2 * numero2) #valor a ser pago

print("VALOR A PAGAR: R$ {:.2f}".format(valor_pagar))