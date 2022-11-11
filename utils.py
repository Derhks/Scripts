import os
import tkinter as tk
import shutil


from PIL import Image


def validate_folder_exist(
    new_path: str,
    label_result: tk.Label = None
) -> None:
    """
    Verifica si la carpeta existe, de lo contrario la crea.

    Args:
        new_path:
            Nueva carpeta de las imágenes
        label_result:
            Etiqueta en la que se van a mostrar los resultados
    """
    if not os.path.exists(new_path):
        os.makedirs(new_path)

        if label_result:
            label_result["text"] = (
                f"Al no encontrarse, la carpeta {new_path} ha sido creada"
            )
        else:
            print(f"Al no encontrarse, la carpeta {new_path} ha sido creada")


def filtering_images(path: str, min_width: int, min_high: int) -> list:
    """
    Filtra las imágenes con mejor resolución en otra carpeta.

    Args:
        path:
            Carpeta actual de la imagen
        min_width:
            Ancho mínimo de la imagen
        min_high:
            Alto mínimo de la imagen

    Returns:
        Lista con las imágenes con mejor resolución
    """
    images_extensions = [
        ".jpg",
        ".png",
        ".jpeg",
        ".gif",
        ".JPG",
        ".PNG",
        ".JPEG",
        ".GIF"
    ]
    high_resolution = []
    images = os.listdir(path)

    for image_path in images:
        # Bug: las imágenes con extensión .jpeg no las procesa
        if image_path[-4:] in images_extensions:
            image = Image.open(os.path.join(path, image_path))
            width, height = image.size

            if width >= min_width and height >= min_high:
                high_resolution.append(image_path)

    return high_resolution


def move_folder_image(
    images: list,
    old_path: str,
    new_path: str,
    label_result: tk.Label = None
) -> None:
    """
    Mueve la imagen a la carpeta indicada.

    Args:
        images:
            Lista de imágenes que hay que mover de carpeta
        old_path:
            Carpeta actual de las imágenes
        new_path:
            Nueva carpeta de las imágenes
        label_result:
            Etiqueta en la que se van a mostrar los resultados
    """
    for image in images:
        src_path = os.path.join(old_path, image)
        dst_path = os.path.join(new_path, image)
        shutil.move(src_path, dst_path)

        if label_result:
            label_result["text"] = (
                f"La imagen {image} ha sido movida a la carpeta {new_path}"
            )
        else:
            print(f"La imagen {image} ha sido movida a la carpeta {new_path}")

    ...
