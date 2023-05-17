import tkinter as tk
from PIL import Image, ImageTk

# Crie uma instância da janela Tkinter
janela = tk.Tk()

# Carregue o arquivo GIF usando o PIL
gif_path = r"C:\Users\47829927855\Desktop\poke-game-main\img\critical.gif"
gif = Image.open(gif_path)

# Extrai os quadros da animação GIF
quadros = []
try:
    while True:
        quadro_atual = gif.copy()
        quadros.append(ImageTk.PhotoImage(quadro_atual))
        gif.seek(len(quadros))  # Vá para o próximo quadro
except EOFError:
    pass

# Crie um widget de rótulo para exibir a animação
label = tk.Label(janela)

def exibir_proximo_quadro(indice):
    # Atualize o rótulo com o próximo quadro da animação
    label.config(image=quadros[indice])
    janela.after(100, exibir_proximo_quadro, (indice + 1) % len(quadros))

# Inicie a exibição do primeiro quadro
exibir_proximo_quadro(0)

# Posicione o widget de rótulo na janela
label.pack()


janela.mainloop()
