import random
import urllib.request

def download_web_image(url):
    name = random.randrange(1,1000)
    full_name = str(name) + ".jpg"
    urllib.request.urlretrieve(url, full_name)

download_web_image("https://thenewboston.com/photos/users/8299/resized/d54bcecc3d46d82b31dffbb00a5dfdc0.jpg")


