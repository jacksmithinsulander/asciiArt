from PIL import Image
import os

ASCII_CHARS = ["Ñ", "@", "#", "W", "$", "9", "8", "7", "6", "5", "4", "3", "2",
     "1", "0", "?", "!", "a", "b", "c", ";", ":", "+", "=", "-", ",", ".", "_",
      " "]

def resize_image(image, new_width=233):
    width, height = image.size
    ratio = height/width
    new_height = int((new_width * ratio) / 2)
    resized_image = image.resize((new_width, new_height))
    return(resized_image)

def grayify(image):
    grayscale_image = image.convert("L")
    return(grayscale_image)
    
def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel//9] for pixel in pixels])
    return(characters)    

def main(new_width=233):
    path = input("Enter a valid pathname to an image:\n")
    try:
        image = Image.open(path)
    except:
        print(path, " is not a valid pathname to an image.")
        return
  
    new_image_data = pixels_to_ascii(grayify(resize_image(image)))
    
    pixel_count = len(new_image_data)  
    ascii_image = "\n".join([
        new_image_data[index:(index+new_width)]
         for index in range(0, pixel_count, new_width)
    ])
    
    print(ascii_image)
    
    filename, ext = os.path.splitext(os.path.basename(path))
    with open(f"{filename}.txt", "w") as f:
        f.write(ascii_image)
 
main()