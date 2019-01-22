#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : kstars
Version  : 2.9.8
Release  : 1
URL      : https://github.com/KDE/kstars/archive/v2.9.8.tar.gz
Source0  : https://github.com/KDE/kstars/archive/v2.9.8.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause CC-BY-SA-4.0 GFDL-1.2 GPL-2.0 SGI-B-2.0
Requires: kstars-bin = %{version}-%{release}
Requires: kstars-data = %{version}-%{release}
Requires: kstars-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-cpan
BuildRequires : buildreq-kde
BuildRequires : cfitsio-dev
BuildRequires : eigen-dev
BuildRequires : glibc-dev
BuildRequires : gsl-dev
BuildRequires : knotifyconfig-dev
BuildRequires : kplotting-dev
BuildRequires : mesa-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(libraw)
BuildRequires : pkgconfig(libraw_r)
BuildRequires : pkgconfig(wcslib)
BuildRequires : qtbase-dev mesa-dev
BuildRequires : zlib-dev

%description
*****************************************************
**   KStars 2.7.9: A Desktop Planetarium for KDE   **
*****************************************************

%package bin
Summary: bin components for the kstars package.
Group: Binaries
Requires: kstars-data = %{version}-%{release}
Requires: kstars-license = %{version}-%{release}

%description bin
bin components for the kstars package.


%package data
Summary: data components for the kstars package.
Group: Data

%description data
data components for the kstars package.


%package doc
Summary: doc components for the kstars package.
Group: Documentation

%description doc
doc components for the kstars package.


%package license
Summary: license components for the kstars package.
Group: Default

%description license
license components for the kstars package.


%prep
%setup -q -n kstars-2.9.8

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1548187277
mkdir -p clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags} VERBOSE=1
popd

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
cd clr-build; make test

%install
export SOURCE_DATE_EPOCH=1548187277
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kstars
cp COPYING %{buildroot}/usr/share/package-licenses/kstars/COPYING
cp COPYING.DOC %{buildroot}/usr/share/package-licenses/kstars/COPYING.DOC
cp LICENSE_OpenNGC %{buildroot}/usr/share/package-licenses/kstars/LICENSE_OpenNGC
cp cmake/modules/COPYING-CMAKE-SCRIPTS %{buildroot}/usr/share/package-licenses/kstars/cmake_modules_COPYING-CMAKE-SCRIPTS
cp kstars/libtess/src/LICENSE %{buildroot}/usr/share/package-licenses/kstars/kstars_libtess_src_LICENSE
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)
/usr/lib64/libexec/kauth/kauth_kstars_helper

