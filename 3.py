from PIL import Image

def create_collage(image_paths, output_format='JPEG'):

    try:
        images = [Image.open(path) for path in image_paths]

        min_width, min_height = min(image.size[0] for image in images), min(image.size[1] for image in images)
        resized_images = [image.resize((min_width, min_height)) for image in images]

        collage_width, collage_height = min_width * 2, min_height * 2
        collage = Image.new('RGB', (collage_width, collage_height))

        x_offset = 0
        y_offset = 0
        for i in range(2):
            for j in range(2):
                collage.paste(resized_images[i * 2 + j], (x_offset, y_offset))
                x_offset += min_width
            x_offset = 0
            y_offset += min_height

        collage.save('collage.' + output_format.lower())
        print(f"Collage saved as collage.{output_format.lower()}")

    except FileNotFoundError:
        print("One or more image files not found.")
    except IOError:
        print("Error reading image files.")

if __name__ == "__main__":
    image_paths = [
        "./images/biscuit.jpg",
        "./images/cat.jpg",
        "./images/decay.jpg",
        "./images/everblush.jpg"
    ]
    output_format = "JPEG" 

    create_collage(image_paths, output_format)