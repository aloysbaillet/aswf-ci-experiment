# Docker and Conan experiments for the ASWF
Build and Deploy status on CircleCI: [![CircleCI](https://circleci.com/gh/aloysbaillet/aswf-ci-experiment.svg?style=svg)](https://circleci.com/gh/aloysbaillet/aswf-ci-experiment)

## Docker images

The docker image tagged [aloysbaillet/aswf-vfx2018](docker/aswf-vfx2018/Dockerfile) is based on the `centos/devtoolset-6-toolchain-centos7` image and adds all required development packages to build packages such as Qt.

The docker image tagged [aloysbaillet/aswf-vfx2018-conan](docker/aswf-vfx2018-conan/Dockerfile) is based on the `aloysbaillet/aswf-vfx2018` image and just adds a [Conan](https://conan.io) installation with some pre-defined settings stored there: `docker/aswf-vfx2018-conan/config`.

The prebuilt docker images are published on DockerHub and can be used to build VFX-Platform compliant packages.


## Conan Packages

The Conan recipes in the `conan` folder are a mix of copies of pre-existing conan recipes from the [Conan Community](https://github.com/conan-community) (with their own licenses preserved) and some custom built ones.

### Usage

First install Conan: https://docs.conan.io/en/latest/installation.html and update your `.conan/settings.yaml` with added linux versions as specified [there](https://github.com/aloysbaillet/aswf-ci-experiment/blob/master/docker/aswf-vfx2018-conan/config/settings.yml#L20).

Or you can use the prebuilt docker image that contains a pre-installed and pre-configured conan. See below for Docker image usage instructions.

Then you need to install the shared conan configuration which contains the VFX2018 settings and the following temporary remote: https://api.bintray.com/conan/aloysbaillet/aswftest :
```
conan config install https://github.com/aloysbaillet/aswf-ci-experiment/raw/master/conan_config.zip
```

To build a package that requires any of the existing Conan packages, simply create a `conanfile.txt` such as:
```
[requires]
boost/1.61.0@aswf/vfx2018
numpy/1.12.1@aswf/vfx2018
IlmBase/2.2.0@aswf/vfx2018

[generators]
cmake_paths
virtualenv
virtualrunenv
```

Then run 
```conan install .```
to download and install all required packages in the current folder.

The `cmake_paths` "generator" will instruct Conan to generate a `conan_paths.cmake` file that can be used as a toolchain file so you can run:
```
cmake . -DCMAKE_TOOLCHAIN_FILE=conan_paths.cmake
```
To activate any environment variables required by the package you can run the following lines:
```
source activate.sh
source activate_run.sh
```

### Development

To create and test conan packages, use the docker images and mount the current folder as shown in this [document](conan/README.md).
