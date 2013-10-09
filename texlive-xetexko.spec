# revision 31108
# category Package
# catalog-ctan /macros/xetex/generic/xetexko
# catalog-date 2013-07-04 11:27:36 +0200
# catalog-license lppl1.3
# catalog-version 2.1
Name:		texlive-xetexko
Version:	2.1
Release:	1
Summary:	Typeset Korean with Xe(La)TeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/xetex/generic/xetexko
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xetexko.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xetexko.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package supports typesetting Korean documents (including
old Hangul texts), using XeTeX. It enhances the existing
support, in XeTeX, providing features that provide quality
typesetting.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/xetex/xetexko/hanja_hangul.tab
%{_texmfdistdir}/tex/xetex/xetexko/hanjacom_hangul.tab
%{_texmfdistdir}/tex/xetex/xetexko/hanjaexa_hangul.tab
%{_texmfdistdir}/tex/xetex/xetexko/xetexko-font.sty
%{_texmfdistdir}/tex/xetex/xetexko/xetexko-hanging.sty
%{_texmfdistdir}/tex/xetex/xetexko/xetexko-josa.sty
%{_texmfdistdir}/tex/xetex/xetexko/xetexko-space.sty
%{_texmfdistdir}/tex/xetex/xetexko/xetexko-vertical.sty
%{_texmfdistdir}/tex/xetex/xetexko/xetexko.sty
%doc %{_texmfdistdir}/doc/xetex/xetexko/ChangeLog
%doc %{_texmfdistdir}/doc/xetex/xetexko/README
%doc %{_texmfdistdir}/doc/xetex/xetexko/xetexko-doc.pdf
%doc %{_texmfdistdir}/doc/xetex/xetexko/xetexko-doc.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
