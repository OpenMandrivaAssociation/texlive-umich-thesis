Name:		texlive-umich-thesis
Version:	15878
Release:	2
Summary:	University of Michigan Thesis LaTeX class
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/umich-thesis
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/umich-thesis.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/umich-thesis.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
