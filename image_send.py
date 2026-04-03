import requests
import base64
import io
import matplotlib.image as mpimg
from matplotlib import pyplot as plt
from skimage.io import imsave

server = "http://vcm-51187.vm.duke.edu:5001"

def load_image_into_b64(filename):
    with open(filename, "rb") as image_file:
        b64_bytes = base64.b64encode(image_file.read())
    b64_string = str(b64_bytes, encoding='utf-8')
    return b64_string

def upload_image(b64_string):
    data = {"image": b64_string,
            "net_id": "daw74",
            "id_no": 3,
            "font_size": 36,
            "font_color": "red"}
    r = requests.post(server + "/add_image",
                      json=data)
    print(r.status_code)
    print(r.text)


def main():
    # b64_str = load_image_into_b64("images.jpg")
    # print(b64_str)
    # upload_image(b64_str)
    r = requests.get(server+"/get_image/daw74/3")
    b64_string = r.text
    image_bytes = base64.b64decode(b64_string)
    with open("result.jpg", "wb") as out_file:
        out_file.write(image_bytes)



if __name__ == "__main__":
    main()