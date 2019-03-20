FROM centos/devtoolset-6-toolchain-centos7
LABEL com.vfxplatform.version="CY2018"

ENV ASWF_BUILD_DIR /tmp/vfx-build
ENV ASWF_ROOT_DIR /opt/aswf/vfx2018

USER root

RUN mkdir -p $ASWF_BUILD_DIR && \
    mkdir -p $ASWF_ROOT_DIR

RUN yum install -y \
    bzip2-devel \
    file \
    make \
    python-devel \
    which \
    zlib-devel \
    git \
    ca-certificates \
    ssh \
    sudo && \
    yum clean all

RUN curl --location "https://github.com/Kitware/CMake/releases/download/v3.14.0/cmake-3.14.0-Linux-x86_64.sh" -o "cmake.sh" &&\
    sh cmake.sh --skip-license

RUN curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py" &&\
    python get-pip.py

RUN pip install \
    numpy==1.12.1

ENV HOME /home/circleci
RUN groupadd -r circleci && useradd -r -d ${HOME} -m -g circleci circleci
RUN echo "%circleci        ALL=(ALL)       NOPASSWD: ALL" >> /etc/sudoers
USER circleci

RUN mkdir -p ${HOME}/.ssh && ssh-keyscan -t rsa github.com >> ${HOME}/.ssh/known_hosts

# Conan
RUN sudo pip install conan
ADD config /tmp/conan-config
RUN conan config install /tmp/conan-config

WORKDIR $ASWF_ROOT_DIR
