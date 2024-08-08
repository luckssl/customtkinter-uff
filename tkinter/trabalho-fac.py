import customtkinter as ctk

"""O Chat GPT foi usado para organizar os dados que  foram usados como "entrada", não no próprio código
mas durante a montagem do algoritmo

Ex: if cod == "TCC00296" and tur == "A1":
    mat = "fundamentos de arquiteturas de computadores"
    dsem = "Terças e Quintas,"
    sala = "206"
    hor = "11h às 13h"



organize as seguintes informações de acordo com a estrura acima:

se cod == "TCC00296" and tur == "B1":

sala 213, mat "fundamentos de arquiteturas de computadores", dsem "Terças e Quintas, hor  hor = "11h às 13h"


do contrário se cod == "GGM00137" and tur == "D1":

sala 303, mat "Fundamentos de Cálculo e Geometria", dsem "Terças e Quintas", hor "09h às 11h"

do contrário se cod == "GGM00137" and tur == "E1":

sala 501, mat "Fundamentos de Cálculo e Geometria", dsem "Terças e Quintas", hor "09h às 11h"

do contrário se cod == "GAN00167" and tur == "B1":

sala 404, mat "Matemática discreta", dsem "Segundas e Quartas", hor "14h às 16h"

do contrário se cod == "GAN00167" and tur == "C1":

sala 404, mat "Matemática discreta", dsem "Segundas e Quartas", hor "14h às 16h"


do contrário se cod == "TCC00346" and tur == "AA":

lab 303, mat "Laboratório e Resolução de Problemas", dsem "Quartas", hor "09h às 11h"

do contrário se cod == "TCC00346" and tur == "BA":

lab 307, mat "Laboratório e Resolução de Problemas", dsem "Quartas", hor "09h às 11h"

do contrário se cod == "TCC00346" and tur == "CA":


lab 303, mat "Laboratório e Resolução de Problemas", dsem "Segundas", hor "09h às 11h"

do contrário se cod == "TCC00308" and tur == "A1" 

    dsem = (input("digite o dia da semana:"))
	se dsem == "Segunda" or dsem == "segunda" or dsem == "Segunda-feira" 

		lab 304, mat "Programação de Computadores I", hor "09h às 11h"
		do contrário se dsem == "Quarta" or dsem == "quarta" or dsem == "Quarta-feira"
			sala 303, mat "Programação de Computadores I", hor "09h às 11h"

do contrário se cod == "TCC00308" and tur == "B1" 

dsem = (input("digite o dia da semana:"))
	se dsem ==  "Segunda" or dsem == "segunda" or dsem == "Segunda-feira"

		sala 313, mat "Programação de Computadores I", hor "09h às 11h"
		do contrário se dsem == "Quarta" or dsem == "quarta" or dsem == "Quarta-feira"
			lab 303, mat "Programação de Computadores I", hor "09h às 11h"


Repita o mesmo código, porém, substitua a variável sala por lab quando cod == "TCC00308" and tur == "A1" e dsem == "Segunda" or dsem == "segunda" or dsem == "Segunda-feira" . 
Além disso, substitua a variável sala por lab quando cod == "TCC00308" and tur == "B1" e dsem == "Quarta" or dsem == "quarta" or dsem == "Quarta-feira"



#Resposta do Chat GPT:

cod = input("Digite o código da disciplina: ")
tur = input("Digite o código da turma: ")

if cod == "TCC00296" and tur == "A1":
    mat = "fundamentos de arquiteturas de computadores"
    dsem = "Terças e Quintas,"
    sala = "206"
    hor = "11h às 13h"
elif cod == "TCC00296" and tur == "B1":
    sala = "213"
    mat = "fundamentos de arquiteturas de computadores"
    dsem = "Terças e Quintas,"
    hor = "11h às 13h"
elif cod == "GGM00137" and tur == "D1":
    sala = "303"
    mat = "Fundamentos de Cálculo e Geometria"
    dsem = "Terças e Quintas"
    hor = "09h às 11h"
elif cod == "GGM00137" and tur == "E1":
    sala = "501"
    mat = "Fundamentos de Cálculo e Geometria"
    dsem = "Terças e Quintas"
    hor = "09h às 11h"
elif cod == "GAN00167" and tur == "B1":
    sala = "404"
    mat = "Matemática discreta"
    dsem = "Segundas e Quartas"
    hor = "14h às 16h"
elif cod == "GAN00167" and tur == "C1":
    sala = "404"
    mat = "Matemática discreta"
    dsem = "Segundas e Quartas"
    hor = "14h às 16h"
elif cod == "TCC00346" and tur == "AA":
    sala = "lab 303"
    mat = "Laboratório e Resolução de Problemas"
    dsem = "Quartas"
    hor = "09h às 11h"
elif cod == "TCC00346" and tur == "BA":
    sala = "lab 307"
    mat = "Laboratório e Resolução de Problemas"
    dsem = "Quartas"
    hor = "09h às 11h"
elif cod == "TCC00346" and tur == "CA":
    sala = "lab 303"
    mat = "Laboratório e Resolução de Problemas"
    dsem = "Segundas"
    hor = "09h às 11h"
elif cod == "TCC00308" and tur == "A1":
    dsem = input("Digite o dia da semana: ")
    if dsem == "segunda" or dsem == "segunda-feira" or dsem == "Segunda" or dsem == "Segunda-feira" :
        sala = "lab 304"
        mat = "Programação de Computadores I"
        hor = "09h às 11h"
    elif dsem == "Quarta" or dsem == "quarta" or dsem == "quarta-feira" or dsem == "Quarta-feira":
        sala = "303"
        mat = "Programação de Computadores I"
        hor = "09h às 11h"
elif cod == "TCC00308" and tur == "B1":
    dsem = input("Digite o dia da semana: ")
    if dsem == "segunda" or dsem == "segunda-feira" or dsem == "Segunda" or dsem == "Segunda-feira" :
        sala = "313"
        mat = "Programação de Computadores I"
        hor = "09h às 11h"
    elif dsem == "Quarta" or dsem == "quarta" or dsem == "quarta-feira" or dsem == "Quarta-feira":
        sala = "lab 303"
        mat = "Programação de Computadores I"
        hor = "09h às 11h"

print("Sala:", sala)
print("Matéria:", mat)
print("Dia e horário:", dsem, hor)



"""
#A variável para Matérias está como "disc"
#mat = str(input("Insira o nome da disciplina em minúsculo (exemplo: fundamentos de arquiteturas de computadores)"))

