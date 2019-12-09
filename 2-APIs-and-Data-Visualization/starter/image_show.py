from PIL import Image
import requests
from io import BytesIO


def show_img_from_url(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img.show()
