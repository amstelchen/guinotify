# Maintainer: Michael John <amstelchen at gmail dot com>

pkgname=guinotify
_pkgname=guinotify
pkgver=0.1.0
pkgrel=1
pkgdesc="A tiny frontend for inotify"
arch=('any')
url="http://github.com/amstelchen/guinotify"
license=('GPL')
packager=('Michael John')
depends=('python' 'python-gettext' 'python-wxpython' 'wxgtk3')
optdepends=('')
makedepends=(python-build python-installer)
source=("${pkgname}_${pkgver}.tar.gz"::"https://github.com/amstelchen/guinotify/archive/refs/tags/${pkgver}.tar.gz")
sha256sums=('833432a0284fe874e082d4cb2f0639d106b8c527b1a408c2caec2f22b3cb9558')

#build() {
#    python -m build --wheel --no-isolation
#}

package() {
    #python -m installer --destdir="$pkgdir" dist/*.whl

  install -Dm755 "${srcdir}/${_pkgname}-${pkgver}"/guinotify.py \
      "${pkgdir}"/usr/bin/guinotify
}
