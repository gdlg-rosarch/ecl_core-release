# Script generated with Bloom
pkgdesc="ROS - Interprocess mechanisms vary greatly across platforms - sysv, posix, win32, there are more than a few. This package provides an infrastructure to allow for developing cross platform c++ wrappers around the lower level c api's that handle these mechanisms. These make it not only easier to utilise such mechanisms, but allow it to be done consistently across platforms."
url='http://wiki.ros.org/ecl_ipc'

pkgname='ros-kinetic-ecl-ipc'
pkgver='0.61.17_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin'
'ros-kinetic-ecl-build'
'ros-kinetic-ecl-config'
'ros-kinetic-ecl-errors'
'ros-kinetic-ecl-exceptions'
'ros-kinetic-ecl-license'
'ros-kinetic-ecl-time'
'ros-kinetic-ecl-time-lite'
)

depends=('ros-kinetic-ecl-build'
'ros-kinetic-ecl-config'
'ros-kinetic-ecl-errors'
'ros-kinetic-ecl-exceptions'
'ros-kinetic-ecl-license'
'ros-kinetic-ecl-time'
'ros-kinetic-ecl-time-lite'
)

conflicts=()
replaces=()

_dir=ecl_ipc
source=()
md5sums=()

prepare() {
    cp -R $startdir/ecl_ipc $srcdir/ecl_ipc
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

