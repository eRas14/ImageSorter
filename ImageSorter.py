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

    def setup_ui(self):
        self.root = Tk()
        self.root.title("Сортировщик by eRas")
        self.label = Label(self.root)
        self.label.pack()

        # Создание кнопок для всех папок
        btn1 = Button(self.root, text=folder_names[0], command=lambda: self.move_to_folder(self.folders[0]))
        btn1.pack(side='left')

        btn2 = Button(self.root, text=folder_names[1], command=lambda: self.move_to_folder(self.folders[1]))
        btn2.pack(side='right')

        btn3 = Button(self.root, text=folder_names[2], command=lambda: self.move_to_folder(self.folders[2]))
        btn3.pack(side='bottom')

        btn4 = Button(self.root, text=folder_namesпа[3], command=lambda: self.move_to_folder(self.folders[3]))
        btn4.pack(side='right')


        self.load_image()
        self.root.bind("<Left>", lambda event: self.move_to_folder(self.folders[0]))  # Первая папка по умолчанию
        self.root.bind("<Right>", lambda event: self.move_to_folder(self.folders[1])) # Вторая папка по умолчанию
        self.root.bind("<Down>", lambda event: self.move_to_folder(self.folders[2])) # Третья папка по умолчанию
        self.root.bind("<Up>", lambda event: self.move_to_folder(self.folders[3])) # Четвертая папка по умолчанию
        self.root.mainloop()

    def load_image(self):
        if self.index < len(self.images):
            image_path = os.path.join(self.folder_path, self.images[self.index])
            img = Image.open(image_path)
            # img.thumbnail((400, 400))  # Изменяем размер изображения для отображения
            self.photo = ImageTk.PhotoImage(img)
            self.label.config(image=self.photo)
            self.label.image = self.photo
        else:
            self.label.config(text="Все изображения отсортированы!")
            self.label.image = None

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