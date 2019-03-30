FROM centos/devtoolset-6-toolchain-centos7
LABEL com.vfxplatform.version="CY2018"

USER root

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
    sudo \
    openssl-devel \
    libxcb libxcb-devel \
    libXrender libXrender-devel \
    xcb-util-wm xcb-util-wm-devel \
    xcb-util xcb-util-devel \
    xcb-util-image xcb-util-image-devel \
    xcb-util-keysyms xcb-util-keysyms-devel \
    pulseaudio-libs-devel \
    gperf \
    ruby \
    libcap-devel \
    libXtst-devel \
    pciutils-devel \
    bison \
    libv4l libv4l-devel \
    libcap-devel \
    mesa-libGL-devel \
    mesa-libEGL-devel \
    libxml2 libxml2-devel \
    libxslt libxslt-devel \
    nss nss-devel \
    dbus dbus-devel \
    fontconfig fontconfig-devel \
    freetype freetype-devel \
    ncurses ncurses-devel \
    readline readline-devel \
    libpng libpng-devel \
    libjpeg libjpeg-devel \
    libXrandr libXrandr-devel \
    libXcomposite libXcomposite-devel \
    libXScrnSaver libXScrnSaver-devel \
    libXcursor libXcursor-devel \
    libXp libXp-devel \
    libXpm libXpm-devel \
    libXmu libXmu-devel \
    libXi libXi-devel \
    glut-devel \
    pulseaudio-libs pulseaudio-libs-devel \
    alsa-lib alsa-lib-devel \
    tcsh \
    fam \
    wget \
    && \
    yum clean all

RUN curl --location "https://github.com/Kitware/CMake/releases/download/v3.14.0/cmake-3.14.0-Linux-x86_64.sh" -o "cmake.sh" &&\
    sh cmake.sh --skip-license

RUN wget https://github.com/ninja-build/ninja/releases/download/v1.9.0/ninja-linux.zip -O /tmp/ninja.zip && \
    sudo unzip /tmp/ninja.zip -d /usr/bin && \
    rm /tmp/ninja.zip && \
    sudo chmod a+x /usr/bin/ninja

RUN curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py" &&\
    python get-pip.py

RUN pip install \
    nose

ENV HOME /home/circleci
RUN groupadd -r circleci && useradd -r -d ${HOME} -m -g circleci circleci
RUN echo "%circleci        ALL=(ALL)       NOPASSWD: ALL" >> /etc/sudoers
USER circleci

RUN mkdir -p ${HOME}/.ssh && ssh-keyscan -t rsa github.com >> ${HOME}/.ssh/known_hosts

#WORKDIR /home/circleci/project
