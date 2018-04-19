# Script generated with Bloom
pkgdesc="ROS - This package provides the c++ extensions for a variety of threaded programming tools. These are usually different on different platforms, so the architecture for a cross-platform framework is also implemented."
url='http://wiki.ros.org/ecl_threads'

pkgname='ros-kinetic-ecl-threads'
pkgver='0.61.17_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin'
'ros-kinetic-ecl-build'
'ros-kinetic-ecl-concepts'
'ros-kinetic-ecl-config'
'ros-kinetic-ecl-errors'
'ros-kinetic-ecl-exceptions'
'ros-kinetic-ecl-license'
'ros-kinetic-ecl-time'
'ros-kinetic-ecl-utilities'
)

depends=('ros-kinetic-ecl-build'
'ros-kinetic-ecl-concepts'
'ros-kinetic-ecl-config'
'ros-kinetic-ecl-errors'
'ros-kinetic-ecl-exceptions'
'ros-kinetic-ecl-license'
'ros-kinetic-ecl-time'
'ros-kinetic-ecl-utilities'
)

conflicts=()
replaces=()

_dir=ecl_threads
source=()
md5sums=()

prepare() {
    cp -R $startdir/ecl_threads $srcdir/ecl_threads
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

