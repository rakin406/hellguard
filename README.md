# hellguard
Home surveillance software to pretend like the FBI. **Spy** *your own* webcam!

## Installation and usage
```shell
git clone https://github.com/rakin406/hellguard.git
cd hellguard
pip3 install python-opencv
curl -L -O https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml

./hellguard.py haarcascade_frontalface_default.xml
OR
python3 hellguard.py haarcascade_frontalface_default.xml
```
