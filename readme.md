# Presence list face recognition

Simple script that receive two filepath to image, find the faces, compare they and output the difference between faces.

This script was a part of Presence List system on https://github.com/decimo3/sistemas_indica_servicos repository.

Create a virtual environment:
```sh
python -m venv venv
```

Activate virtual environment:
```sh
source ./venv/bin/activate
```

Install de dependecies:
```sh
pip install -r requirements.txt
```

Run the test:
```sh
pytest test_presence_list.py
```

Build an executable:
```sh
pyinstaller ./presence_list.py --add-data "$VIRTUAL_ENV/Lib/site-packages/face_recognition_models/;./face_recognition_models/" --noconfirm
```

Run executable to compare faces:
```sh
presence_list.exe "/path/to/first/image.jpg" "/path/to/second/image.jpg"
```

The output will be:

```sh

```