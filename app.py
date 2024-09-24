import random as rd

class ContaBancaria:

  def __init__(self, titular, senha, cpf, rg, agencia, numero, saldo, limite,pontos, milhas):
    self.titular = titular
    self._senha = senha
    self._cpf = cpf
    self._rg = rg
    self._agencia = agencia
    self._numero = numero
    self._saldo = saldo
    self._limite = limite
    self._pontos = pontos
    self._milhas = milhas

  @property
  def senha(self):
    return self._senha

  @senha.setter
  def senha(self,valor):
    self._senha = valor

  @property
  def cpf(self):
    return self._cpf

  @cpf.setter
  def cpf(self,valor):
    self._cpf = valor

  @property
  def rg(self):
    return self._rg

  @rg.setter
  def rg(self,valor):
    self._rg = valor

  @property
  def agencia(self):
    return self._agencia

  @agencia.setter
  def agencia(self,valor):
    self._agencia = valor

  @property
  def numero(self):
    return self._numero

  @numero.setter
  def numero(self,valor):
    self._numero = valor

  @property
  def saldo(self):
    return self._saldo

  @saldo.setter
  def saldo(self,valor):
    self._saldo = valor

  @property
  def limite(self):
    return self._limite

  @limite.setter
  def limite(self,valor):
    self._limite = valor

  @property
  def pontos(self):
    return self._pontos

  @pontos.setter
  def pontos(self, valor):
    self._pontos = valor

  @property
  def milhas(self):
    return self._milhas

  @milhas.setter
  def milhas(self, valor):
    self._milhas = valor

  def extrato(self):
    print("\n==== EXTRATO ====")
    print("-----------------")
    print(f"Titular: {self.titular}")
    print(f"Saldo: R${self._saldo}")
    print(f"Limite: R${self._limite}")
    print(f"Pontos: {self._pontos}")
    print(f"Milhas: {self._milhas}")

  def saque(self):

    tentativa = 1

    while tentativa <= 3:

      senha = input("\nInforme sua senha: ")

      valor_saque = float(input("Valor saque: R$ "))

      if senha == self._senha:

        if valor_saque <= self._saldo:
          self._saldo -= valor_saque
          print("\nSaque efetuado com sucesso!")
          break
        else:
          print("\nSaldo insuficiente!")
      else:

        print("\nSenha incorreta! Tente novamente.")
        tentativa += 1

  def deposito(self):

    tentativa = 1

    while tentativa <= 3:

      senha = input("\nInforme sua senha: ")

      if senha == self._senha:
        valor_deposito = float(input("Valor depósito: R$ "))
        self._saldo += valor_deposito
        print("\nDepósito efetuado com sucesso!")
        break
      else:
        print("\nSenha incorreta! Tente novamente.")
        tentativa += 1

  def compra_no_credito(self):

    tentativa = 1

    valor_compra = float(round(rd.uniform(10,200),2))

    while tentativa <= 3:

      print(f"\nValor da Compra: R${valor_compra}")

      senha = input("\nInforme sua senha: ")

      if senha == self._senha:

        if valor_compra <= self._limite:
          self._limite -= valor_compra
          self.junta_pontos(valor_compra)
          self.junta_milhas(valor_compra)
          print("\nCompra efetuada com sucesso!")
          break
        else:
          print("\nLimite insuficiente!")
          break

      else:
        print("\nSenha incorreta! Tente novamente.")
        tentativa += 1

  def junta_pontos(self, valor_compra):
    pontos = round((valor_compra / 5),0)
    self._pontos += pontos

  def junta_milhas(self, valor_compra):
    milhas = round((valor_compra / 8),0)
    self._milhas += milhas 
    
  def atelogo(self):
    print(f'Volte logo {self.titular}')

  def BoasVindas(self):
    print('\n|============== FLOWBANK ===================|')
    print('\n|----SEJA BEM VINDO A SUA CONTA BANCARIA!---|')
    print('|-------------------------------------------|')
    print('|-------PARA REALIZAR SAQUES DIGITE (1)-----|')
    print('|--------PARA REALIZAR DEPOSITOS DIGITE (2)-|')
    print('|PARA REALIZAR COMPRAS NO CREDITO DIGITE (3)|')
    print('|PARA VISUALIZAR EXTRATO DA CONTA DIGITE (4)|')
    print('|---------PARA SAIR DIGITE (5)--------------|')
    print('|===========================================|')

    opcao = int(input('\nDigite qual opção deseja realizar: '))

    if opcao == (1):
        conta.saque()
        conta.BoasVindas()
    if opcao == (2):
        conta.deposito()
        conta.BoasVindas()
    if opcao == (3):
        conta.compra_no_credito()
        conta.BoasVindas()
    if opcao == (4):
        conta.extrato()
        conta.BoasVindas()
    if opcao == (5):
        conta.atelogo()

conta = ContaBancaria('Pablo', '123','123.456.789-01','123.456.789-0','0001',0000,1000,2000,0,0)
conta.BoasVindas()
