# Script generated with Bloom
pkgdesc="ROS - This includes a suite of programs demo'ing various aspects of the ecl_core. It also includes various benchmarking and utility programs for use primarily with embedded systems."
url='http://wiki.ros.org/ecl_core_apps'

pkgname='ros-kinetic-ecl-core-apps'
pkgver='0.61.17_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin'
'ros-kinetic-ecl-build'
'ros-kinetic-ecl-command-line'
'ros-kinetic-ecl-config'
'ros-kinetic-ecl-containers'
'ros-kinetic-ecl-converters'
'ros-kinetic-ecl-devices'
'ros-kinetic-ecl-errors'
'ros-kinetic-ecl-exceptions'
'ros-kinetic-ecl-formatters'
'ros-kinetic-ecl-geometry'
'ros-kinetic-ecl-ipc'
'ros-kinetic-ecl-license'
'ros-kinetic-ecl-linear-algebra'
'ros-kinetic-ecl-sigslots'
'ros-kinetic-ecl-streams'
'ros-kinetic-ecl-threads'
'ros-kinetic-ecl-time-lite'
'ros-kinetic-ecl-type-traits'
)

depends=('ros-kinetic-ecl-build'
'ros-kinetic-ecl-command-line'
'ros-kinetic-ecl-config'
'ros-kinetic-ecl-containers'
'ros-kinetic-ecl-converters'
'ros-kinetic-ecl-devices'
'ros-kinetic-ecl-errors'
'ros-kinetic-ecl-exceptions'
'ros-kinetic-ecl-formatters'
'ros-kinetic-ecl-geometry'
'ros-kinetic-ecl-ipc'
'ros-kinetic-ecl-license'
'ros-kinetic-ecl-linear-algebra'
'ros-kinetic-ecl-sigslots'
'ros-kinetic-ecl-streams'
'ros-kinetic-ecl-threads'
'ros-kinetic-ecl-time-lite'
'ros-kinetic-ecl-type-traits'
)

conflicts=()
replaces=()

_dir=ecl_core_apps
source=()
md5sums=()

prepare() {
    cp -R $startdir/ecl_core_apps $srcdir/ecl_core_apps
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

