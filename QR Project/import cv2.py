
'''import cv2
a = cv2.QRCodeDetector()
retval, points, straight_qrcode = a.detectAndDecode(cv2.imread("/content/new.jpg"))
print(retval)'''  1st -  to decode img 1st



2nd - use that decoded link to create a new one
import qrcode
from urllib.parse import quote

amount = 1  
currency = "INR"

f_amount = f"{amount:.2f}"

pay_url = (
    f"upi:abc"  #add the link half till &am 
    f"&am={quote(f_amount)}&cu={quote(currency)}"
    f"&aid=xyz"  #remaining link after &aid
)

qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4,)

qr.add_data(pay_url)
qr.make(fit=True)

img = qr.make_image(fill='black', back_color='white')
img.save("fixed_pay_qr.png")
img.show()


- also try to match the pay_url to retval if its equal then gg
