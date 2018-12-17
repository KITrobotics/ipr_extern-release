Name:           ros-melodic-libmodbus
Version:        0.8.8
Release:        0%{?dist}
Summary:        ROS libmodbus package

Group:          Development/Libraries
License:        LGPLv3
URL:            http://wiki.ros.org/iirob_controllers
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-melodic-cmake-modules
BuildRequires:  ros-melodic-catkin
BuildRequires:  ros-melodic-cmake-modules

%description
The iirob_filters package implements following filters: 1) Low-Pass 2) Moving
Mean 3) Gravity Compensation (used for force-torque sensors) 4) Threshold Filter

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/melodic

%changelog
* Mon Dec 17 2018 Denis Štogl <denis.stogl@kit.edu> - 0.8.8-0
- Autogenerated by Bloom

