# Script generated with Bloom
pkgdesc="ROS - Timing utilities are very dependent on the system api provided for their use. This package provides a means for handling different timing models. Current support - posix rt : complete. - macosx : posix timers only, missing absolute timers. - win : none."
url='http://wiki.ros.org/ecl_time'

pkgname='ros-kinetic-ecl-time'
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
'ros-kinetic-ecl-time-lite'
)

depends=('ros-kinetic-ecl-build'
'ros-kinetic-ecl-config'
'ros-kinetic-ecl-errors'
'ros-kinetic-ecl-exceptions'
'ros-kinetic-ecl-license'
'ros-kinetic-ecl-time-lite'
)

conflicts=()
replaces=()

_dir=ecl_time
source=()
md5sums=()

prepare() {
    cp -R $startdir/ecl_time $srcdir/ecl_time
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

