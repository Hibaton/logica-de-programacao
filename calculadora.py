# Solicitar primeiro numero e convert-lo para int e o validar
numero_digitado=0
numero_para_calcular=0
resultado =0


while numero_digitado != int:
 try:
  numero_digitado =int(input("Digite um numero: "))
  break
 except ValueError:
  print("Valor invalido")
  print("Digite um numero inteiro")

resultado=numero_digitado
# a calculdaor faz os seguinte operacaoes (sum,sub,mult,div,AC(zerar para coemcar de novo))
# no final o usador tem o opcao de encerrar ou fazer  novo operacao
operacao=(input("Digite a operação (+, -, *, /,AC): "))
while operacao != 'AC':
 if operacao == "+":

    while numero_para_calcular != int:
     try:
      numero_para_calcular=int(input("Digite um numero: "))
      break
     except ValueError:
      print("Valor invalido")
      print("Digite um numero inteiro")
    resultado = resultado + numero_para_calcular
    print(resultado)
    operacao=(input("Digite a operação (+, -, *, /,AC): "))
 elif operacao == '-':
    while numero_para_calcular != int:
     try:
      numero_para_calcular=int(input("Digite um numero: "))
      break
     except ValueError:
      print("Valor invalido")
      print("Digite um numero inteiro")
    resultado= resultado - numero_para_calcular
    print(resultado)
    operacao=(input("Digite a operação (+, -, *, /,AC): "))
 elif operacao == '*':
     while numero_para_calcular != int:
      try:
       numero_para_calcular=int(input("Digite um numero: "))
       break
      except ValueError:
       print("Valor invalido")
       print("Digite um numero inteiro")
     resultado=resultado*numero_para_calcular
     print(resultado)
     operacao=(input("Digite a operação (+, -, *, /,AC): "))
 elif operacao == '/':
     while numero_para_calcular != int:
      try:
       numero_para_calcular=int(input("Digite um numero: "))
       break
      except ValueError:
       print("Valor invalido")
       print("Digite um numero inteiro")
     resultado=resultado/numero_para_calcular
     print(resultado)
     operacao=(input("Digite a operação (+, -, *, /,AC): "))
 else:
  print("Operação invalida")
  operacao=(input("Digite a operação (+, -, *, /,AC): "))
if operacao == 'AC':
# zerar o resultado para fazer novo operacao
  resultado=0
  numero_para_calcular=0
  print(resultado)
# solicitar se quer encerrar ou fazer novo operacao
  continue_calculadora=(input("Deseja fazer outra operação? (S/N): "))
  while continue_calculadora != 'S' and continue_calculadora != 'N':
    print("input invalido")
    continue_calculadora=(input("Deseja fazer outra operação? (S/N): "))
  if continue_calculadora == 'N':
     print("Obrigado por usar a calculadora")
  while continue_calculadora == 'S':
       while numero_digitado != int:
             try:
                numero_digitado =int(input("Digite um numero: "))
                break
             except ValueError:
                print("Valor invalido")
                print("Digite um numero inteiro")

       resultado=numero_digitado
       operacao=(input("Digite a operação (+, -, *, /,AC): "))
       while operacao != 'AC':
           if operacao == "+":

              while numero_para_calcular != int:
                   try:
                      numero_para_calcular=int(input("Digite um numero: "))
                      break
                   except ValueError:
                      print("Valor invalido")
                      print("Digite um numero inteiro")
              resultado=resultado + numero_para_calcular
              print(resultado)
              operacao=(input("Digite a operação (+, -, *, /,AC): "))
           elif operacao == '-':
                while numero_para_calcular != int:
                   try:
                      numero_para_calcular=int(input("Digite um numero: "))
                      break
                   except ValueError:
                     print("Valor invalido")
                     print("Digite um numero inteiro")
                resultado=resultado-numero_para_calcular
                print(resultado)
                operacao=(input("Digite a operação (+, -, *, /,AC): "))
           elif operacao == '*':
                while numero_para_calcular != int:
                   try:
                    numero_para_calcular=int(input("Digite um numero: "))
                    break
                   except ValueError:
                    print("Valor invalido")
                    print("Digite um numero inteiro")
                resultado=resultado*numero_para_calcular
                print(resultado)
                operacao=(input("Digite a operação (+, -, *, /,AC): "))
           elif operacao == '/':
                while numero_para_calcular != int:
                  try:
                   numero_para_calcular=int(input("Digite um numero: "))
                   break
                  except ValueError:
                   print("Valor invalido")
                   print("Digite um numero inteiro")
                resultado=resultado/numero_para_calcular
                print(resultado)
                operacao=(input("Digite a operação (+, -, *, /,AC): "))
           else:
               print("Operação invalida")
               operacao= (input("Digite a operação (+, -, *, /,AC): "))
       if operacao == 'AC':
# zerar o resultado e encerrar
          resultado=0
          # solicitar se quer encerrar ou fazer novo operacao
          continue_calculadora=(input("Deseja fazer outra operação? (S/N): "))
          if continue_calculadora == 'N':
            print("Obrigado por usar a calculadora")
            break

 
