ARG PYTHON_VERSION=3.9.2-alpine3.13
ARG ALPINE_VERSION=3.13

FROM alpine:$ALPINE_VERSION AS base

FROM base AS build-base
RUN apk add --no-cache curl

FROM build-base AS kubectl
ARG KUBECTL_VERSION=1.20.0
ARG KUBECTL_CHECKSUM=081472833601aa4fa78e79239f67833aa4efcb4efe714426cd01d4ddf6f36fbf304ef7e1f5373bff0fdff44a845f7560165c093c108bd359b5ab4189f36b1f2f
ARG SOURCE=https://dl.k8s.io/v$KUBECTL_VERSION/kubernetes-client-linux-amd64.tar.gz
ARG TARGET=/kubernetes-client.tar.gz
RUN curl -fLSs "$SOURCE" -o "$TARGET"
RUN sha512sum "$TARGET"
RUN echo "$KUBECTL_CHECKSUM *$TARGET" | sha512sum -c -
RUN tar -xvf "$TARGET" -C /

FROM build-base AS helm
ARG HELM_VERSION=3.5.3
ARG HELM_CHECKSUM=2170a1a644a9e0b863f00c17b761ce33d4323da64fc74562a3a6df2abbf6cd70
ARG SOURCE=https://get.helm.sh/helm-v$HELM_VERSION-linux-amd64.tar.gz
ARG TARGET=/helm.tar.gz
RUN curl -fLSs "$SOURCE" -o "$TARGET"
RUN sha256sum "$TARGET"
RUN echo "$HELM_CHECKSUM *$TARGET" | sha256sum -c -
RUN mkdir -p /helm
RUN tar -xvf "$TARGET" -C /helm

FROM build-base AS stage
WORKDIR /stage
ENV PATH=$PATH:/stage/usr/bin
COPY --from=kubectl /kubernetes/client/bin/kubectl ./usr/bin/
COPY --from=helm /helm/linux-amd64/[ht]* ./usr/bin/

FROM python:$PYTHON_VERSION

ENV HOME=/home/app/

COPY --from=stage [ "/stage/", "/" ]

SHELL ["/bin/sh", "-o", "pipefail", "-c"]
RUN apk add --no-cache jpeg-dev zlib-dev tini && \
    adduser -D python && mkdir $HOME && chown -R python:python $HOME

WORKDIR $HOME

ENTRYPOINT ["/tini", "--"]

COPY [ ".", "hrpurge/" ]

RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers && \
    pip install --no-cache-dir -e ./hrpurge && \
    python -m compileall hrpurge/hrpurge && \
    apk del .tmp

USER python

CMD [ "hrpurge" ]
