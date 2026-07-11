%global tl_name xetexko
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	4.6
Release:	%{tl_revision}.1
Summary:	Typeset Korean with Xe(La)TeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/xetex/generic/xetexko
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xetexko.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xetexko.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package supports typesetting Korean documents (including old Hangul
texts), using XeTeX. It enhances the existing support, in XeTeX,
providing features that provide quality typesetting. This package
requires the cjk-ko package for its full functionality.

