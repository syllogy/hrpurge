FROM python:3.9.2-slim-buster

SHELL ["/bin/bash", "-o", "pipefail", "-c"]
RUN apt-get update && apt-get clean && \
    apt-get clean autoclean && \
    apt-get autoremove --yes && \
    rm -rf /var/lib/{apt,dpkg,cache,log}/

WORKDIR /usr/src

COPY . hrpurge/

RUN pip3 install --no-cache-dir -e ./hrpurge && \
    python3 -m compileall hrpurge/hrpurge

CMD [ "hrpurge" ]
