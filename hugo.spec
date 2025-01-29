%define debug_package %{nil}

Name:		hugo
Version:	0.142.0
Release:	1
Source0:	https://github.com/gohugoio/hugo/archive/refs/tags/v%{version}.tar.gz
Summary:	A static site generator written in Go.
URL:		https://gohugo.io/
License:	Apache 2.0
Group:	    development	

Buildrequires: golang >= 1.20
Buildrequires: git
Buildrequires: clang 

%description
Hugo is a static site generator written in Go, optimized for speed and designed
for flexibility. With its advanced templating system and fast asset pipelines,
Hugo renders a complete site in seconds, often less.

%prep
%autosetup -p1

%build
CGO_ENABLED=1 go build -tags extended -o %{buildroot}%{_bindir}/%{name} 

%files
%{_bindir}/%{name}
%license LICENSE
