%define		packname	edgeR

Summary:	Empirical analysis of digital gene expression data in R
Name:		R-%{packname}
Version:	3.2.3
Release:	1
License:	LGPL
Group:		Applications/Engineering
Source0:	http://www.bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
# Source0-md5:	fdf9457b51e457743bc9171b8026afc0
URL:		http://www.bioconductor.org/packages/release/bioc/html/edgeR.html
BuildRequires:	R-limma
BuildRequires:	R
BuildRequires:	texlive-latex
Requires:	R-limma
Requires:	R
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Differential expression analysis of RNA-seq and digital gene
expression profiles with biological replication. Uses empirical Bayes
estimation and exact tests based on the negative binomial
distribution. Also useful for differential signal analysis with other
types of genome-scale count data.

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/R/library

R CMD INSTALL %{packname} -l $RPM_BUILD_ROOT%{_libdir}/R/library

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_libdir}/R/library/%{packname}/
%doc %{_libdir}/R/library/%{packname}/CITATION
%doc %{_libdir}/R/library/%{packname}/DESCRIPTION
%doc %{_libdir}/R/library/%{packname}/NEWS.Rd
%doc %{_libdir}/R/library/%{packname}/html
%doc %{_libdir}/R/library/%{packname}/doc
%{_libdir}/R/library/%{packname}/INDEX
%{_libdir}/R/library/%{packname}/Meta/
%{_libdir}/R/library/%{packname}/NAMESPACE
%{_libdir}/R/library/%{packname}/R/
%{_libdir}/R/library/%{packname}/help/
%{_libdir}/R/library/%{packname}/data
%dir %{_libdir}/R/library/%{packname}/libs
%attr(755,root,root) %{_libdir}/R/library/%{packname}/libs/edgeR.so
