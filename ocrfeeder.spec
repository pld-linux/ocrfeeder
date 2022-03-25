Summary:	OCRFeeder - document layout analysis and optical character recognition system
Summary(pl.UTF-8):	OCRFeeder - system analizy układu dokumentu i optycznego rozpoznawania znaków
Name:		ocrfeeder
Version:	0.8.5
Release:	2
License:	GPL v3+
Group:		Applications/Graphics
Source0:	https://download.gnome.org/sources/ocrfeeder/0.8/%{name}-%{version}.tar.xz
# Source0-md5:	908c68946d53cd1b864e53af1fe4de0d
URL:		https://wiki.gnome.org/Apps/OCRFeeder
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.11
BuildRequires:	gettext-tools
# for AM_GLIB_GNU_GETTEXT
BuildRequires:	glib2-devel >= 2.0
# Gtk, GooCanvas gobject bindings
BuildRequires:	goocanvas2
# Gtk gobject binding
BuildRequires:	gtk+3
BuildRequires:	gobject-introspection
BuildRequires:	intltool >= 0.35.0
BuildRequires:	python3 >= 1:3.5
BuildRequires:	python3-ReportLab
BuildRequires:	python3-odfpy
BuildRequires:	python3-pillow
BuildRequires:	python3-pyenchant
BuildRequires:	python3-pygobject3
BuildRequires:	python3-sane
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.507
BuildRequires:	sed >= 4.0
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	yelp-tools
BuildConflicts:	gtk4
Requires:	goocanvas2
Requires:	gtk+3
Requires:	python3-ReportLab
Requires:	python3-modules >= 1:3.5
Requires:	python3-odfpy
Requires:	python3-pillow
Requires:	python3-pyenchant
Requires:	python3-pygobject3
Requires:	python3-sane
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OCRFeeder is a document layout analysis and optical character
recognition system.

Given the images it will automatically outline its contents,
distinguish between what's graphics and text and perform OCR over the
latter. It generates multiple formats being its main one ODT.

It features a complete GTK+ graphical user interface that allows the
users to correct any unrecognized characters, defined or correct
bounding boxes, set paragraph styles, clean the input images, import
PDFs, save and load the project, export everything to multiple
formats, etc. OCRFeeder was developed as the project of the Master's
Thesis in Computer Science of Joaquim Rocha.

%description -l pl.UTF-8
OCRFeeder to system analizy układu dokumentów i optycznego
rozpoznawania znaków.

Po przekazaniu obrazów automatycznie obrysowuje ich zawartość,
rozróżniając tekst od grafiki i wykonując OCR na tekście. Potrafi
generować tekst w wielu formatach, między innymi ODT.

Zawiera pełny graficzny interfejs użytkownika GTK+, pozwalający na
korygowanie nie rozpoznanych znaków, definiowanie i poprawianie
prostokątów ograniczających, ustawianie styli akapitów, czyszczenie
obrazów wejściowych, importowanie plików PDF, zapisywanie i
wczytywanie projektów, eksportowanie wszystkiego do wielu formatów
itp. OCRFeeder powstał jako projekt z pracy magisterskiej z
informatyki Joaquima Rocha.

%prep
%setup -q

%{__sed} -i -e '1s,/usr/bin/env python3,%{__python3},' bin/ocrfeeder.in bin/ocrfeeder-cli.in

%build
# rebuild am to get PLD version of python.m4
%{__intltoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TRANSLATORS
%attr(755,root,root) %{_bindir}/ocrfeeder
%attr(755,root,root) %{_bindir}/ocrfeeder-cli
%{py3_sitescriptdir}/ocrfeeder
%{_datadir}/ocrfeeder
%{_datadir}/metainfo/org.gnome.OCRFeeder.appdata.xml
%{_desktopdir}/org.gnome.OCRFeeder.desktop
%{_iconsdir}/hicolor/scalable/apps/org.gnome.OCRFeeder.svg
%{_mandir}/man1/ocrfeeder.1*
%{_mandir}/man1/ocrfeeder-cli.1*
