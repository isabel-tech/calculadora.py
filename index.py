from tkinter import *
import math

class Calculadora(): # Classe: Uma classe é como um molde para criar objetos. Nesse caso, Calculadora é um molde para criar calculadoras.
    def __init__(self): #Esse método é chamado automaticamente quando você cria uma nova calculadora. É como um "iniciador" que inicia a calculadora.
        self.total = 0 # Armazena o resultado total dos cálculos (inicialmente 0).
        self.current = '' # Armazena o número que o usuário está digitando (inicialmente vazio).
        self.input_value = True # Indica se o usuário pode inserir um novo valor (inicialmente True).
        self.check_sum = False # Indica se uma operação de soma está em andamento (inicialmente False).
        self.op = '' # Armazena a operação matemática escolhida (começa vazio).
        self.result = False # Indica se já foi calculado um resultado (começa como falso).
    
        
    def numero_enter(self, num):
        self.result= False
        primeiro_numero = input_entrada.get()
        segundo_numero = str(num)
        
        # Se o primeiro número for '0' e o usuário inserir outro número, removemos o '0'
        if primeiro_numero == '0':
            primeiro_numero = ''
        if self.op == 'mod': 
            self.current = primeiro_numero + "mod" + segundo_numero 
        else:
            # Concatenar o segundo número com o que já está no display
            self.current = primeiro_numero + segundo_numero
        self.display(self.current)

        
    def display(self, value):
        input_entrada.delete(0, END)
        input_entrada.insert(0, value) 
    
        
    def soma_do_total(self):
        self.result = True
        try:
            expressao = input_entrada.get().replace('÷', '/').replace('×', '*').replace('^', '**').replace('x', '*').replace('mod', '%')
            self.current = eval(expressao)
        except:
            self.current = float(self.current)  # Caso não seja uma expressão matemática, converte diretamente para float
        if self.check_sum == True:
            self.validar_funcao()
        else:
            self.total = self.current
        self.display(self.total)
        

    
    def validar_funcao(self):
        if self.op == 'add':
            self.total += self.current
        if self.op == 'sub':
            self.total -= self.current   
        if self.op == 'mult':
            self.total *= self.current   
        if self.op == 'divide':
            self.total /= self.current   
        if self.op == 'mod':
            self.total %= self.current
        if self.op == 'expo':
            self.total **= self.current
        if self.op == 'squared':
            self.current = self.current ** 2
        if self.op == 'log':
            self.current = math.log10(self.current)
        self.total = self.current 
        self.input_value = True
        self.check_sum = False
        self.display(self.total)
    
    def operacao(self, op):
        self.current = float(self.current)
        if self.check_sum:
            self.validar_funcao() 
        elif not self.result:  #  Se não houver operação pendente e ainda não houver resultado calculado, o valor digitado é armazenado em self.total
            self.total = float(self.current)
            self.input_value = True
        self.check_sum = True
        self.op = op
        self.result = False # Define self.result = False para indicar que o resultado ainda não foi calculado.
        
    
    def apagar(self):
        tamanho_numero = len(input_entrada.get())
        input_entrada.delete(tamanho_numero - 1, 'end')
        if tamanho_numero == 1:
            input_entrada.insert(0, '0') # índice, valor
    
    def limpar(self):
        self.result = False
        self.current = '0'
        self.display(0)
        self.input_value = True
        
    def limpar_tudo(self):
        self.limpar()
        self.total = 0
        
    def pressionar(self, simbolo):
        self.current = input_entrada.get() + simbolo
        self.display(self.current)
       
    def raiz_quadrada(self):
        self.result = False
        self.current = math.sqrt(float(input_entrada.get()))
        self.display(self.current)
        
    def sin(self):
        self.result = False
        self.current = math.sin(math.radians(float(input_entrada.get())))
        self.display(self.current)
        
    def cos(self):
        self.result = False
        self.current = math.cos(math.radians(float(input_entrada.get())))
        self.display(self.current)
    
    def tan(self):
        self.result = False
        self.current = math.tan(math.radians(float(input_entrada.get())))
        self.display(self.current)
    
    def escrever_pi(self):
        self.current = math.pi
        self.display(self.current)         
            
janela = Tk()
janela.title('Calculadora')
janela.geometry('438x700+500+200')

quadro_moldura = Frame(janela, bd=20, pady=0, relief=RIDGE) #relief=RIDGE: Define o estilo da borda do Frame como "ridge" (corda), o que cria um efeito tridimensional que parece que a borda está elevada em relação à área do Frame.
quadro_moldura.grid()

quadro_principal_moldura = Frame(quadro_moldura, bd=10, pady=2, bg='cadetblue', relief=RIDGE)
quadro_principal_moldura.grid()

quadro_principal = Frame(quadro_principal_moldura, bd=5, pady=2, relief=RIDGE) 
quadro_principal.grid()

input_entrada = Entry(quadro_principal, font=('arial', 18, 'bold'), bd= 14, width=26, bg='cadetblue', justify=RIGHT)
input_entrada.grid(row=0, column=0, columnspan=4, pady=1, ipady=10)
input_entrada.insert(0, '0') 

valor_adicionado = Calculadora()

teclado_numerico = '789456123'
i = 0
botao = []

