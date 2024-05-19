import qrcode

# Données à encoder dans le QR code
data = "https://www.instagram.com"

# Créer un objet QRCode
qr = qrcode.QRCode(
    version=1,  # version: la taille du QR code (1 à 40, 1 est le plus petit)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # niveau de correction d'erreur
    box_size=10,  # taille de chaque boîte du QR code
    border=4,  # taille de la bordure
)

# Ajouter les donnees 
qr.add_data(data)
qr.make(fit=True)

# Créer une image du QR code
img = qr.make_image(fill_color="black", back_color="white")

# Sauvegarder l'image dans un fichier
img.save("qrcode.png")

print("QR code généré et sauvegardé sous le nom 'qrcode.png'")