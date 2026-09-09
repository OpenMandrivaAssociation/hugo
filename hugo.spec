%define debug_package %{nil}

Name:		hugo
Version:	0.166.0
Release:	1
Source0:	https://github.com/gohugoio/hugo/archive/v%{version}/%{name}-%{version}.tar.gz
# Vendor contains the most of the dependencies needed to build hugo
# use the create_vendor script to create this file
Source1:	vendor20260909.tar.gz
Source2:	https://github.com/bep/golibsass/archive/v1.2.0/golibsass-1.2.0.tar.gz
# Point go.mod at the local golibsass tree (includes libsass C sources)
Patch0:		patch0
Summary:	A static site generator written in Go.
URL:		https://gohugo.io/
License:	Apache 2.0
Group:		development
BuildRequires:	golang >= 1.27
BuildRequires:	git
BuildRequires:	clang
BuildRequires:	zstd

%description
Hugo is a static site generator written in Go, optimized for speed and designed
for flexibility. With its advanced templating system and fast asset pipelines,
Hugo renders a complete site in seconds, often less.

%prep
%setup -q -b 1 -b 2
%patch 0 -p 1

%build
export GOPROXY=off
export GOSUMDB=off
export CGO_ENABLED=1
go build -tags extended -o %{buildroot}%{_bindir}/%{name}
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
