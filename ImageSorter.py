import os
import shutil
from tkinter import Tk, Label, Button
from tkinter import filedialog
from PIL import Image, ImageTk

class ImageSorter:
    def __init__(self, folder_path, folder_names):
        self.folder_path = folder_path
        
        # Создаем папки
        self.folders = []
        for folder_name in folder_names:
            folder_path_full = os.path.join(folder_path, folder_name)
            os.makedirs(folder_path_full, exist_ok=True)
            self.folders.append(folder_path_full)

        self.images = [f for f in os.listdir(folder_path) if f.endswith(('jpg', 'jpeg', 'png', 'bmp'))]
        self.index = 0
       
        self.setup_ui()
    # Оболочка
    def setup_ui(self): 
        self.root = Tk()
        self.root.configure(background='black')
        self.root.title("Image Sorter by eRas")
        self.label = Label(self.root)
        self.label.pack(expand=True) #expend=True - отвечает за отображение фото по центру
        
        #Словарь где хранятся расположение кнопок
        user_buttons = {1: 'left', 2: 'right', 3: 'bottom', 4: 'top'}

        #Пусто словрь для создания кнопок
        buttons = []
        
        #В этом цикле создаются кнопки, и добавляются в список buttons, после идет распоковка, где берется значение из user_buttons (располождение кнопки)
        for i in range(len(folder_names)):
            btn = Button(self.root, text=folder_names[i], command=lambda i=i: self.move_to_folder(self.folders[i]))
            buttons.append(btn)
            btn.pack(side=user_buttons.get(i+1))

        #Папки по умолчанию на кнопках, отсюда вывод -- > забинжены только 4 стрелки
        self.load_image()
        self.root.bind("<Left>", lambda event: self.move_to_folder(self.folders[0]))  
        self.root.bind("<Right>", lambda event: self.move_to_folder(self.folders[1])) 
        self.root.bind("<Down>", lambda event: self.move_to_folder(self.folders[2])) 
        self.root.bind("<Up>", lambda event: self.move_to_folder(self.folders[3])) 
        self.root.mainloop()
    #Загрузка фото в окно
    def load_image(self):
        if self.index < len(self.images):
            image_path = os.path.join(self.folder_path, self.images[self.index])
            img = Image.open(image_path)
            self.photo = ImageTk.PhotoImage(img)
            self.label.config(image=self.photo)
            self.label.image = self.photo
        else:
            self.label.config(text="Все изображения отсортированы!")
            self.label.image = None
    #Перемещаем фото
    def move_to_folder(self, target_folder):
        if self.index < len(self.images):
            source_image_path = os.path.join(self.folder_path, self.images[self.index])
            shutil.move(source_image_path, target_folder)
            self.index += 1
            self.load_image()

if __name__ == '__main__':
    folder_path = filedialog.askdirectory(title="Выберите папку с изображениями")
    if folder_path:
        num_folders = int(input("Введите количество папок для создания: "))
        folder_names = []
        for i in range(num_folders):
            folder_name = input(f"Введите название для папки {i + 1}: ")
            if folder_name:
                folder_names.append(folder_name)
        
        if folder_names:
            sorter = ImageSorter(folder_path, folder_names)

