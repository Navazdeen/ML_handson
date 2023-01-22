from django.shortcuts import render
from qrcode import QRCode
from Qrapp.settings import STATIC_DIR
# Create your views here.


def index(request):
    context = {
        'img':False
        }
    if request.method == 'POST':
        text = request.POST.get("Text")
        img = generate_qrcode(text)
        img.save(STATIC_DIR.joinpath('tmp.png'))
        context['img'] = True

    return render(request, 'main/index.django-html', context)


def generate_qrcode(text):
    qr = QRCode(version=1, box_size=10, border=5)
    qr.add_data(text)
    qr.make(fit=True)
    return qr.make_image()
