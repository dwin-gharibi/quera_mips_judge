FROM registry.gitlab.com/qio/standard/ubuntu:20.04

RUN apt-get update && \
    yes | unminimize && \
    apt-get -y install \
        openssh-server \
        passwd \
        sudo \
        man-db \
        nasm \
        libc6-dev-i386 \
        curl \
        wget \
        spim \
        vim-tiny && \
    apt-get -qq clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

WORKDIR /workspace

CMD ["tail", "-f", "/dev/null"]