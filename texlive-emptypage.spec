# revision 18064
# category Package
# catalog-ctan /macros/latex/contrib/emptypage
# catalog-date 2010-04-30 19:49:05 +0200
# catalog-license lppl1.2
# catalog-version 1.2
Name:		texlive-emptypage
Version:	1.2
Release:	1
Summary:	Make empty pages really empty
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/emptypage
License:	LPPL1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/emptypage.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/emptypage.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/emptypage.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
This package prevents page numbers and headings from appearing
on empty pages.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/emptypage/emptypage.sty
%doc %{_texmfdistdir}/doc/latex/emptypage/README
%doc %{_texmfdistdir}/doc/latex/emptypage/emptypage.pdf
#- source
%doc %{_texmfdistdir}/source/latex/emptypage/emptypage.dtx
%doc %{_texmfdistdir}/source/latex/emptypage/emptypage.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
