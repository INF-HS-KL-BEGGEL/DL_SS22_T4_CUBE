import os

os.system("docker build -f docker/Dockerfile -t maze_tf .")
os.system("docker-compose -f docker/docker-compose.yml up")