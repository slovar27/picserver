import json
import os.path, glob

import random, datetime, base64, uuid

def get_randon_hash():
    x = uuid.uuid4().hex + "o"
    x = x + str(random.randint(1, 9999999999999999)) + "a"
    x = x + str(random.randint(1, 9999999999999999)) + "b"
    x = x + str(datetime.datetime.now())
    hash = (base64.b64encode(x.encode())).decode()[:64]
    return hash

def file_save_content(path, data):
    with open(path, "w") as file:
        file.write(data)