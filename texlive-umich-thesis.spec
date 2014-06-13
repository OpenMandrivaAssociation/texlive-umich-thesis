# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/umich-thesis
# catalog-date 2009-09-27 11:52:43 +0200
# catalog-license lppl
# catalog-version 1.20
Name:		texlive-umich-thesis
Version:	1.20
Release:	7
Summary:	University of Michigan Thesis LaTeX class
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/umich-thesis
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/umich-thesis.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/umich-thesis.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A LaTeX2e class to create a University of Michigan dissertation
according to the Rackham dissertation handbook.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/umich-thesis/umich-thesis.cls
%doc %{_texmfdistdir}/doc/latex/umich-thesis/README

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.20-2
+ Revision: 757249
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.20-1
+ Revision: 719839
- texlive-umich-thesis
- texlive-umich-thesis
- texlive-umich-thesis

