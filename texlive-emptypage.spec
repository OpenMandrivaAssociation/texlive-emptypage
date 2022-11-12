Name:		texlive-emptypage
Version:	18064
Release:	1
Summary:	Make empty pages really empty
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/emptypage
License:	LPPL1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/emptypage.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/emptypage.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/emptypage.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package prevents page numbers and headings from appearing
on empty pages.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/emptypage/emptypage.sty
%doc %{_texmfdistdir}/doc/latex/emptypage/README
%doc %{_texmfdistdir}/doc/latex/emptypage/emptypage.pdf
#- source
%doc %{_texmfdistdir}/source/latex/emptypage/emptypage.dtx
%doc %{_texmfdistdir}/source/latex/emptypage/emptypage.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
