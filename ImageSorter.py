
import os
import shutil
from tkinter import Tk, Label, Button
from tkinter import filedialog
from PIL import Image, ImageTk

class ImageSorter:
    def __init__(self, folder_path, folder_name_1, folder_name_2):
        self.folder_path = folder_path
        
        # Создаем папки
        self.folder_1 = os.path.join(folder_path, folder_name_1)
        self.folder_2 = os.path.join(folder_path, folder_name_2)
        os.makedirs(self.folder_1, exist_ok=True)
        os.makedirs(self.folder_2, exist_ok=True)

        self.images = [f for f in os.listdir(folder_path) if f.endswith(('jpg', 'jpeg', 'png', 'bmp'))]
        self.index = 0
        self.setup_ui()

    def setup_ui(self):
        self.root = Tk()
        self.root.title("Сортировщик")
        self.label = Label(self.root)
        self.label.pack()

        btn_left = Button(self.root, text=os.path.basename(self.folder_1), command=self.move_to_folder_1)
        btn_left.pack(side='left')

        btn_right = Button(self.root, text=os.path.basename(self.folder_2), command=self.move_to_folder_2)
        btn_right.pack(side='right')

        self.load_image()
        self.root.bind("<Left>", lambda event: self.move_to_folder_1())
        self.root.bind("<Right>", lambda event: self.move_to_folder_2())
        self.root.mainloop()

    def load_image(self):
        if self.index < len(self.images):
            image_path = os.path.join(self.folder_path, self.images[self.index])
            img = Image.open(image_path)
            img.thumbnail((400, 400))  # Изменяем размер изображения для отображения
            self.photo = ImageTk.PhotoImage(img)
            self.label.config(image=self.photo)
            self.label.image = self.photo
        else:
            self.label.config(text="Все изображения отсортированы!")
            self.label.image = None

    def move_to_folder_1(self):
        self.move_image(self.folder_1)

    def move_to_folder_2(self):
        self.move_image(self.folder_2)

    def move_image(self, target_folder):
        if self.index < len(self.images):
            source_image_path = os.path.join(self.folder_path, self.images[self.index])
            shutil.move(source_image_path, target_folder)
            self.index += 1
            self.load_image()


if __name__ == '__main__':
    folder_path = filedialog.askdirectory(title="Выберите папку с изображениями")
    if folder_path:
        folder_name_1 = input("Введите название для папки 1: ")
        folder_name_2 = input("Введите название для папки 2: ")
        if folder_name_1 and folder_name_2:
            sorter = ImageSorter(folder_path, folder_name_1, folder_name_2)


