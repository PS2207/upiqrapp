import qrcode
from io import BytesIO
from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.core.image import Image as CoreImage
from kivy.uix.label import Label

class QRCodeApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        # Hardcoded UPI details
        upi_id = "pragyasinha959@oksbi"
        name = "Pragya"
        amount = "101"
        message = "Thanks"

        # Generate UPI QR code
        upi_url = f"upi://pay?pa={upi_id}&pn={name}&am={amount}&cu=INR&tn={message}"
        qr = qrcode.make(upi_url)

        # Convert QR code to a format Kivy can display
        buffer = BytesIO()
        qr.save(buffer, format='PNG')
        buffer.seek(0)
        core_image = CoreImage(buffer, ext='png')
        qr_image = Image(texture=core_image.texture)

        layout.add_widget(qr_image)
        layout.add_widget(Label(text=f"Scan this QR to pay {amount}", font_size='20sp'))

        return layout

if __name__ == '__main__':
    QRCodeApp().run()

