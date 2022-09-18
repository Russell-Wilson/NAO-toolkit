# NAO-toolkit
An opensource NAO Python toolkit.

# Docker build instructions
This repo utilises docker to expedite build:
-   image (https://hub.docker.com/r/kw90/naoqi-opencv-developer) 

If the script required no terminal interaction, the script can be run by creating a CMD entry in the dockerfile or a command entry in the compose file. 
The script and build can then be run with the following. If no rebuild is required then '--build' is not required
Command for build:
  - "docker compose up --build"

Please note - when wanting to run an interactive terminal, which needs users input please run the scripts commands in order:
- docker compose build
- docker compose run --rm python-container 
