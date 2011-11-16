Name:		sxiv
Version:	1.0
Release:	1
Summary:	Simple (or small or suckless) X Image Viewer
Group:		Graphics
License:	GPLv2
URL:		https://github.com/muennich/%{name}/
Source0:	https://github.com/downloads/muennich/%{name}/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
BuildRequires:	libx11-devel
BuildRequires:	imlib2-devel
BuildRequires:	desktop-file-utils

%description
sxiv is an alternative to feh and qiv. Its only dependency besides xlib
is imlib2. The primary goal for writing sxiv is to create an image viewer,
which only has the most basic features required for fast image viewing (the
ones I want). It works nicely with tiling window managers and its code base
should be kept small and clean to make it easy for you to dig into it and
customize it for your needs.

%prep
%setup -q

%build
%make

%install
make install DESTDIR=%{buildroot} PREFIX=%{_prefix}
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}

%files
%doc LICENSE README.md
%{_bindir}/sxiv
%{_mandir}/man1/*
%{_datadir}/applications