#Código da turma = cod
def nova_tela():
    nova_janela = ctk.CTkToplevel(janela)
    nova_janela.geometry("500x350")

janela = ctk.CTk()
janela.title("Encontrar sala de aula")
janela.geometry("500x300")

codigo_rotulo = ctk.CTkLabel(janela, text="Digite o código da matéria: ")
codigo_rotulo.pack()
cod = ctk.CTkEntry(janela)
cod.pack(padx=10, pady=10)
cod = cod.get()

turma_rotulo = ctk.CTkLabel(janela, text="Digite sua turma: ")
turma_rotulo.pack()
tur = ctk.CTkEntry(janela)
tur.pack(padx=10, pady=10)
tur = tur.get()

button_rotulo = ctk.CTkButton(janela, text="Confirmar", command=nova_tela())
button_rotulo.pack(padx=10, pady=10)

while cod != "TCC00296" and cod != "GAN00167" and cod != "GGM00137" and cod != "TCC00308" and cod != "TCC00346":
    print("Código inválido")
    cod = str(input("Insira o código da turma (exemplo:TCC00296): "))

#Turma = tur
while tur != "D1" and tur != "E1" and tur != "B1" and tur != "C1" and tur != "A1" and tur != "AA" and tur != "BA" and tur != "CA":
    print("Código inválido")
    tur = str(input("Insira sua turma (exemplo:A1): "))

#Dia da semana = dsem
#dsem
#Sala da aula = sala
#sala = int()
#Institutos = inst
#Horários = hor

mat = 0
inst = 0
dsem = 0
hor = 0
sala = 0

if cod == "TCC00296" and tur == "A1":
    mat = "fundamentos de arquiteturas de computadores"
    #inst = "instituto de computação (Bloco  tal)"
    dsem = "Terças e Quintas,"
    sala = "206"
    hor = "11h às 13h"
    #local = "-22.906448057524642, -43.133247500730846"

