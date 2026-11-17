%define debug_package %{nil}

Name:		hugo
Version:	0.170.1
Release:	1
Source0:	https://github.com/gohugoio/hugo/archive/v%{version}/%{name}-%{version}.tar.gz
# Vendor contains the dependencies needed to build hugo.
# Use the create_vendor script to create this file.
Source1:	vendor20261117.tar.gz
Summary:	A static site generator written in Go.
URL:		https://gohugo.io/
License:	Apache 2.0
Group:		development
BuildRequires:	golang >= 1.27
BuildRequires:	zstd

%description
Hugo is a static site generator written in Go, optimized for speed and designed
for flexibility. With its advanced templating system and fast asset pipelines,
Hugo renders a complete site in seconds, often less.

%prep
%setup -q -b 1

%build
export GOPROXY=off
export GOSUMDB=off
export CGO_ENABLED=0
go build -mod=vendor -buildvcs=false -o %{buildroot}%{_bindir}/%{name}
install -d -p %{buildroot}%{_datadir}/bash-completion/completions
%{buildroot}%{_bindir}/hugo completion bash > %{buildroot}%{_datadir}/bash-completion/completions/hugo
%{buildroot}%{_bindir}/hugo gen man --dir %{buildroot}%{_mandir}/man1
cd %{buildroot}%{_mandir}/man1
zstd --rm *

%files
%doc CONTRIBUTING.md README.md
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/bash-completion/completions/hugo
%{_mandir}/man1/*.1*
