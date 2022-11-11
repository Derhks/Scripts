import tkinter as tk

from utils import filtering_images, move_folder_image, validate_folder_exist


def main() -> None:
    actual_dir = actual_directory.get()
    new_dir = new_directory.get()
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
min_width = tk.Entry(master=width_entry, width=20)
label_min_width = tk.Label(master=window, text="Anchura de la imagen")

height_entry = tk.Frame(master=window)
min_height = tk.Entry(master=height_entry, width=20)
label_min_height = tk.Label(master=window, text="Altura de la imagen")

actual_directory_entry = tk.Frame(master=window)
actual_directory = tk.Entry(master=actual_directory_entry, width=20)
label_actual_directory = tk.Label(
    master=window,
    text="Ruta de la carpeta actual de las imágenes"
)

new_directory_entry = tk.Frame(master=window)
new_directory = tk.Entry(master=new_directory_entry, width=20)
label_new_directory = tk.Label(
    master=window,
    text="Ruta de la nueva carpeta de las imágenes"
)

btn_filter = tk.Button(
    master=window,
    text="Filtrar",
    command=main
)

label_result = tk.Label(master=window, text="Esperando...")

width_entry.grid(row=0, column=0, padx=15, pady=5)
min_width.grid(row=0, column=0, sticky="e")
label_min_width.grid(row=0, column=1, sticky="w")

height_entry.grid(row=1, column=0)
min_height.grid(row=1, column=0, sticky="e")
label_min_height.grid(row=1, column=1, sticky="w")

actual_directory_entry.grid(row=2, column=0, pady=5)
actual_directory.grid(row=2, column=0, sticky="e")
label_actual_directory.grid(row=2, column=1, sticky="w")

new_directory_entry.grid(row=3, column=0)
new_directory.grid(row=3, column=0, sticky="e")
label_new_directory.grid(row=3, column=1, sticky="w")

btn_filter.grid(row=4, column=2, pady=10)

label_result.grid(row=5, column=2, padx=10)

window.mainloop()
