import os
os.system("docker-compose -f docker/docker-compose.yml down -v --rmi all")
os.system("docker build -f docker/Dockerfile -t maze_tf .")
os.system("docker-compose -f docker/docker-compose.yml up -d")
os.system("docker logs docker_testrunner_1 -f")
