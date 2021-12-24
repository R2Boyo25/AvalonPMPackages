owd="$(pwd)"
cd $3
mkdir build && cd build
cmake $owd -DCMAKE_INSTALL_PREFIX=$3 -DCMAKE_BUILD_TYPE=Debug -DKRITA_DEVS=ON
make -j`nproc`
make install -j`nproc`