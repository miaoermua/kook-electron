# Maintainer: miaoermua <miaoermua@gmail.com>
pkgname=kook-electron
pkgver=1.2.9
pkgrel=1
pkgdesc="KOOK Electron App (uses system electron)"
arch=('x86_64')
url="https://www.kookapp.cn/app/"
license=('MIT')
depends=('electron')
makedepends=('git')
provides=($pkgname)
options=(!emptydirs)

source=(
    "kook-electron-v$pkgver.tar.gz" 
)
sha256sums=('SKIP')

package() {
    _datadir="/usr/lib/$pkgname"
    _bindir="/usr/bin"
    _desktopdir="/usr/share/applications"
    _iconsdir="/usr/share/icons/hicolor"

    mkdir -p "$pkgdir$_datadir"
    mkdir -p "$pkgdir$_bindir"
    mkdir -p "$pkgdir$_desktopdir"
    mkdir -p "$pkgdir$_iconsdir/256x256/apps"

    cd "$srcdir/kook-electron"
    cp -r main.js package.json "$pkgdir$_datadir/"

    cp icon.png "$pkgdir$_iconsdir/256x256/apps/$pkgname.png"

    cat > "$pkgdir$_bindir/kook-electron" << 'EOF'
#!/bin/sh
APP_DIR="/usr/lib/kook-electron"
cd "$APP_DIR"
echo "[Tip] 首次加载资源可能需要 10s 左右"
exec electron main.js "$@"
EOF
    chmod +x "$pkgdir$_bindir/kook-electron"

    cat > "$pkgdir$_desktopdir/$pkgname.desktop" << EOF
[Desktop Entry]
Name=KOOK
Comment=KOOK Electron App
Exec=$pkgname
Icon=$pkgname
Terminal=false
Type=Application
Categories=Network;Chat;
StartupWMClass=kook-electron
EOF
    chmod 644 "$pkgdir$_desktopdir/$pkgname.desktop"
}