#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-WikipediR
Version  : 1.5.0
Release  : 14
URL      : https://cran.r-project.org/src/contrib/WikipediR_1.5.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/WikipediR_1.5.0.tar.gz
Summary  : A MediaWiki API Wrapper
Group    : Development/Tools
License  : MIT
Requires: R-httr
Requires: R-jsonlite
BuildRequires : R-httr
BuildRequires : R-jsonlite
BuildRequires : buildreq-R

%description
Wikimedia 'production' wikis, such as Wikipedia. It can be used to retrieve
    page text, information about users or the history of pages, and elements of
    the category tree.

%prep
%setup -q -c -n WikipediR

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1569376945

%install
export SOURCE_DATE_EPOCH=1569376945
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library WikipediR
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library WikipediR
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library WikipediR
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc WikipediR || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/WikipediR/DESCRIPTION
/usr/lib64/R/library/WikipediR/INDEX
/usr/lib64/R/library/WikipediR/LICENSE
/usr/lib64/R/library/WikipediR/Meta/Rd.rds
/usr/lib64/R/library/WikipediR/Meta/features.rds
/usr/lib64/R/library/WikipediR/Meta/hsearch.rds
/usr/lib64/R/library/WikipediR/Meta/links.rds
/usr/lib64/R/library/WikipediR/Meta/nsInfo.rds
/usr/lib64/R/library/WikipediR/Meta/package.rds
/usr/lib64/R/library/WikipediR/Meta/vignette.rds
/usr/lib64/R/library/WikipediR/NAMESPACE
/usr/lib64/R/library/WikipediR/NEWS
/usr/lib64/R/library/WikipediR/R/WikipediR
/usr/lib64/R/library/WikipediR/R/WikipediR.rdb
/usr/lib64/R/library/WikipediR/R/WikipediR.rdx
/usr/lib64/R/library/WikipediR/doc/WikipediR.Rmd
/usr/lib64/R/library/WikipediR/doc/WikipediR.html
/usr/lib64/R/library/WikipediR/doc/index.html
/usr/lib64/R/library/WikipediR/help/AnIndex
/usr/lib64/R/library/WikipediR/help/WikipediR.rdb
/usr/lib64/R/library/WikipediR/help/WikipediR.rdx
/usr/lib64/R/library/WikipediR/help/aliases.rds
/usr/lib64/R/library/WikipediR/help/paths.rds
/usr/lib64/R/library/WikipediR/html/00Index.html
/usr/lib64/R/library/WikipediR/html/R.css
/usr/lib64/R/library/WikipediR/tests/testthat.R
/usr/lib64/R/library/WikipediR/tests/testthat/test_category_retrieval.R
/usr/lib64/R/library/WikipediR/tests/testthat/test_content_retrieval.R
/usr/lib64/R/library/WikipediR/tests/testthat/test_metadata_retrieval.R
/usr/lib64/R/library/WikipediR/tests/testthat/test_recent_changes.R