%files bin
%defattr(-,root,root,-)
/usr/bin/kstars

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.kstars.desktop
/usr/share/config.kcfg/kstars.kcfg
/usr/share/dbus-1/system-services/org.kde.kf5auth.kstars.service
/usr/share/dbus-1/system.d/org.kde.kf5auth.kstars.conf
/usr/share/icons/hicolor/128x128/apps/kstars.png
/usr/share/icons/hicolor/16x16/apps/kstars.png
/usr/share/icons/hicolor/32x32/apps/kstars.png
/usr/share/icons/hicolor/48x48/apps/kstars.png
/usr/share/icons/hicolor/64x64/apps/kstars.png
/usr/share/icons/hicolor/scalable/apps/kstars.svgz
/usr/share/knotifications5/kstars.notifyrc
/usr/share/kstars/Henry-Draper.idx
/usr/share/kstars/Interesting.dat
/usr/share/kstars/PlanetFacts.dat
/usr/share/kstars/TZrules.dat
/usr/share/kstars/advinterface.dat
/usr/share/kstars/asteroids.dat
/usr/share/kstars/catalog.min.json
/usr/share/kstars/cbounds-3.idx
/usr/share/kstars/cbounds-4.idx
/usr/share/kstars/cbounds-5.idx
/usr/share/kstars/cbounds-6.idx
/usr/share/kstars/cbounds.dat
/usr/share/kstars/chart.colors
/usr/share/kstars/citydb.sqlite
/usr/share/kstars/classic.colors
/usr/share/kstars/clines.dat
/usr/share/kstars/cnames.dat
/usr/share/kstars/comets.dat
/usr/share/kstars/defaultflag.gif
/usr/share/kstars/earth.B0.vsop
/usr/share/kstars/earth.B1.vsop
/usr/share/kstars/earth.B2.vsop
/usr/share/kstars/earth.B3.vsop
/usr/share/kstars/earth.B4.vsop
/usr/share/kstars/earth.B5.vsop
/usr/share/kstars/earth.L0.vsop
/usr/share/kstars/earth.L1.vsop
/usr/share/kstars/earth.L2.vsop
/usr/share/kstars/earth.L3.vsop
/usr/share/kstars/earth.L4.vsop
/usr/share/kstars/earth.L5.vsop
/usr/share/kstars/earth.R0.vsop
/usr/share/kstars/earth.R1.vsop
/usr/share/kstars/earth.R2.vsop
/usr/share/kstars/earth.R3.vsop
/usr/share/kstars/earth.R4.vsop
/usr/share/kstars/earth.R5.vsop
/usr/share/kstars/earth.orbit
/usr/share/kstars/ekoslive.png
/usr/share/kstars/geomap.png
/usr/share/kstars/glossary.xml
/usr/share/kstars/image_url.dat
/usr/share/kstars/indidrivers.xml
/usr/share/kstars/info_url.dat
/usr/share/kstars/jupiter.B0.vsop
/usr/share/kstars/jupiter.B1.vsop
/usr/share/kstars/jupiter.B2.vsop
/usr/share/kstars/jupiter.B3.vsop
/usr/share/kstars/jupiter.B4.vsop
/usr/share/kstars/jupiter.B5.vsop
/usr/share/kstars/jupiter.L0.vsop
/usr/share/kstars/jupiter.L1.vsop
/usr/share/kstars/jupiter.L2.vsop
/usr/share/kstars/jupiter.L3.vsop
/usr/share/kstars/jupiter.L4.vsop
/usr/share/kstars/jupiter.L5.vsop
/usr/share/kstars/jupiter.R0.vsop
/usr/share/kstars/jupiter.R1.vsop
/usr/share/kstars/jupiter.R2.vsop
/usr/share/kstars/jupiter.R3.vsop
/usr/share/kstars/jupiter.R4.vsop
/usr/share/kstars/jupiter.R5.vsop
/usr/share/kstars/jupiter.orbit
/usr/share/kstars/kstars.png
/usr/share/kstars/kstarslite/qml/constants/Constants.qml
/usr/share/kstars/kstarslite/qml/constants/qmldir
/usr/share/kstars/kstarslite/qml/dialogs/AboutDialog.qml
/usr/share/kstars/kstarslite/qml/dialogs/DetailsDialog.qml
/usr/share/kstars/kstarslite/qml/dialogs/FindDialog.qml
/usr/share/kstars/kstarslite/qml/dialogs/LocationDialog.qml
/usr/share/kstars/kstarslite/qml/dialogs/helpers/DetailsAddLink.qml
/usr/share/kstars/kstarslite/qml/dialogs/helpers/DetailsItem.qml
/usr/share/kstars/kstarslite/qml/dialogs/helpers/LocationEdit.qml
/usr/share/kstars/kstarslite/qml/dialogs/helpers/LocationLoading.qml
/usr/share/kstars/kstarslite/qml/dialogs/menus/DetailsLinkMenu.qml
/usr/share/kstars/kstarslite/qml/dialogs/menus/LocationsGeoMenu.qml
/usr/share/kstars/kstarslite/qml/images/appointment-new.png
/usr/share/kstars/kstarslite/qml/images/appointment-new@2x.png
/usr/share/kstars/kstarslite/qml/images/appointment-new@3x.png
/usr/share/kstars/kstarslite/qml/images/appointment-new@4x.png
/usr/share/kstars/kstarslite/qml/images/arrow-down.png
/usr/share/kstars/kstarslite/qml/images/arrow-down@2x.png
/usr/share/kstars/kstarslite/qml/images/arrow-down@3x.png
/usr/share/kstars/kstarslite/qml/images/arrow-down@4x.png
/usr/share/kstars/kstarslite/qml/images/arrow-up.png
/usr/share/kstars/kstarslite/qml/images/arrow-up@2x.png
/usr/share/kstars/kstarslite/qml/images/arrow-up@3x.png
/usr/share/kstars/kstarslite/qml/images/arrow-up@4x.png
/usr/share/kstars/kstarslite/qml/images/arrow.png
/usr/share/kstars/kstarslite/qml/images/arrow@2x.png
/usr/share/kstars/kstarslite/qml/images/arrow@3x.png
/usr/share/kstars/kstarslite/qml/images/arrow@4x.png
/usr/share/kstars/kstarslite/qml/images/back.png
/usr/share/kstars/kstarslite/qml/images/back@2x.png
/usr/share/kstars/kstarslite/qml/images/back@3x.png
/usr/share/kstars/kstarslite/qml/images/back@4x.png
/usr/share/kstars/kstarslite/qml/images/draw-star.png
/usr/share/kstars/kstarslite/qml/images/draw-star@2x.png
/usr/share/kstars/kstarslite/qml/images/draw-star@3x.png
/usr/share/kstars/kstarslite/qml/images/draw-star@4x.png
/usr/share/kstars/kstarslite/qml/images/edit-find.png
/usr/share/kstars/kstarslite/qml/images/edit-find@2x.png
/usr/share/kstars/kstarslite/qml/images/edit-find@3x.png
/usr/share/kstars/kstarslite/qml/images/edit-find@4x.png
/usr/share/kstars/kstarslite/qml/images/kde-logo.png
/usr/share/kstars/kstarslite/qml/images/kde-logo@2x.png
/usr/share/kstars/kstarslite/qml/images/kde-logo@3x.png
/usr/share/kstars/kstarslite/qml/images/kde-logo@4x.png
/usr/share/kstars/kstarslite/qml/images/kstars.png
/usr/share/kstars/kstarslite/qml/images/kstars_automode.png
/usr/share/kstars/kstarslite/qml/images/kstars_automode@2x.png
/usr/share/kstars/kstarslite/qml/images/kstars_automode@3x.png
/usr/share/kstars/kstarslite/qml/images/kstars_automode@4x.png
/usr/share/kstars/kstarslite/qml/images/kstars_cbound.png
/usr/share/kstars/kstarslite/qml/images/kstars_cbound@2x.png
/usr/share/kstars/kstarslite/qml/images/kstars_cbound@3x.png
/usr/share/kstars/kstarslite/qml/images/kstars_cbound@4x.png
/usr/share/kstars/kstarslite/qml/images/kstars_clines.png
/usr/share/kstars/kstarslite/qml/images/kstars_clines@2x.png
/usr/share/kstars/kstarslite/qml/images/kstars_clines@3x.png
/usr/share/kstars/kstarslite/qml/images/kstars_clines@4x.png
/usr/share/kstars/kstarslite/qml/images/kstars_cnames.png
/usr/share/kstars/kstarslite/qml/images/kstars_cnames@2x.png
/usr/share/kstars/kstarslite/qml/images/kstars_cnames@3x.png
/usr/share/kstars/kstarslite/qml/images/kstars_cnames@4x.png
/usr/share/kstars/kstarslite/qml/images/kstars_constellationart.png
/usr/share/kstars/kstarslite/qml/images/kstars_constellationart@2x.png
/usr/share/kstars/kstarslite/qml/images/kstars_constellationart@3x.png
/usr/share/kstars/kstarslite/qml/images/kstars_constellationart@4x.png
/usr/share/kstars/kstarslite/qml/images/kstars_deepsky.png
/usr/share/kstars/kstarslite/qml/images/kstars_deepsky@2x.png
/usr/share/kstars/kstarslite/qml/images/kstars_deepsky@3x.png
/usr/share/kstars/kstarslite/qml/images/kstars_deepsky@4x.png
/usr/share/kstars/kstarslite/qml/images/kstars_ekos.png
/usr/share/kstars/kstarslite/qml/images/kstars_ekos@2x.png
/usr/share/kstars/kstarslite/qml/images/kstars_ekos@3x.png
/usr/share/kstars/kstarslite/qml/images/kstars_ekos@4x.png
/usr/share/kstars/kstarslite/qml/images/kstars_fitsviewer.png
/usr/share/kstars/kstarslite/qml/images/kstars_fitsviewer@2x.png
/usr/share/kstars/kstarslite/qml/images/kstars_fitsviewer@3x.png
/usr/share/kstars/kstarslite/qml/images/kstars_fitsviewer@4x.png
/usr/share/kstars/kstarslite/qml/images/kstars_grid.png
/usr/share/kstars/kstarslite/qml/images/kstars_grid@2x.png
/usr/share/kstars/kstarslite/qml/images/kstars_grid@3x.png
/usr/share/kstars/kstarslite/qml/images/kstars_grid@4x.png
/usr/share/kstars/kstarslite/qml/images/kstars_guides.png
/usr/share/kstars/kstarslite/qml/images/kstars_guides@2x.png
/usr/share/kstars/kstarslite/qml/images/kstars_guides@3x.png
/usr/share/kstars/kstarslite/qml/images/kstars_guides@4x.png
/usr/share/kstars/kstarslite/qml/images/kstars_hgrid.png
/usr/share/kstars/kstarslite/qml/images/kstars_hgrid@2x.png
/usr/share/kstars/kstarslite/qml/images/kstars_hgrid@3x.png
/usr/share/kstars/kstarslite/qml/images/kstars_hgrid@4x.png
/usr/share/kstars/kstarslite/qml/images/kstars_horizon.png
/usr/share/kstars/kstarslite/qml/images/kstars_horizon@2x.png
/usr/share/kstars/kstarslite/qml/images/kstars_horizon@3x.png
/usr/share/kstars/kstarslite/qml/images/kstars_horizon@4x.png
/usr/share/kstars/kstarslite/qml/images/kstars_indi.png
/usr/share/kstars/kstarslite/qml/images/kstars_indi@2x.png
/usr/share/kstars/kstarslite/qml/images/kstars_indi@3x.png
/usr/share/kstars/kstarslite/qml/images/kstars_indi@4x.png
/usr/share/kstars/kstarslite/qml/images/kstars_mw.png
/usr/share/kstars/kstarslite/qml/images/kstars_mw@2x.png
/usr/share/kstars/kstarslite/qml/images/kstars_mw@3x.png
/usr/share/kstars/kstarslite/qml/images/kstars_mw@4x.png
/usr/share/kstars/kstarslite/qml/images/kstars_planets.png
/usr/share/kstars/kstarslite/qml/images/kstars_planets@2x.png
/usr/share/kstars/kstarslite/qml/images/kstars_planets@3x.png
/usr/share/kstars/kstarslite/qml/images/kstars_planets@4x.png
/usr/share/kstars/kstarslite/qml/images/kstars_satellites.png
/usr/share/kstars/kstarslite/qml/images/kstars_satellites@2x.png
/usr/share/kstars/kstarslite/qml/images/kstars_satellites@3x.png
/usr/share/kstars/kstarslite/qml/images/kstars_satellites@4x.png
/usr/share/kstars/kstarslite/qml/images/kstars_solarsystem.png
/usr/share/kstars/kstarslite/qml/images/kstars_solarsystem@2x.png
/usr/share/kstars/kstarslite/qml/images/kstars_solarsystem@3x.png
/usr/share/kstars/kstarslite/qml/images/kstars_solarsystem@4x.png
/usr/share/kstars/kstarslite/qml/images/kstars_stars.png
/usr/share/kstars/kstarslite/qml/images/kstars_stars@2x.png
/usr/share/kstars/kstarslite/qml/images/kstars_stars@3x.png
/usr/share/kstars/kstarslite/qml/images/kstars_stars@4x.png
/usr/share/kstars/kstarslite/qml/images/kstars_supernovae.png
/usr/share/kstars/kstarslite/qml/images/kstars_supernovae@2x.png
/usr/share/kstars/kstarslite/qml/images/kstars_supernovae@3x.png
/usr/share/kstars/kstarslite/qml/images/kstars_supernovae@4x.png
/usr/share/kstars/kstarslite/qml/images/left-arrow.png
/usr/share/kstars/kstarslite/qml/images/left-arrow@2x.png
/usr/share/kstars/kstarslite/qml/images/left-arrow@3x.png
/usr/share/kstars/kstarslite/qml/images/left-arrow@4x.png
/usr/share/kstars/kstarslite/qml/images/lock-closed.png
/usr/share/kstars/kstarslite/qml/images/lock-closed@2x.png
/usr/share/kstars/kstarslite/qml/images/lock-closed@3x.png
/usr/share/kstars/kstarslite/qml/images/lock-closed@4x.png
/usr/share/kstars/kstarslite/qml/images/lock-open.png
/usr/share/kstars/kstarslite/qml/images/lock-open@2x.png
/usr/share/kstars/kstarslite/qml/images/lock-open@3x.png
/usr/share/kstars/kstarslite/qml/images/lock-open@4x.png
/usr/share/kstars/kstarslite/qml/images/media-playback-pause.png
/usr/share/kstars/kstarslite/qml/images/media-playback-pause@2x.png
/usr/share/kstars/kstarslite/qml/images/media-playback-pause@3x.png
/usr/share/kstars/kstarslite/qml/images/media-playback-pause@4x.png
/usr/share/kstars/kstarslite/qml/images/media-playback-start.png
/usr/share/kstars/kstarslite/qml/images/media-playback-start@2x.png
/usr/share/kstars/kstarslite/qml/images/media-playback-start@3x.png
/usr/share/kstars/kstarslite/qml/images/media-playback-start@4x.png
/usr/share/kstars/kstarslite/qml/images/media-skip-backward.png
/usr/share/kstars/kstarslite/qml/images/media-skip-backward@2x.png
/usr/share/kstars/kstarslite/qml/images/media-skip-backward@3x.png
/usr/share/kstars/kstarslite/qml/images/media-skip-backward@4x.png
/usr/share/kstars/kstarslite/qml/images/media-skip-forward.png
/usr/share/kstars/kstarslite/qml/images/media-skip-forward@2x.png
/usr/share/kstars/kstarslite/qml/images/media-skip-forward@3x.png
/usr/share/kstars/kstarslite/qml/images/media-skip-forward@4x.png
/usr/share/kstars/kstarslite/qml/images/right-arrow.png
/usr/share/kstars/kstarslite/qml/images/right-arrow@2x.png
/usr/share/kstars/kstarslite/qml/images/right-arrow@3x.png
/usr/share/kstars/kstarslite/qml/images/right-arrow@4x.png
/usr/share/kstars/kstarslite/qml/images/splash.png
/usr/share/kstars/kstarslite/qml/images/splash@2x.png
/usr/share/kstars/kstarslite/qml/images/splash@3x.png
/usr/share/kstars/kstarslite/qml/images/splash@4x.png
/usr/share/kstars/kstarslite/qml/images/splash_bg.jpeg
/usr/share/kstars/kstarslite/qml/images/splash_bg@2x.jpeg
/usr/share/kstars/kstarslite/qml/images/splash_bg@3x.jpeg
/usr/share/kstars/kstarslite/qml/images/splash_bg@4x.jpeg
/usr/share/kstars/kstarslite/qml/images/tutorial-arrow-horizontal.png
/usr/share/kstars/kstarslite/qml/images/tutorial-arrow-horizontal@2x.png
/usr/share/kstars/kstarslite/qml/images/tutorial-arrow-horizontal@3x.png
/usr/share/kstars/kstarslite/qml/images/tutorial-arrow-horizontal@4x.png
/usr/share/kstars/kstarslite/qml/images/tutorial-arrow-vertical.png
/usr/share/kstars/kstarslite/qml/images/tutorial-arrow-vertical@2x.png
/usr/share/kstars/kstarslite/qml/images/tutorial-arrow-vertical@3x.png
/usr/share/kstars/kstarslite/qml/images/tutorial-arrow-vertical@4x.png
/usr/share/kstars/kstarslite/qml/indi/DevicePanel.qml
/usr/share/kstars/kstarslite/qml/indi/INDIControlPanel.qml
/usr/share/kstars/kstarslite/qml/indi/ImagePreview.qml
/usr/share/kstars/kstarslite/qml/indi/modules/KSButtonSwitch.qml
/usr/share/kstars/kstarslite/qml/indi/modules/KSButtonsSwitchRow.qml
/usr/share/kstars/kstarslite/qml/indi/modules/KSCheckBox.qml
/usr/share/kstars/kstarslite/qml/indi/modules/KSINDIText.qml
/usr/share/kstars/kstarslite/qml/indi/modules/KSINDITextField.qml
/usr/share/kstars/kstarslite/qml/indi/modules/KSLed.qml
/usr/share/kstars/kstarslite/qml/indi/modules/Led.qml
/usr/share/kstars/kstarslite/qml/indi/modules/MotionControl.qml
/usr/share/kstars/kstarslite/qml/indi/modules/Property.qml
/usr/share/kstars/kstarslite/qml/indi/modules/images/hdpi/green.png
/usr/share/kstars/kstarslite/qml/indi/modules/images/hdpi/grey.png
/usr/share/kstars/kstarslite/qml/indi/modules/images/hdpi/red.png
/usr/share/kstars/kstarslite/qml/indi/modules/images/hdpi/yellow.png
/usr/share/kstars/kstarslite/qml/indi/modules/images/ldpi/green.png
/usr/share/kstars/kstarslite/qml/indi/modules/images/ldpi/grey.png
/usr/share/kstars/kstarslite/qml/indi/modules/images/ldpi/red.png
/usr/share/kstars/kstarslite/qml/indi/modules/images/ldpi/yellow.png
/usr/share/kstars/kstarslite/qml/indi/modules/images/mdpi/green.png
/usr/share/kstars/kstarslite/qml/indi/modules/images/mdpi/grey.png
/usr/share/kstars/kstarslite/qml/indi/modules/images/mdpi/red.png
/usr/share/kstars/kstarslite/qml/indi/modules/images/mdpi/yellow.png
/usr/share/kstars/kstarslite/qml/indi/modules/images/xhdpi/green.png
/usr/share/kstars/kstarslite/qml/indi/modules/images/xhdpi/grey.png
/usr/share/kstars/kstarslite/qml/indi/modules/images/xhdpi/red.png
/usr/share/kstars/kstarslite/qml/indi/modules/images/xhdpi/yellow.png
/usr/share/kstars/kstarslite/qml/indi/modules/images/xxhdpi/green.png
/usr/share/kstars/kstarslite/qml/indi/modules/images/xxhdpi/grey.png
/usr/share/kstars/kstarslite/qml/indi/modules/images/xxhdpi/red.png
/usr/share/kstars/kstarslite/qml/indi/modules/images/xxhdpi/yellow.png
/usr/share/kstars/kstarslite/qml/indi/modules/images/xxxhdpi/green.png
/usr/share/kstars/kstarslite/qml/indi/modules/images/xxxhdpi/grey.png
/usr/share/kstars/kstarslite/qml/indi/modules/images/xxxhdpi/red.png
/usr/share/kstars/kstarslite/qml/indi/modules/images/xxxhdpi/yellow.png
/usr/share/kstars/kstarslite/qml/main.qml
/usr/share/kstars/kstarslite/qml/modules/BottomMenu.qml
/usr/share/kstars/kstarslite/qml/modules/KSButton.qml
/usr/share/kstars/kstarslite/qml/modules/KSLabel.qml
/usr/share/kstars/kstarslite/qml/modules/KSListView.qml
/usr/share/kstars/kstarslite/qml/modules/KSPage.qml
/usr/share/kstars/kstarslite/qml/modules/KSTab.qml
/usr/share/kstars/kstarslite/qml/modules/KSTabBarArrow.qml
/usr/share/kstars/kstarslite/qml/modules/KSTabButton.qml
/usr/share/kstars/kstarslite/qml/modules/KSText.qml
/usr/share/kstars/kstarslite/qml/modules/KSTextField.qml
/usr/share/kstars/kstarslite/qml/modules/SkyMapLiteWrapper.qml
/usr/share/kstars/kstarslite/qml/modules/Splash.qml
/usr/share/kstars/kstarslite/qml/modules/TimePage.qml
/usr/share/kstars/kstarslite/qml/modules/TopMenu.qml
/usr/share/kstars/kstarslite/qml/modules/helpers/BottomMenuButton.qml
/usr/share/kstars/kstarslite/qml/modules/helpers/KSMenuItem.qml
/usr/share/kstars/kstarslite/qml/modules/helpers/PassiveNotification.qml
/usr/share/kstars/kstarslite/qml/modules/helpers/TelescopeControl.qml
/usr/share/kstars/kstarslite/qml/modules/helpers/TimeSpinBox.qml
/usr/share/kstars/kstarslite/qml/modules/helpers/TopMenuButton.qml
/usr/share/kstars/kstarslite/qml/modules/helpers/Units.qml
/usr/share/kstars/kstarslite/qml/modules/menus/ContextMenu.qml
/usr/share/kstars/kstarslite/qml/modules/popups/ColorSchemePopup.qml
/usr/share/kstars/kstarslite/qml/modules/popups/FOVPopup.qml
/usr/share/kstars/kstarslite/qml/modules/popups/ProjectionsPopup.qml
/usr/share/kstars/kstarslite/qml/modules/tutorial/TutorialExitPopup.qml
/usr/share/kstars/kstarslite/qml/modules/tutorial/TutorialPane.qml
/usr/share/kstars/kstarslite/qml/modules/tutorial/TutorialPopup.qml
/usr/share/kstars/kstarslite/qml/modules/tutorial/TutorialStep1.qml
/usr/share/kstars/kstarslite/qml/modules/tutorial/TutorialStep2.qml
/usr/share/kstars/kstarslite/qml/modules/tutorial/TutorialStep3.qml
/usr/share/kstars/kstarslite/qml/modules/tutorial/TutorialStep4.qml
/usr/share/kstars/kstarslite/qml/modules/tutorial/TutorialStep5.qml
/usr/share/kstars/lmc.dat
/usr/share/kstars/mars.B0.vsop
/usr/share/kstars/mars.B1.vsop
/usr/share/kstars/mars.B2.vsop
/usr/share/kstars/mars.B3.vsop
/usr/share/kstars/mars.B4.vsop
/usr/share/kstars/mars.B5.vsop
/usr/share/kstars/mars.L0.vsop
/usr/share/kstars/mars.L1.vsop
/usr/share/kstars/mars.L2.vsop
/usr/share/kstars/mars.L3.vsop
/usr/share/kstars/mars.L4.vsop
/usr/share/kstars/mars.L5.vsop
/usr/share/kstars/mars.R0.vsop
/usr/share/kstars/mars.R1.vsop
/usr/share/kstars/mars.R2.vsop
/usr/share/kstars/mars.R3.vsop
/usr/share/kstars/mars.R4.vsop
/usr/share/kstars/mars.R5.vsop
/usr/share/kstars/mars.orbit
/usr/share/kstars/mercury.B0.vsop
/usr/share/kstars/mercury.B1.vsop
/usr/share/kstars/mercury.B2.vsop
/usr/share/kstars/mercury.B3.vsop
/usr/share/kstars/mercury.B4.vsop
/usr/share/kstars/mercury.B5.vsop
/usr/share/kstars/mercury.L0.vsop
/usr/share/kstars/mercury.L1.vsop
/usr/share/kstars/mercury.L2.vsop
/usr/share/kstars/mercury.L3.vsop
/usr/share/kstars/mercury.L4.vsop
/usr/share/kstars/mercury.L5.vsop
/usr/share/kstars/mercury.R0.vsop
/usr/share/kstars/mercury.R1.vsop
/usr/share/kstars/mercury.R2.vsop
/usr/share/kstars/mercury.R3.vsop
/usr/share/kstars/mercury.R4.vsop
/usr/share/kstars/mercury.R5.vsop
/usr/share/kstars/mercury.orbit
/usr/share/kstars/milkyway.dat
/usr/share/kstars/moonB.dat
/usr/share/kstars/moonLR.dat
/usr/share/kstars/moonless-night.colors
/usr/share/kstars/namedstars.dat
/usr/share/kstars/neptune.B0.vsop
/usr/share/kstars/neptune.B1.vsop
/usr/share/kstars/neptune.B2.vsop
/usr/share/kstars/neptune.B3.vsop
/usr/share/kstars/neptune.B4.vsop
/usr/share/kstars/neptune.B5.vsop
/usr/share/kstars/neptune.L0.vsop
/usr/share/kstars/neptune.L1.vsop
/usr/share/kstars/neptune.L2.vsop
/usr/share/kstars/neptune.L3.vsop
/usr/share/kstars/neptune.L4.vsop
/usr/share/kstars/neptune.L5.vsop
/usr/share/kstars/neptune.R0.vsop
/usr/share/kstars/neptune.R1.vsop
/usr/share/kstars/neptune.R2.vsop
/usr/share/kstars/neptune.R3.vsop
/usr/share/kstars/neptune.R4.vsop
/usr/share/kstars/neptune.orbit
/usr/share/kstars/ngcic.dat
/usr/share/kstars/night.colors
/usr/share/kstars/pluto.orbit
/usr/share/kstars/satellites.dat
/usr/share/kstars/saturn.B0.vsop
/usr/share/kstars/saturn.B1.vsop
/usr/share/kstars/saturn.B2.vsop
/usr/share/kstars/saturn.B3.vsop
/usr/share/kstars/saturn.B4.vsop
/usr/share/kstars/saturn.B5.vsop
/usr/share/kstars/saturn.L0.vsop
/usr/share/kstars/saturn.L1.vsop
/usr/share/kstars/saturn.L2.vsop
/usr/share/kstars/saturn.L3.vsop
/usr/share/kstars/saturn.L4.vsop
/usr/share/kstars/saturn.L5.vsop
/usr/share/kstars/saturn.R0.vsop
/usr/share/kstars/saturn.R1.vsop
/usr/share/kstars/saturn.R2.vsop
/usr/share/kstars/saturn.R3.vsop
/usr/share/kstars/saturn.R4.vsop
/usr/share/kstars/saturn.R5.vsop
/usr/share/kstars/saturn.orbit
/usr/share/kstars/skycultures.sqlite
/usr/share/kstars/skycultures/inuit/blubber-container.png
/usr/share/kstars/skycultures/inuit/breastbone.png
/usr/share/kstars/skycultures/inuit/caribou.png
/usr/share/kstars/skycultures/inuit/collarbones.png
/usr/share/kstars/skycultures/inuit/dogs.png
/usr/share/kstars/skycultures/inuit/lamp-stand.png
/usr/share/kstars/skycultures/inuit/runners.png
/usr/share/kstars/skycultures/inuit/the-one-behind.png
/usr/share/kstars/skycultures/inuit/two-in-front.png
/usr/share/kstars/skycultures/inuit/two-placed-far-apart.png
/usr/share/kstars/skycultures/inuit/two-sunbeams.png
/usr/share/kstars/skycultures/western/andromeda.png
/usr/share/kstars/skycultures/western/antlia.png
/usr/share/kstars/skycultures/western/apus.png
/usr/share/kstars/skycultures/western/aquarius.png
/usr/share/kstars/skycultures/western/aquila.png
/usr/share/kstars/skycultures/western/ara.png
/usr/share/kstars/skycultures/western/argonavis.png
/usr/share/kstars/skycultures/western/aries.png
/usr/share/kstars/skycultures/western/auriga.png
/usr/share/kstars/skycultures/western/bootes.png
/usr/share/kstars/skycultures/western/caelum.png
/usr/share/kstars/skycultures/western/camelopardalis.png
/usr/share/kstars/skycultures/western/cancer.png
/usr/share/kstars/skycultures/western/canes-venatici.png
/usr/share/kstars/skycultures/western/canis-major.png
/usr/share/kstars/skycultures/western/canis-minor.png
/usr/share/kstars/skycultures/western/capricornus.png
/usr/share/kstars/skycultures/western/cassiopeia.png
/usr/share/kstars/skycultures/western/centaurus.png
/usr/share/kstars/skycultures/western/cepheus.png
/usr/share/kstars/skycultures/western/cetus.png
/usr/share/kstars/skycultures/western/chamaeleon.png
/usr/share/kstars/skycultures/western/circinus.png
/usr/share/kstars/skycultures/western/columba.png
/usr/share/kstars/skycultures/western/coma-berenices.png
/usr/share/kstars/skycultures/western/corona-australis.png
/usr/share/kstars/skycultures/western/corona-borealis.png
/usr/share/kstars/skycultures/western/corvus.png
/usr/share/kstars/skycultures/western/crater.png
/usr/share/kstars/skycultures/western/crux.png
/usr/share/kstars/skycultures/western/cygnus.png
/usr/share/kstars/skycultures/western/delphinus.png
/usr/share/kstars/skycultures/western/dorado.png
/usr/share/kstars/skycultures/western/draco.png
/usr/share/kstars/skycultures/western/equuleus.png
/usr/share/kstars/skycultures/western/eridanus.png
/usr/share/kstars/skycultures/western/fornax.png
/usr/share/kstars/skycultures/western/gemini.png
/usr/share/kstars/skycultures/western/grus.png
/usr/share/kstars/skycultures/western/hercules.png
/usr/share/kstars/skycultures/western/horlogium.png
/usr/share/kstars/skycultures/western/hydra.png
/usr/share/kstars/skycultures/western/hydrus.png
/usr/share/kstars/skycultures/western/indus.png
/usr/share/kstars/skycultures/western/lacerta.png
/usr/share/kstars/skycultures/western/leo-minor.png
/usr/share/kstars/skycultures/western/leo.png
/usr/share/kstars/skycultures/western/lepus.png
/usr/share/kstars/skycultures/western/libra.png
/usr/share/kstars/skycultures/western/lupus.png
/usr/share/kstars/skycultures/western/lynx.png
/usr/share/kstars/skycultures/western/lyra.png
/usr/share/kstars/skycultures/western/mensa.png
/usr/share/kstars/skycultures/western/microscopium.png
/usr/share/kstars/skycultures/western/monoceros.png
/usr/share/kstars/skycultures/western/musca.png
/usr/share/kstars/skycultures/western/norma.png
/usr/share/kstars/skycultures/western/octans.png
/usr/share/kstars/skycultures/western/ophiuchus.png
/usr/share/kstars/skycultures/western/orion.png
/usr/share/kstars/skycultures/western/pavo.png
/usr/share/kstars/skycultures/western/pegasus.png
/usr/share/kstars/skycultures/western/perseus.png
/usr/share/kstars/skycultures/western/phoenix.png
/usr/share/kstars/skycultures/western/pictor.png
/usr/share/kstars/skycultures/western/pisces.png
/usr/share/kstars/skycultures/western/piscis-austrinus.png
/usr/share/kstars/skycultures/western/pyxis.png
/usr/share/kstars/skycultures/western/reticulum.png
/usr/share/kstars/skycultures/western/sagitta.png
/usr/share/kstars/skycultures/western/sagittarius.png
/usr/share/kstars/skycultures/western/scorpius.png
/usr/share/kstars/skycultures/western/sculptor.png
/usr/share/kstars/skycultures/western/scutum.png
/usr/share/kstars/skycultures/western/sextans.png
/usr/share/kstars/skycultures/western/taurus.png
/usr/share/kstars/skycultures/western/telescopium.png
/usr/share/kstars/skycultures/western/triangulum-australe.png
/usr/share/kstars/skycultures/western/triangulum.png
/usr/share/kstars/skycultures/western/tucana.png
/usr/share/kstars/skycultures/western/ursa-major.png
/usr/share/kstars/skycultures/western/ursa-minor.png
/usr/share/kstars/skycultures/western/virgo.png
/usr/share/kstars/skycultures/western/volans.png
/usr/share/kstars/skycultures/western/vulpecula.png
/usr/share/kstars/smc.dat
/usr/share/kstars/starlnum.idx
/usr/share/kstars/starnames.dat
/usr/share/kstars/stars.dat
/usr/share/kstars/textures/defaultflag.png
/usr/share/kstars/textures/galaxy-cluster.png
/usr/share/kstars/textures/galaxy.png
/usr/share/kstars/textures/gaseous-nebula.png
/usr/share/kstars/textures/globular-cluster.png
/usr/share/kstars/textures/jupiter.png
/usr/share/kstars/textures/mars.png
/usr/share/kstars/textures/mercury.png
/usr/share/kstars/textures/moon00.png
/usr/share/kstars/textures/moon01.png
/usr/share/kstars/textures/moon02.png
/usr/share/kstars/textures/moon03.png
/usr/share/kstars/textures/moon04.png
/usr/share/kstars/textures/moon05.png
/usr/share/kstars/textures/moon06.png
/usr/share/kstars/textures/moon07.png
/usr/share/kstars/textures/moon08.png
/usr/share/kstars/textures/moon09.png
/usr/share/kstars/textures/moon10.png
/usr/share/kstars/textures/moon11.png
/usr/share/kstars/textures/moon12.png
/usr/share/kstars/textures/moon13.png
/usr/share/kstars/textures/moon14.png
/usr/share/kstars/textures/moon15.png
/usr/share/kstars/textures/moon16.png
/usr/share/kstars/textures/moon17.png
/usr/share/kstars/textures/moon18.png
/usr/share/kstars/textures/moon19.png
/usr/share/kstars/textures/moon20.png
/usr/share/kstars/textures/moon21.png
/usr/share/kstars/textures/moon22.png
/usr/share/kstars/textures/moon23.png
/usr/share/kstars/textures/moon24.png
/usr/share/kstars/textures/moon25.png
/usr/share/kstars/textures/moon26.png
/usr/share/kstars/textures/moon27.png
/usr/share/kstars/textures/moon28.png
/usr/share/kstars/textures/moon29.png
/usr/share/kstars/textures/moon30.png
/usr/share/kstars/textures/moon31.png
/usr/share/kstars/textures/moon32.png
/usr/share/kstars/textures/moon33.png
/usr/share/kstars/textures/moon34.png
/usr/share/kstars/textures/moon35.png
/usr/share/kstars/textures/neptune.png
/usr/share/kstars/textures/obslistsymbol.png
/usr/share/kstars/textures/open-cluster.png
/usr/share/kstars/textures/planetary-nebula.png
/usr/share/kstars/textures/pluto.png
/usr/share/kstars/textures/saturn.png
/usr/share/kstars/textures/star.png
/usr/share/kstars/textures/sun.png
/usr/share/kstars/textures/uranus.png
/usr/share/kstars/textures/venus.png
/usr/share/kstars/themes/blackbody.colors
/usr/share/kstars/themes/colorcontrast.colors
/usr/share/kstars/themes/darkroom.colors
/usr/share/kstars/themes/graycard.colors
/usr/share/kstars/themes/highkey.colors
/usr/share/kstars/themes/lowkey.colors
/usr/share/kstars/themes/nightvision.colors
/usr/share/kstars/themes/shadeofgray.colors
/usr/share/kstars/themes/sunsetcolor.colors
/usr/share/kstars/themes/whitebalance.colors
/usr/share/kstars/tips
/usr/share/kstars/unnamedstars.dat
/usr/share/kstars/uranus.B0.vsop
/usr/share/kstars/uranus.B1.vsop
/usr/share/kstars/uranus.B2.vsop
/usr/share/kstars/uranus.B3.vsop
/usr/share/kstars/uranus.B4.vsop
/usr/share/kstars/uranus.L0.vsop
/usr/share/kstars/uranus.L1.vsop
/usr/share/kstars/uranus.L2.vsop
/usr/share/kstars/uranus.L3.vsop
/usr/share/kstars/uranus.L4.vsop
/usr/share/kstars/uranus.L5.vsop
/usr/share/kstars/uranus.R0.vsop
/usr/share/kstars/uranus.R1.vsop
/usr/share/kstars/uranus.R2.vsop
/usr/share/kstars/uranus.R3.vsop
/usr/share/kstars/uranus.R4.vsop
/usr/share/kstars/uranus.orbit
/usr/share/kstars/venus.B0.vsop
/usr/share/kstars/venus.B1.vsop
/usr/share/kstars/venus.B2.vsop
/usr/share/kstars/venus.B3.vsop
/usr/share/kstars/venus.B4.vsop
/usr/share/kstars/venus.B5.vsop
/usr/share/kstars/venus.L0.vsop
/usr/share/kstars/venus.L1.vsop
/usr/share/kstars/venus.L2.vsop
/usr/share/kstars/venus.L3.vsop
/usr/share/kstars/venus.L4.vsop
/usr/share/kstars/venus.L5.vsop
/usr/share/kstars/venus.R0.vsop
/usr/share/kstars/venus.R1.vsop
/usr/share/kstars/venus.R2.vsop
/usr/share/kstars/venus.R3.vsop
/usr/share/kstars/venus.R4.vsop
/usr/share/kstars/venus.R5.vsop
/usr/share/kstars/venus.orbit
/usr/share/kstars/windi.png
/usr/share/kstars/wzdownload.png
/usr/share/kstars/wzekos.png
/usr/share/kstars/wzgeo.png
/usr/share/kstars/wzscope.png
/usr/share/kstars/wzstars.png
/usr/share/metainfo/org.kde.kstars.appdata.xml
/usr/share/sounds/KDE-KStars-Alert.ogg
/usr/share/sounds/KDE-KStars-FITS-Received.ogg
/usr/share/sounds/KDE-KStars-Finish-Success.ogg
/usr/share/sounds/KDE-KStars-Sys-App-Error-Serious.ogg
/usr/share/sounds/KDE-KStars-Sys-App-Message.ogg
/usr/share/sounds/KDE-KStars-Warning.ogg

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/en/kstars/Add_Object_to_Session_plan.png
/usr/share/doc/HTML/en/kstars/Another_way4.png
/usr/share/doc/HTML/en/kstars/Another_way5.png
/usr/share/doc/HTML/en/kstars/Another_way6.png
/usr/share/doc/HTML/en/kstars/Another_way_to_add.png
/usr/share/doc/HTML/en/kstars/Another_way_to_add_part3.png
/usr/share/doc/HTML/en/kstars/Arp84_EyepieceView.png
/usr/share/doc/HTML/en/kstars/Delete_all_images.png
/usr/share/doc/HTML/en/kstars/EPView_Screenshot.png
/usr/share/doc/HTML/en/kstars/KStars_Neptune.png
/usr/share/doc/HTML/en/kstars/Savin_session.png
/usr/share/doc/HTML/en/kstars/add_catalog.png
/usr/share/doc/HTML/en/kstars/added_ldn.png
/usr/share/doc/HTML/en/kstars/advanced_tab.png
/usr/share/doc/HTML/en/kstars/ai-contents.docbook
/usr/share/doc/HTML/en/kstars/alpha.png
/usr/share/doc/HTML/en/kstars/altvstime.docbook
/usr/share/doc/HTML/en/kstars/altvstime.png
/usr/share/doc/HTML/en/kstars/astroinfo.docbook
/usr/share/doc/HTML/en/kstars/blackbody.docbook
/usr/share/doc/HTML/en/kstars/blackbody.png
/usr/share/doc/HTML/en/kstars/calc-angdist.docbook
/usr/share/doc/HTML/en/kstars/calc-angdist.png
/usr/share/doc/HTML/en/kstars/calc-apcoords.docbook
/usr/share/doc/HTML/en/kstars/calc-apcoords.png
/usr/share/doc/HTML/en/kstars/calc-dayduration.docbook
/usr/share/doc/HTML/en/kstars/calc-daylength.png
/usr/share/doc/HTML/en/kstars/calc-ecliptic.docbook
/usr/share/doc/HTML/en/kstars/calc-ecliptic.png
/usr/share/doc/HTML/en/kstars/calc-eqgal.docbook
/usr/share/doc/HTML/en/kstars/calc-eqgal.png
/usr/share/doc/HTML/en/kstars/calc-equinox.docbook
/usr/share/doc/HTML/en/kstars/calc-equinox.png
/usr/share/doc/HTML/en/kstars/calc-geodetic.docbook
/usr/share/doc/HTML/en/kstars/calc-geodetic.png
/usr/share/doc/HTML/en/kstars/calc-horizontal.docbook
/usr/share/doc/HTML/en/kstars/calc-horizontal.png
/usr/share/doc/HTML/en/kstars/calc-julian.png
/usr/share/doc/HTML/en/kstars/calc-julianday.docbook
/usr/share/doc/HTML/en/kstars/calc-planetcoords.docbook
/usr/share/doc/HTML/en/kstars/calc-planetcoords.png
/usr/share/doc/HTML/en/kstars/calc-sidereal.docbook
/usr/share/doc/HTML/en/kstars/calc-sidereal.png
/usr/share/doc/HTML/en/kstars/calculator.docbook
/usr/share/doc/HTML/en/kstars/cequator.docbook
/usr/share/doc/HTML/en/kstars/color_indices.png
/usr/share/doc/HTML/en/kstars/colorandtemp.docbook
/usr/share/doc/HTML/en/kstars/colors_tab.png
/usr/share/doc/HTML/en/kstars/commands.docbook
/usr/share/doc/HTML/en/kstars/complete_info_ldn.png
/usr/share/doc/HTML/en/kstars/config.docbook
/usr/share/doc/HTML/en/kstars/cosmicdist.docbook
/usr/share/doc/HTML/en/kstars/cpoles.docbook
/usr/share/doc/HTML/en/kstars/credits.docbook
/usr/share/doc/HTML/en/kstars/csphere.docbook
/usr/share/doc/HTML/en/kstars/darkmatter.docbook
/usr/share/doc/HTML/en/kstars/delete_catalog.png
/usr/share/doc/HTML/en/kstars/detaildialog.png
/usr/share/doc/HTML/en/kstars/details.docbook
/usr/share/doc/HTML/en/kstars/devicemanager.png
/usr/share/doc/HTML/en/kstars/dss.png
/usr/share/doc/HTML/en/kstars/dumpmode.docbook
/usr/share/doc/HTML/en/kstars/ecliptic.docbook
/usr/share/doc/HTML/en/kstars/ekos_tab.png
/usr/share/doc/HTML/en/kstars/ellipticalgalaxies.docbook
/usr/share/doc/HTML/en/kstars/epoch.docbook
/usr/share/doc/HTML/en/kstars/equinox.docbook
/usr/share/doc/HTML/en/kstars/execute_session_nt.png
/usr/share/doc/HTML/en/kstars/execute_session_the_nt.png
/usr/share/doc/HTML/en/kstars/eyepieceview.docbook
/usr/share/doc/HTML/en/kstars/faq.docbook
/usr/share/doc/HTML/en/kstars/find.png
/usr/share/doc/HTML/en/kstars/find2.png
/usr/share/doc/HTML/en/kstars/fitsarea.png
/usr/share/doc/HTML/en/kstars/fitsviewer.docbook
/usr/share/doc/HTML/en/kstars/flux.docbook
/usr/share/doc/HTML/en/kstars/flux.png
/usr/share/doc/HTML/en/kstars/flux1.png
/usr/share/doc/HTML/en/kstars/flux2.png
/usr/share/doc/HTML/en/kstars/fovdialog.png
/usr/share/doc/HTML/en/kstars/geocoords.docbook
/usr/share/doc/HTML/en/kstars/geolocator.png
/usr/share/doc/HTML/en/kstars/greatcircle.docbook
/usr/share/doc/HTML/en/kstars/guides_tab.png
/usr/share/doc/HTML/en/kstars/hips.docbook
/usr/share/doc/HTML/en/kstars/horizon.docbook
/usr/share/doc/HTML/en/kstars/hourangle.docbook
/usr/share/doc/HTML/en/kstars/import_catalog.png
/usr/share/doc/HTML/en/kstars/index.cache.bz2
/usr/share/doc/HTML/en/kstars/index.docbook
/usr/share/doc/HTML/en/kstars/indi.docbook
/usr/share/doc/HTML/en/kstars/indi_tab.png
/usr/share/doc/HTML/en/kstars/indicapture.png
/usr/share/doc/HTML/en/kstars/indiclient.png
/usr/share/doc/HTML/en/kstars/indicontrolpanel.png
/usr/share/doc/HTML/en/kstars/jmoons.docbook
/usr/share/doc/HTML/en/kstars/jmoons.png
/usr/share/doc/HTML/en/kstars/julianday.docbook
/usr/share/doc/HTML/en/kstars/kepler2nd.png
/usr/share/doc/HTML/en/kstars/kepler3d.png
/usr/share/doc/HTML/en/kstars/kstars_hips.png
/usr/share/doc/HTML/en/kstars/kstars_horizon.png
/usr/share/doc/HTML/en/kstars/lambda_ex.png
/usr/share/doc/HTML/en/kstars/lambda_max.png
/usr/share/doc/HTML/en/kstars/leapyear.docbook
/usr/share/doc/HTML/en/kstars/lightcurve.png
/usr/share/doc/HTML/en/kstars/lightcurves.docbook
/usr/share/doc/HTML/en/kstars/load_catalog.png
/usr/share/doc/HTML/en/kstars/luminosity.docbook
/usr/share/doc/HTML/en/kstars/luminosity.png
/usr/share/doc/HTML/en/kstars/luminosity_ex.png
/usr/share/doc/HTML/en/kstars/magnitude.docbook
/usr/share/doc/HTML/en/kstars/meridian.docbook
/usr/share/doc/HTML/en/kstars/newfov.png
/usr/share/doc/HTML/en/kstars/obsplanner.docbook
/usr/share/doc/HTML/en/kstars/open_dialog_ldn.png
/usr/share/doc/HTML/en/kstars/open_ldn.png
/usr/share/doc/HTML/en/kstars/overwrite_catalog.png
/usr/share/doc/HTML/en/kstars/parallax.docbook
/usr/share/doc/HTML/en/kstars/popup.png
/usr/share/doc/HTML/en/kstars/precession.docbook
/usr/share/doc/HTML/en/kstars/quicktour.docbook
/usr/share/doc/HTML/en/kstars/retrograde.docbook
/usr/share/doc/HTML/en/kstars/satellites_tab.png
/usr/share/doc/HTML/en/kstars/screen1.png
/usr/share/doc/HTML/en/kstars/scriptbuilder.docbook
/usr/share/doc/HTML/en/kstars/scriptbuilder.png
/usr/share/doc/HTML/en/kstars/sds.png
/usr/share/doc/HTML/en/kstars/sidereal.docbook
/usr/share/doc/HTML/en/kstars/skycoords.docbook
/usr/share/doc/HTML/en/kstars/skymapdevice.png
/usr/share/doc/HTML/en/kstars/solarsys.docbook
/usr/share/doc/HTML/en/kstars/solarsystem.png
/usr/share/doc/HTML/en/kstars/solarsystem_tab.png
/usr/share/doc/HTML/en/kstars/spiralgalaxies.docbook
/usr/share/doc/HTML/en/kstars/star_colors.png
/usr/share/doc/HTML/en/kstars/stars.docbook
/usr/share/doc/HTML/en/kstars/supernovae_tab.png
/usr/share/doc/HTML/en/kstars/telescopes.docbook
/usr/share/doc/HTML/en/kstars/timezones.docbook
/usr/share/doc/HTML/en/kstars/tools.docbook
/usr/share/doc/HTML/en/kstars/utime.docbook
/usr/share/doc/HTML/en/kstars/viewops.png
/usr/share/doc/HTML/en/kstars/wut.docbook
/usr/share/doc/HTML/en/kstars/wut.png
/usr/share/doc/HTML/en/kstars/zenith.docbook

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kstars/COPYING
/usr/share/package-licenses/kstars/COPYING.DOC
/usr/share/package-licenses/kstars/LICENSE_OpenNGC
/usr/share/package-licenses/kstars/cmake_modules_COPYING-CMAKE-SCRIPTS
/usr/share/package-licenses/kstars/kstars_libtess_src_LICENSE
