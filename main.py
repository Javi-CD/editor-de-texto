import tkinter as tk
from tkinter import filedialog, font, colorchooser

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Editor de Texto")
        
        # Variables de tema y fuente
        self.theme = "light"
        self.font_family = "Arial"
        self.font_size = 12
        
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
        
        # Crear un submenú Editar
        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Editar", menu=self.edit_menu)
        self.edit_menu.add_command(label="Tema Oscuro", command=self.toggle_theme)
        self.edit_menu.add_command(label="Cambiar Tamaño de Fuente", command=self.change_font_size)
        self.edit_menu.add_command(label="Cambiar Color de Fuente", command=self.change_font_color)
        
        # Crear el cuadro de texto con scrollbar
        self.text_area = tk.Text(root, wrap='word', font=(self.font_family, self.font_size))
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
    
    def toggle_theme(self):
        if self.theme == "light":
            self.text_area.config(bg="black", fg="white", insertbackground="white")
            self.theme = "dark"
        else:
            self.text_area.config(bg="white", fg="black", insertbackground="black")
            self.theme = "light"
    
    def change_font_size(self):
        font_size = tk.simpledialog.askinteger("Tamaño de Fuente", "Ingrese el tamaño de la fuente:")
        if font_size:
            self.font_size = font_size
            self.text_area.config(font=(self.font_family, self.font_size))
    
    def change_font_color(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.text_area.config(fg=color)

if __name__ == "__main__":
    root = tk.Tk()
    app = TextEditor(root)
    root.mainloop()
