import customtkinter as ctk
from turtle import RawTurtle, Canvas, TurtleScreen

title_font = ('ISOCPEUR', 40)
text_font = ('ISOCPEUR', 30)
credit_font = ('ISOCPEUR', 20)
txt_color = '#C5F9C7'


class Caterpillar:
    def __init__(self, window):
        self.window = window

        def desenho_circulo():
            turtle.circle(50)
        def desenho_frente():
            turtle.forward(50)
        def vira_direita():
            turtle.right(30)
        def vira_esquerda():
            turtle.left(30)
        def limpar():
            turtle.clear()
        def preto():
            turtle.pencolor('black')
        def branco():
            turtle.pencolor('white')
        def vermelho():
            turtle.pencolor('red')
        def amarelo():
            turtle.pencolor('yellow')
        def azul():
            turtle.pencolor('blue')
        def verde():
            turtle.pencolor('green')
        def levanta():
            turtle.up()
        def abaixa():
            turtle.down()

        self.window.title("AutoCAD Oficial Edição LabEEE")
        self.window.geometry('1440x960')
        self.window.resizable(False, False)
        self.window.configure(fg_color='black')
        
        label = ctk.CTkLabel(window, text='AutoCAD Oficial Edição LabEEE', text_color=txt_color, font=title_font)
        label.grid(row=0, column=0, padx=40, pady=20)

        frame = ctk.CTkFrame(window, fg_color='#2B2B2B', width=650, height=800)
        frame.grid(row=1, column=0, padx=60)
        frame.grid_propagate(False)

        credit = ctk.CTkLabel(window, text='Zac Milioli, LabEEE 2024', text_color=txt_color, font=credit_font)
        credit.grid(row=2, column=0, padx=10, pady=20)

        canvas = Canvas(window, width=720, height=960, highlightbackground='#2B2B2B')
        canvas.grid(row=0, rowspan=3, column=1)
        screen = TurtleScreen(canvas)
        screen.bgcolor('#2B2B2B')
        turtle = RawTurtle(screen)
        turtle.color('white')
        turtle.pensize(5)
        turtle.speed(5)
        turtle.fillcolor('#00FF0A')

        botao1 = ctk.CTkButton(frame, text='Círculo', font=text_font, fg_color='white', text_color='black', command=desenho_circulo)
        botao1.grid(row=0, column=0, pady=20, padx=40)
        botao2 = ctk.CTkButton(frame, text='Frente', font=text_font, fg_color='white', text_color='black', command=desenho_frente)
        botao2.grid(row=0, column=1, pady=20, padx=40)
        botao3 = ctk.CTkButton(frame, text='Direita', font=text_font, fg_color='white', text_color='black', command=vira_direita)
        botao3.grid(row=1, column=0, pady=20, padx=40)
        botao4 = ctk.CTkButton(frame, text='Esquerda', font=text_font, fg_color='white', text_color='black', command=vira_esquerda)
        botao4.grid(row=1, column=1, pady=20, padx=40)
        botao5 = ctk.CTkButton(frame, text='Limpar', font=text_font, fg_color='white', text_color='black', command=limpar)
        botao5.grid(row=2, column=0, pady=20, padx=40)
        botao6 = ctk.CTkButton(frame, text='Cor: Preto', font=text_font, fg_color='white', text_color='black', command=preto)
        botao6.grid(row=2, column=1, pady=20, padx=40)
        botao7 = ctk.CTkButton(frame, text='Cor: Branco', font=text_font, fg_color='white', text_color='black', command=branco)
        botao7.grid(row=3, column=0, pady=20, padx=40)
        botao8 = ctk.CTkButton(frame, text='Cor: Azul', font=text_font, fg_color='white', text_color='black', command=azul)
        botao8.grid(row=3, column=1, pady=20, padx=40)
        botao9 = ctk.CTkButton(frame, text='Cor: Amarelo', font=text_font, fg_color='white', text_color='black', command=amarelo)
        botao9.grid(row=4, column=0, pady=20, padx=40)
        botao10 = ctk.CTkButton(frame, text='Cor: Verde', font=text_font, fg_color='white', text_color='black', command=verde)
        botao10.grid(row=4, column=1, pady=20, padx=40)
        botao11 = ctk.CTkButton(frame, text='Cor: Vermelho', font=text_font, fg_color='white', text_color='black', command=vermelho)
        botao11.grid(row=5, column=0, pady=20, padx=40)
        botao12 = ctk.CTkButton(frame, text='Levantar Caneta', font=text_font, fg_color='white', text_color='black', command=levanta)
        botao12.grid(row=5, column=1, pady=20, padx=40)
        botao13 = ctk.CTkButton(frame, text='Abaixar Caneta', font=text_font, fg_color='white', text_color='black', command=abaixa)
        botao13.grid(row=6, column=0, pady=20, padx=40)


if __name__ == '__main__':
    root = ctk.CTk()
    caterpillar = Caterpillar(root)
    root.mainloop()

