# Script generated with Bloom
pkgdesc="ROS - A set of tools and interfaces extending the capabilities of c++ to provide a lightweight, consistent interface with a focus for control programming."
url='http://www.ros.org/wiki/ecl_core'

pkgname='ros-kinetic-ecl-core'
pkgver='0.61.17_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin'
)

depends=('ros-kinetic-ecl-command-line'
'ros-kinetic-ecl-concepts'
'ros-kinetic-ecl-containers'
'ros-kinetic-ecl-converters'
'ros-kinetic-ecl-core-apps'
'ros-kinetic-ecl-devices'
'ros-kinetic-ecl-eigen'
'ros-kinetic-ecl-exceptions'
'ros-kinetic-ecl-formatters'
'ros-kinetic-ecl-geometry'
'ros-kinetic-ecl-ipc'
'ros-kinetic-ecl-linear-algebra'
'ros-kinetic-ecl-math'
'ros-kinetic-ecl-mpl'
'ros-kinetic-ecl-sigslots'
'ros-kinetic-ecl-statistics'
'ros-kinetic-ecl-streams'
'ros-kinetic-ecl-threads'
'ros-kinetic-ecl-time'
'ros-kinetic-ecl-type-traits'
'ros-kinetic-ecl-utilities'
)

conflicts=()
replaces=()

_dir=ecl_core
source=()
md5sums=()

prepare() {
    cp -R $startdir/ecl_core $srcdir/ecl_core
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

