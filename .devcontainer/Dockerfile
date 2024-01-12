FROM ubuntu
ARG DEBIAN_FRONTEND=noninteractive
RUN --mount=type=cache,target=/var/cache/apt \
    apt-get update && \
    apt-get install -y  build-essential \
                    git \
                    ca-certificates \
                    curl \
                    unzip
RUN apt-get install -y python3-pip
RUN pip3 install jupyterlab fastapi uvicorn[standard]
