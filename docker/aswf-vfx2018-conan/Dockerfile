FROM aloysbaillet/aswf-vfx2018

# Conan
RUN sudo pip install conan
ADD config /tmp/_conan-config

ENV CONAN_USER_HOME=/tmp
RUN conan config install /tmp/_conan-config && \
    chmod a+rw -R ${CONAN_USER_HOME}/.conan
