import argparse
import os, os.path
import shutil

from PIL import Image

parser = argparse.ArgumentParser(
    prog="Filtering Images",
    description=("Mueve de carpeta aquellas imágenes que tengan una resolución"
                 " igual o mayor a la indicada en los parámetros de anchura y "
                 "altura. El programa filtra las imágenes que tengan las "
                 "siguientes extensiones: .jpg, .png, .jpeg y .gif"),
    epilog='Disfruta el programa! :)'
)
parser.add_argument(
    "-mw",
    "--min-width",
    dest="min_width",
    help="Anchura la imagen",
    type=int,
    required=True
)
parser.add_argument(
    "-mh",
    "--min-height",
    dest="min_height",
    help="Altura de la imagen",
    type=int,
    required=True
)
parser.add_argument(
    "-ad",
    "--actual-directory",
    dest="actual_directory",
    help="Carpeta actual de las imágenes",
    type=str,
    required=True
)
parser.add_argument(
    "-nd",
    "--new-directory",
    dest="new_directory",
    help="Nueva carpeta de las imágenes",
    type=str,
    required=True
)
args = parser.parse_args()


def validate_folder_exist(new_path: str) -> None:
    """
    Verifica si la carpeta existe, de lo contrario la crea.

    Args:
        new_path:
            Nueva carpeta de las imágenes
    """
    if not os.path.exists(new_path):
        os.makedirs(new_path)
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
        if image_path[-4:] in images_extensions:
            image = Image.open(os.path.join(path, image_path))
            width, height = image.size

            if width >= min_width and height >= min_high:
                high_resolution.append(image_path)

    return high_resolution


def move_folder_image(images: list, old_path: str, new_path: str) -> None:
    """
    Mueve la imagen a la carpeta indicada.

    Args:
        images:
            Lista de imágenes que hay que mover de carpeta
        old_path:
            Carpeta actual de las imágenes
        new_path:
            Nueva carpeta de las imágenes

    Returns:
        Un mensaje indicando que la imagen se ha movido de carpeta.
    """
    for image in images:
        src_path = os.path.join(old_path, image)
        dst_path = os.path.join(new_path, image)
        shutil.move(src_path, dst_path)
        print(f"La imagen {image} ha sido movida a la carpeta {new_path}")


if __name__ == "__main__":
    actual_directory = args.actual_directory  # "/mnt/c/Users/derhk/OneDrive/Imágenes/Anime Wallpapers"
    new_directory = args.new_directory  # "/mnt/c/Users/derhk/OneDrive/Imágenes/Anime Wallpapers/1080p"
    image_min_width = args.min_width  # 1920
    image_min_height = args.min_height  # 1080


    validate_folder_exist(new_directory)
    image_list = filtering_images(
        actual_directory, image_min_width, image_min_height
    )

    if len(image_list) == 1:
        print(f"{len(image_list)} imagen va a ser movida de carpeta")
    else:
        print(f"{len(image_list)} imágenes van a ser movidas de carpeta")

    move_folder_image(image_list, actual_directory, new_directory)
