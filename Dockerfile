FROM kw90/naoqi-opencv-developer:latest

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN python -m pip install pip==19.2
RUN pip install --no-cache-dir -r requirements.txt
RUN pip --version

COPY . .

# CMD [ "python", "./tests/understandWord.py"]
# CMD [ "python", "./tests/understandWord.py"]
# CMD [ "python", "./tests/reset.py"]
# CMD [ "python", "./tests/arms.py"]
# CMD [ "pip", "--version"]
