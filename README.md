# NAO-toolkit
An opensource NAO Python toolkit.

# Docker build instructions
This repo utilises docker to expedite build:
-   image (https://hub.docker.com/r/kw90/naoqi-opencv-developer) 

Command for build:
  - "docker compose up --build"

Please note - when wanting to run an interactive terminal, which needs users input please run the scripts commands in order:
- docker compose build
- docker compose run --rm python-container 