if cod == "TCC00296" and tur == "A1":
    mat = "fundamentos de arquiteturas de computadores"
    dsem = "Terças e Quintas,"
    sala = "206"
    hor = "11h às 13h"


elif cod == "TCC00296" and tur == "B1":
    sala = "213"
    mat = "fundamentos de arquiteturas de computadores"
    dsem = "Terças e Quintas,"
    hor = "11h às 13h"

elif cod == "GGM00137" and tur == "D1":
    inst = "UFASA - BLOCO H"
    sala = "303"
    mat = "Fundamentos de Cálculo e Geometria"
    dsem = "Terças e Quintas"
    hor = "09h às 11h"

elif cod == "GGM00137" and tur == "E1":
    #inst = "UFASA - BLOCO H"
    sala = "501"
    mat = "Fundamentos de Cálculo e Geometria"
    dsem = "Terças e Quintas"
    hor = "09h às 11h"
    
elif cod == "GAN00167" and tur == "B1":
    sala = "404"
    mat = "Matemática discreta"
    dsem = "Segundas e Quartas"
    hor = "14h às 16h"
    
elif cod == "GAN00167" and tur == "C1":
    sala = "404"
    mat = "Matemática discreta"
    dsem = "Segundas e Quartas"
    hor = "14h às 16h"
    
elif cod == "TCC00346" and tur == "AA":
    sala = "lab 303"
    mat = "Laboratório e Resolução de Problemas"
    dsem = "Quartas"
    hor = "09h às 11h"
   
elif cod == "TCC00346" and tur == "BA":
    sala = "lab 307"
    mat = "Laboratório e Resolução de Problemas"
    dsem = "Quartas"
    hor = "09h às 11h"
    
elif cod == "TCC00346" and tur == "CA":
    
    sala = "lab 303"
    mat = "Laboratório e Resolução de Problemas"
    dsem = "Segundas"
    hor = "09h às 11h"
    
elif cod == "TCC00308" and tur == "A1":
    dsem = input("Digite o dia da semana: ")
    if dsem == "segunda" or dsem == "segunda-feira" or dsem == "Segunda" or dsem == "Segunda-feira" :
        sala = "lab 304"
        mat = "Programação de Computadores I"
        hor = "09h às 11h"
    
    elif dsem == "Quarta" or dsem == "quarta" or dsem == "quarta-feira" or dsem == "Quarta-feira":
        sala = "303"
        mat = "Programação de Computadores I"
        hor = "09h às 11h"

elif cod == "TCC00308" and tur == "B1":
    dsem = input("Digite o dia da semana: ")
    if dsem == "segunda" or dsem == "segunda-feira" or dsem == "Segunda" or dsem == "Segunda-feira" :
        sala = "313"
        mat = "Programação de Computadores I"
        hor = "09h às 11h"
        
    elif dsem == "Quarta" or dsem == "quarta" or dsem == "quarta-feira" or dsem == "Quarta-feira":
        sala = "lab 303"
        mat = "Programação de Computadores I"
        hor = "09h às 11h"
    

    
if cod.startswith("TCC"):
    inst = "instituto de computação"
    local = "https://maps.app.goo.gl/tH1Tak8tBRePeGjF6"
elif cod.startswith("GGM"):
    inst = "instituto de matemática e estatística (Bloco H)"
    local = "https://maps.app.goo.gl/6u6FdQufmprA2H7B6"
elif cod.startswith("GAN"):
    inst = "instituto de matemática e estatística (Bloco H)"
    local = "https://maps.app.goo.gl/6u6FdQufmprA2H7B6"





#ÁREAS DOS PRINTS
if (mat != 0 and inst != 0 and tur != 0 and dsem != 0 and hor != 0 and sala != 0):
    print("\nDisciplina:",mat)
    print("No",inst)
    print("Sua turma é a",tur)
    print("Sua aula será às",dsem,"das",hor,"na sala",sala,"\n")
    Mostrar_local = input("Deseja saber a localização? Responda com Sim ou Nao: ")

    if Mostrar_local == "sim" or Mostrar_local == "Sim":
        import webbrowser
        webbrowser.open(local)
else:
    print ("\ninformações inválidas")
