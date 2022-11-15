import tkinter as tk
from tkinter import filedialog

from utils import filtering_images, move_folder_image, validate_folder_exist


new_directory_path = ""
actual_directory_path = ""


# call function when we click on entry box
def width_click(*args):
    min_width.delete(0, 'end')


def height_click(*args):
    min_height.delete(0, 'end')


def ask_actual_directory() -> None:
    """
    Obtiene la ruta de la actual carpeta en la cual se van a guardar las
    imágenes
    """
    global actual_directory_path
    actual_directory_path = filedialog.askdirectory()


def ask_new_directory() -> None:
    """
    Obtiene la ruta de la nueva carpeta en la cual se van a guardar las
    imágenes
    """
    global new_directory_path
    new_directory_path = filedialog.askdirectory()


def clear() -> None:
    """
    Limpia todas las entradas de la ventana
    """
    min_width.delete(0, tk.END)
    min_height.delete(0, tk.END)

    ...


def main() -> None:
    actual_dir = actual_directory_path
    new_dir = new_directory_path
    image_min_width = int(min_width.get())
    image_min_height = int(min_height.get())

    validate_folder_exist(new_dir, label_result)
    image_list = filtering_images(
        actual_dir, image_min_width, image_min_height
    )

    if len(image_list) == 1:
        label_result["text"] = (
            f"{len(image_list)} imagen va a ser movida de carpeta"
        )
    else:
        label_result["text"] = (
            f"{len(image_list)} imágenes van a ser movidas de carpeta"
        )

    move_folder_image(image_list, actual_dir, new_dir, label_result)

    label_result["text"] = "Se movieron todas las imágenes."

    ...


window = tk.Tk()
window.title("Filtrar Imágenes")
window.resizable(width=False, height=False)

width_entry = tk.Frame(master=window)
min_width = tk.Entry(master=width_entry, width=20, borderwidth=5)
min_width.insert(0, "Anchura de la imagen")
min_width.bind("<Button-1>", width_click)

height_entry = tk.Frame(master=window)
min_height = tk.Entry(master=height_entry, width=20, borderwidth=5)
min_height.insert(0, "Altura de la imagen")
min_height.bind("<Button-1>", height_click)

btn_ask_actual_dir = tk.Button(
    master=window,
    text="Actual Directorio",
    command=lambda:ask_actual_directory(),
    width=15
)

btn_new_actual_dir = tk.Button(
    master=window,
    text="Nuevo Directorio",
    command=lambda:ask_new_directory(),
    width=15
)

btn_filter = tk.Button(
    master=window,
    text="Filtrar",
    command=main
)

btn_clear = tk.Button(
    master=window,
    text="Limpiar",
    command=clear
)

label_result = tk.Label(master=window, text="Esperando...")

width_entry.grid(row=0, column=0, padx=15, pady=15)
min_width.grid(row=0, column=0, sticky="e")

height_entry.grid(row=1, column=0)
min_height.grid(row=1, column=0, sticky="e")

btn_ask_actual_dir.grid(row=2, column=0, padx=15, pady=10)

btn_new_actual_dir.grid(row=3, column=0, padx=15, pady=10)

btn_filter.grid(row=4, column=2, pady=10)

btn_clear.grid(row=4, column=3, pady=10)

label_result.grid(row=6, column=3, padx=10, sticky="w")

window.mainloop()
