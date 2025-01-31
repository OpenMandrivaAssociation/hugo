%define debug_package %{nil}

Name:		hugo
Version:	0.142.0
Release:	1
Source0:	https://github.com/gohugoio/hugo/archive/v%{version}/%{name}-%{version}.tar.gz
# Vendor contains the most of the dependencies needed to build hugo
# use the create_vendor script to create this file
Source1:    vendor20250129.tar.gz
Source2:    https://github.com/bep/golibsass/archive/v1.2.0/golibsass-1.2.0.tar.gz
Source3:    https://github.com/bep/gowebp/archive/v0.3.0/gowebp-0.3.0.tar.gz
Source4:    https://github.com/census-instrumentation/opencensus-go/archive/v0.24.0/opencensus-go-0.24.0.tar.gz
# Patch to modify the go.mod file to poile at the above dependencies
Patch0:     patch0
Summary:	A static site generator written in Go.
URL:		https://gohugo.io/
License:	Apache 2.0
Group:		development	
BuildRequires: golang >= 1.20
BuildRequires: git
BuildRequires: clang 
BuildRequires: zstd

%description
Hugo is a static site generator written in Go, optimized for speed and designed
for flexibility. With its advanced templating system and fast asset pipelines,
Hugo renders a complete site in seconds, often less.

%prep
%setup -a 0 -b 1 -b 2  -b 3  -b 4
%patch  0 -p 1

%build
CGO_ENABLED=1 go build -tags extended -o %{buildroot}%{_bindir}/%{name} 
install -d -p %{buildroot}%{_datadir}/bash-completion/completions
%{buildroot}%{_bindir}/hugo completion > %{buildroot}%{_datadir}/bash-completion/completions/hugo
%{buildroot}%{_bindir}/hugo gen man --dir %{buildroot}%{_mandir}/man1
cd %{buildroot}%{_mandir}/man1
zstd --rm *

%files
%doc CONTRIBUTING.md README.md
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/bash-completion/completions/hugo
%{_mandir}/man1/*.1*
