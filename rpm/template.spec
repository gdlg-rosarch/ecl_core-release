Name:           ros-indigo-ecl-linear-algebra
Version:        0.61.1
Release:        0%{?dist}
Summary:        ROS ecl_linear_algebra package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/ecl_linear_algebra
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-ecl-eigen
Requires:       ros-indigo-ecl-exceptions
Requires:       ros-indigo-ecl-formatters
Requires:       ros-indigo-ecl-license
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-ecl-eigen
BuildRequires:  ros-indigo-ecl-exceptions
BuildRequires:  ros-indigo-ecl-formatters
BuildRequires:  ros-indigo-ecl-license

%description
Ecl frontend to a linear matrix package (currently eigen).

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Wed Jul 22 2015 Daniel Stonier <d.stonier@gmail.com> - 0.61.1-0
- Autogenerated by Bloom

* Fri Sep 12 2014 Daniel Stonier <d.stonier@gmail.com> - 0.61.0-0
- Autogenerated by Bloom

