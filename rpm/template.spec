Name:           ros-indigo-ecl-command-line
Version:        0.61.18
Release:        0%{?dist}
Summary:        ROS ecl_command_line package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/ecl_command_line
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-ecl-license
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-ecl-license

%description
Embeds the TCLAP library inside the ecl. This is a very convenient command line
parser in templatised c++.

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
        -DCMAKE_INSTALL_LIBDIR="lib" \
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
* Mon Jun 26 2017 Daniel Stonier <d.stonier@gmail.com> - 0.61.18-0
- Autogenerated by Bloom

* Sun Feb 05 2017 Daniel Stonier <d.stonier@gmail.com> - 0.61.17-0
- Autogenerated by Bloom

* Wed Nov 09 2016 Daniel Stonier <d.stonier@gmail.com> - 0.61.15-0
- Autogenerated by Bloom

* Thu Jun 16 2016 Daniel Stonier <d.stonier@gmail.com> - 0.61.14-0
- Autogenerated by Bloom

* Tue Feb 23 2016 Daniel Stonier <d.stonier@gmail.com> - 0.61.9-0
- Autogenerated by Bloom

* Sun Jan 10 2016 Daniel Stonier <d.stonier@gmail.com> - 0.61.8-0
- Autogenerated by Bloom

* Sat Jan 09 2016 Daniel Stonier <d.stonier@gmail.com> - 0.61.7-0
- Autogenerated by Bloom

* Wed Jan 06 2016 Daniel Stonier <d.stonier@gmail.com> - 0.61.6-1
- Autogenerated by Bloom

* Tue Nov 24 2015 Daniel Stonier <d.stonier@gmail.com> - 0.61.5-0
- Autogenerated by Bloom

* Sat Oct 10 2015 Daniel Stonier <d.stonier@gmail.com> - 0.61.4-0
- Autogenerated by Bloom

* Sat Sep 05 2015 Daniel Stonier <d.stonier@gmail.com> - 0.61.3-0
- Autogenerated by Bloom

* Wed Aug 12 2015 Daniel Stonier <d.stonier@gmail.com> - 0.61.2-0
- Autogenerated by Bloom

* Wed Jul 22 2015 Daniel Stonier <d.stonier@gmail.com> - 0.61.1-0
- Autogenerated by Bloom

* Fri Sep 12 2014 Daniel Stonier <d.stonier@gmail.com> - 0.61.0-0
- Autogenerated by Bloom

