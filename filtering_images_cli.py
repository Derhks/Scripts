import argparse

from utils import filtering_images, validate_folder_exist, move_folder_image


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
