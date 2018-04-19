# Script generated with Bloom
pkgdesc="ROS - These are lightweight text streaming classes that connect to standardised ecl type devices."
url='http://wiki.ros.org/ecl_streams'

pkgname='ros-kinetic-ecl-streams'
pkgver='0.61.17_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin'
'ros-kinetic-ecl-concepts'
'ros-kinetic-ecl-converters'
'ros-kinetic-ecl-devices'
'ros-kinetic-ecl-errors'
'ros-kinetic-ecl-license'
'ros-kinetic-ecl-time'
'ros-kinetic-ecl-type-traits'
)

depends=('ros-kinetic-ecl-concepts'
'ros-kinetic-ecl-converters'
'ros-kinetic-ecl-devices'
'ros-kinetic-ecl-errors'
'ros-kinetic-ecl-license'
'ros-kinetic-ecl-time'
'ros-kinetic-ecl-type-traits'
)

conflicts=()
replaces=()

_dir=ecl_streams
source=()
md5sums=()

prepare() {
    cp -R $startdir/ecl_streams $srcdir/ecl_streams
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

