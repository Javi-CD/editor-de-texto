

import tkinter as tk
from tkinter import filedialog

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Editor de Texto")
        
        # Crear la barra de menú
        self.menu_bar = tk.Menu(root)
        root.config(menu=self.menu_bar)
        
        # Crear un submenú Archivo
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Archivo", menu=self.file_menu)
        self.file_menu.add_command(label="Nuevo", command=self.new_file)
        self.file_menu.add_command(label="Abrir", command=self.open_file)
        self.file_menu.add_command(label="Guardar", command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Salir", command=root.quit)

        # Crear el cuadro de texto con scrollbar
        self.text_area = tk.Text(root, wrap='word')
        self.scroll_bar = tk.Scrollbar(root, command=self.text_area.yview)
        self.text_area.config(yscrollcommand=self.scroll_bar.set)
        self.text_area.pack(expand=1, fill='both')
        self.scroll_bar.pack(side='right', fill='y')
    
    def new_file(self):
        self.text_area.delete(1.0, tk.END)
    
    def open_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, 'r') as file:
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, file.read())
    
    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", 
                                                 filetypes=[("All Files", "*.*"), 
                                                            ("Text Files", "*.txt")])
        if file_path:
            with open(file_path, 'w') as file:
                file.write(self.text_area.get(1.0, tk.END))

if __name__ == "__main__":
    root = tk.Tk()
    app = TextEditor(root)
    root.mainloop()
