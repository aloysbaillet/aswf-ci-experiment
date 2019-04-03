# Simple Python Demo

This has been tested within the centos-7 docker containers and Ubuntu workstations.

To install dependencies:
```
mkdir build
cd build
conan install .. --profile vfx2018
```

To run:
```
source activate.sh
source activate_run.sh
python2.7 ../main.py
```
