FROM aloysbaillet/aswf-vfx2018

# Conan
RUN sudo pip install conan
ADD config /tmp/conan-config
RUN conan config install /tmp/conan-config
