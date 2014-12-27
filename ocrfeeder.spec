Summary:	OCRFeeder - document layout analysis and optical character recognition system
Summary(pl.UTF-8):	OCRFeeder - system analizy układu dokumentu i optycznego rozpoznawania znaków
Name:		ocrfeeder
Version:	0.8.1
Release:	1
License:	GPL v3+
Group:		Applications/Graphics
Source0:	http://ftp.gnome.org/pub/GNOME/sources/ocrfeeder/0.8/%{name}-%{version}.tar.xz
# Source0-md5:	defa1fc1034e637f48fbc37a4809296a
URL:		https://wiki.gnome.org/OCRFeeder
BuildRequires:	gettext-tools
BuildRequires:	gnome-doc-utils
# Gtk, GooCanvas gobject bindings
BuildRequires:	goocanvas2
# Gtk gobject binding
BuildRequires:	gtk+3
BuildRequires:	intltool >= 0.35.0
# sane, reportlab
BuildRequires:	python-PIL
BuildRequires:	python-ReportLab
BuildRequires:	python-pyenchant
# note: checks for pygobject, but uses pygobject3
BuildRequires:	python-pygobject
BuildRequires:	python-pysane
BuildRequires:	python-modules >= 1:2.5
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	sed >= 4.0
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	goocanvas2
Requires:	gtk+3
Requires:	python-PIL
Requires:	python-ReportLab
Requires:	python-modules >= 1:2.5
Requires:	python-pyenchant
Requires:	python-pygobject3
Requires:	python-pysane
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

%{__sed} -i -e '1s,/usr/bin/env python,/usr/bin/python,' bin/ocrfeeder.in bin/ocrfeeder-cli.in

%build
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%py_postclean

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TRANSLATORS
%attr(755,root,root) %{_bindir}/ocrfeeder
%attr(755,root,root) %{_bindir}/ocrfeeder-cli
%{py_sitescriptdir}/ocrfeeder
%{_datadir}/ocrfeeder
%{_desktopdir}/ocrfeeder.desktop
%{_mandir}/man1/ocrfeeder.1*
%{_mandir}/man1/ocrfeeder-cli.1*
