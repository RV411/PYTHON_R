import PIL.Image

#ascii characters used to build the output text
ASCII_CHARS=["@","#","S","%","?","*","+",";",":",",","."]

#resize image accordign to a new width
def resize_image(image,new_width=100):
    width,height=image.size
    ratio=height/width
    new_height=int(new_width*ratio)
    resize_image=image.resize((new_width,new_height))
    return(resize_image)

#convert each pixel to grayscale
def grafity(image):
    grayscale_image=image.convert("L")
    return(grayscale_image)

#convert pixel to a string of ASCII characters
def pixels_to_ascii(image):
    pixels=image.getdata()
    characters="".join([ASCII_CHARS[pixel//25] for pixel in pixels])
    return(characters)

def main( new_width=100):
    #attemp to open image form user-input
    path=input("Ingresa el path de la imagen:\n")

    try:
        image=PIL.Image.open(path)
    except:
        print(path,": el path no tiene imagen")

    #convert image to ASCII
    new_image_data=pixels_to_ascii(grafity(resize_image(image)))

    #format
    pixel_count=len(new_image_data)
    ascii_image="\n".join(new_image_data[i:(i+new_width)] for i in range (0, pixel_count,new_width))

    #print result
    print(ascii_image)

    #save result
    with open("ascii_image.txt","w") as f:
        f.write(ascii_image)


main()