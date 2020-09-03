#!/usr/bin/env python
# coding: utf-8

# In[27]:


def calculadora():
   # Passo 1 - imprimir na tela o termo Python Calculator
    print ('******************* Python Calculator *******************')
    # Passo 2 - imprimir na tela uma mensagem para solicitando a seleção da operação desejada
    print ('Selecione o número da operação desejada:')
    # Passo 3 - imprimir na tela as opções de operações matemáticas
    print ('1 - Soma \n2 - Subtração \n3 - Multiplicação \n4 - Divisão')
    # Passo 4 - imprimir na tela a caixa para escolha da operação matemática desejada
    operação = int(input('Digite sua opção (1/2/3/4): '))
    # Passo 5 - imprimir na tela a caixa para entrada do primeiro número
    num1 = int(input('Digite o primeiro número: '))
    # Passo 6 - imprimir na tela a caixa para a entrada do segundo número
    num2 = int(input('Digite o segundo número: '))
    # Passo 7 - realizar a operação matemática escolhida com os números fornecidos nos passos 6 e 7
    if operação == 1:
        print ('%s + %s = ' %(num1, num2), num1 + num2)
    elif operação == 2:
        print ('%s - %s = ' %(num1, num2), num1 - num2)
    elif operação == 3:
        print ('%s x %s = ' %(num1, num2), num1 * num2)
    elif operação == 4:
        print ('%s / %s = ' %(num1, num2), num1 / num2)
    elif operação > 4:
        print ('Opção inválida!')
        

calculadora()


# ## 

# In[ ]:




