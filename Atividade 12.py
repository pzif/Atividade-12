import tkinter as tk
import sqlite3

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Cadastro de Produtos")        
        
        menu = tk.Menu(self)
        self.config(menu=menu)        
       
        submenu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Produtos", menu=submenu)
        submenu.add_command(label="Novo Produto", command=self.novo_produto)
    
        self.conn = sqlite3.connect("produtos.db")
        self.c = self.conn.cursor()
        self.c.execute("CREATE TABLE IF NOT EXISTS produtos (id INTEGER PRIMARY KEY, nome TEXT, preco REAL)")
        self.conn.commit()
        
    def novo_produto(self):
        
        janela = tk.Toplevel(self)
        janela.title("Novo Produto")        
    
        nome_label = tk.Label(janela, text="Nome:")
        nome_label.grid(row=0, column=0, padx=5, pady=5)
        nome_entry = tk.Entry(janela)
        nome_entry.grid(row=0, column=1, padx=5, pady=5)
        
        preco_label = tk.Label(janela, text="Preço:")
        preco_label.grid(row=1, column=0, padx=5, pady=5)
        preco_entry = tk.Entry(janela)
        preco_entry.grid(row=1, column=1, padx=5, pady=5)
        
        salvar_button = tk.Button(janela, text="Salvar", command=lambda: self.salvar_produto(janela, nome_entry.get(), preco_entry.get()))
        salvar_button.grid(row=2, column=1, padx=5, pady=5)
        
    def salvar_produto(self, janela, nome, preco):        
        self.c.execute("INSERT INTO produtos (nome, preco) VALUES (?, ?)", (nome, preco))
        self.conn.commit()
        
        janela.destroy()
        
if __name__ == "__main__":
    app = App()
    app.mainloop()
