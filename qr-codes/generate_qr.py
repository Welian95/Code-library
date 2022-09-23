from turtle import fillcolor
import qrcode
import qrcode.image.svg

def createqr (massage):
    '''this is a function to generate a qr code by given input 
    param massage : string with the massage shown from qr-code '''
    qr = qrcode.QRCode(box_size=50 , border= 5)                 #change size
    qr.add_data(massage)
    img = qr.make_image(fillcolor="black", back_color="white")  #change color
    
    #create an .svg file - svg is unlimited scaleable
    f = qrcode.image.svg.SvgPathImage
    img_svg = qrcode.make(massage, image_factory = f)

    return img, img_svg

if __name__ == "__main__":
    img, img_svg = createqr ("Dies ist der test des QR-Codes") 

    #img.save("test.png")   #save as png
    #img_svg("test.svg")    #save as svg

    img.show()              #Anzeigen des qr-codes

