# UoM Telstra M2M Challenge

# QR Generation code
# Written by Jun Min Cheong (Pheo)

################################################################################

import qrcode

# Generates and outputs a .PNG QR (L Err. Corr.) Code
def generate_qrcode(input_string="www.google.com",file_name="QR.PNG"):
	# Initialize Qr Cursor Settings
	qr = qrcode.QRCode(
			version=1,
			# L is sufficient since code is displayed digitally
			error_correction=qrcode.constants.ERROR_CORRECT_L,
			box_size=10,
			border=4,
			)
	# Add's input_string to Cursor
	qr.add_data(input_string)
	qr.make(fit=True)
	img = qr.make_image()
	image_file = open(file_name,"w+")
	# Write QR Code to file
	img.save(image_file,"PNG")
	image_file.close()
	
