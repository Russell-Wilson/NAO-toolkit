# NAO-toolkit
An opensource NAO Python toolkit.

# Docker build instructions

Please first rename the "example.env" file to ".env" and update the file with your environment variables.

This repo utilises docker to expedite build:
-   image (https://hub.docker.com/r/kw90/naoqi-opencv-developer) 

If the script requires no terminal interaction the script and build can then be run with the following. 
As no bind mounts are used for this work, a container is rebuilt on launch with the '--build' flag.
Command for build:
  - "docker compose up --build"

Please note - when wanting to run an interactive terminal, which needs users input please run the scripts commands in order:
- docker compose build
- docker compose run --rm python-container 

# Running GUIs

the Python Docker image is build on a Linux operating system. To run GUIs Docker images from a windows or mac pc an appropriate x11 server must be installed. 
- windows - VcXsrv - https://sourceforge.net/projects/vcxsrv/
- mac - Xquartz - https://www.xquartz.org/

before running your app ensure the x11 server is running and your "DISPLAY" env variable is updated in your .env folder. 
