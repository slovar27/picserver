from PIL import Image


def resize_to_width(path, target_path, new_width):
    pass
    image = Image.open(path)

    orig_width, orig_height = image.size

    ratio = new_width / orig_width

    new_height = int(ratio * orig_height)

    new_image = image.resize((new_width, new_height))
    print(image.size) # Output: (1920, 1280)
    print(new_image.size) # Output: (400, 400)

    new_image.save(target_path)

    #print(image2.size)








if __name__ == "__main__":
    pass
    resize_to_width("uploads/a1.jpg", 600)