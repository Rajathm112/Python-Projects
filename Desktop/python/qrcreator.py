#before startin you need to install the qrcode by pip install qrcode
import qrcode
#here you put the data you need to add in qrcode 
data="xyz"
#this will make the qrcode and store in the img
img=qrcode.make(data)
#the image will appear in the file where your program is situated tho and rember to add the png extension
img.save('rajath.png')