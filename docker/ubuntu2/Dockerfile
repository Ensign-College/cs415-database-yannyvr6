FROM ubuntu:latest

# Update packages and create new user
RUN apt-get update && \
    useradd -ms /bin/bash myuser

# Switch to new user
USER myuser
WORKDIR /home/myuser

CMD ["bash"]