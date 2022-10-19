FROM kw90/naoqi-opencv-developer:latest

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# CMD [ "python", "./tests/understandWord.py"]
# CMD [ "python", "./tests/understandWord.py"]
# CMD [ "python", "./tests/reset.py"]
# CMD [ "python", "./tests/arms.py"]