for linha in range(4,7):
    for coluna in range(3):
        botao.append(Button(quadro_principal, width=6, height=2, font=('arial', 16, 'bold'), bd=4, text=teclado_numerico[i]))
        botao[i].grid(row=linha, column=coluna, pady=1)
        botao[i]['command'] = lambda x=teclado_numerico[i] : valor_adicionado.numero_enter(x)
        i += 1

botao_pi= Button(quadro_principal, width=6, height=2, font=('arial', 16, 'bold'), bd=4, text='π', bg='cadetblue', command= valor_adicionado.escrever_pi )
botao_pi.grid(row=1, column=0, pady=1)

botao_limpar = Button(quadro_principal, width=6, height=2, font=('arial', 16, 'bold'), bd=4, text=chr(67), bg='cadetblue', command= valor_adicionado.limpar)
botao_limpar.grid(row=1, column=1, pady=1)

botao_limpar_tudo = Button(quadro_principal, width=6, height=2, font=('arial', 16, 'bold'), bd=4, text=chr(67)+chr(69), bg='cadetblue', command= valor_adicionado.limpar_tudo)
botao_limpar_tudo.grid(row=1, column=2, pady=1)

botao_apagar = Button(quadro_principal, width=6, height=2, font=('arial', 16, 'bold'), bd=4, text='⌫', bg='cadetblue', command= valor_adicionado.apagar)
botao_apagar.grid(row=1, column=3, pady=1)

botao_raiz_quadrada = Button(quadro_principal, width=6, height=2, font=('arial', 16, 'bold'), bd=4, text='sqrt', bg='cadetblue', command= valor_adicionado.raiz_quadrada)
botao_raiz_quadrada.grid(row=2, column=0, pady=1)

botao_seno = Button(quadro_principal, width=6, height=2, font=('arial', 16, 'bold'), bd=4, text='Sin', bg='cadetblue', command= valor_adicionado.sin)
botao_seno.grid(row=2, column=1, pady=1)

botao_cosseno= Button(quadro_principal, width=6, height=2, font=('arial', 16, 'bold'), bd=4, text='Cos', bg='cadetblue', command= valor_adicionado.cos)
botao_cosseno.grid(row=2, column=2, pady=1)

botao_tangente= Button(quadro_principal, width=6, height=2, font=('arial', 16, 'bold'), bd=4, text='Tan', bg='cadetblue', command= valor_adicionado.tan)
botao_tangente.grid(row=2, column=3, pady=1)

botao_adicionar = Button(quadro_principal, width=6, height=2, font=('arial', 16, 'bold'), bd=4, text='+', bg='cadetblue', command= lambda:[valor_adicionado.operacao('add'), valor_adicionado.pressionar('+')])
botao_adicionar.grid(row=3, column=0, pady=1)

botao_subtrair = Button(quadro_principal, width=6, height=2, font=('arial', 16, 'bold'), bd=4, text='-', bg='cadetblue', command= lambda:[valor_adicionado.operacao('sub'), valor_adicionado.pressionar('-')])
botao_subtrair.grid(row=3, column=1, pady=1)

botao_multiplicar = Button(quadro_principal, width=6, height=2, font=('arial', 16, 'bold'), bd=4, text='×', bg='cadetblue', command= lambda:[valor_adicionado.operacao('mult'), valor_adicionado.pressionar('×')])
botao_multiplicar.grid(row=3, column=2, pady=1)

botao_dividir = Button(quadro_principal, width=6, height=2, font=('arial', 16, 'bold'), bd=4, text='÷', bg='cadetblue', command= lambda:[valor_adicionado.operacao('divide'), valor_adicionado.pressionar('÷')])
botao_dividir.grid(row=3, column=3, pady=1)

botao_log = Button(quadro_principal, width=6, height=2, font=('arial', 16, 'bold'), bd=4, text='log', bg='cadetblue', command= lambda:[valor_adicionado.operacao('log')])
botao_log.grid(row=4, column=3, pady=1)

botao_expoente_quadrado = Button(quadro_principal, width=6, height=2, font=('arial', 16, 'bold'), bd=4, text='x²', bg='cadetblue', command= lambda:valor_adicionado.operacao('squared'))
botao_expoente_quadrado.grid(row=5, column=3, pady=1)

botao_expoente = Button(quadro_principal, width=6, height=2, font=('arial', 16, 'bold'), bd=4, text='^', bg='cadetblue', command= lambda:[valor_adicionado.operacao('expo'), valor_adicionado.pressionar('^')])
botao_expoente.grid(row=6, column=3, pady=1)

botao_mod = Button(quadro_principal, width=6, height=2, font=('arial', 16, 'bold'), bd=4, text='mod', bg='cadetblue', command= lambda:valor_adicionado.operacao('mod'))
botao_mod.grid(row=7, column=0, pady=1)

botao_zero = Button(quadro_principal, width=6, height=2, font=('arial', 16, 'bold'), bd=4, text='0', bg='cadetblue', command= lambda:valor_adicionado.numero_enter(0))
botao_zero.grid(row=7, column=1, pady=1)

botao_ponto = Button(quadro_principal, width=6, height=2, font=('arial', 16, 'bold'), bd=4, text='.', bg='cadetblue', command= lambda:valor_adicionado.numero_enter('.'))
botao_ponto.grid(row=7, column=2, pady=1)

botao_igual = Button(quadro_principal, width=6, height=2, font=('arial', 16, 'bold'), bd=4, text='=', bg='cadetblue', command=valor_adicionado.soma_do_total)
botao_igual.grid(row=7, column=3, pady=1)


janela.mainloop()

