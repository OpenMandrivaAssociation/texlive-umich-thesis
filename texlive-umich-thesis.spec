# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/umich-thesis
# catalog-date 2009-09-27 11:52:43 +0200
# catalog-license lppl
# catalog-version 1.20
Name:		texlive-umich-thesis
Version:	1.20
Release:	1
Summary:	University of Michigan Thesis LaTeX class
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/umich-thesis
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/umich-thesis.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/umich-thesis.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3

%description
A LaTeX2e class to create a University of Michigan dissertation
according to the Rackham dissertation handbook.

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
%{_texmfdistdir}/tex/latex/umich-thesis/umich-thesis.cls
%doc %{_texmfdistdir}/doc/latex/umich-thesis/README
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
