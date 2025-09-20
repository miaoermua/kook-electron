# Maintainer: miaoermua <miaoermua@gmail.com>
pkgname=kook-electron
pkgver=1.2.9
pkgrel=1
pkgdesc="KOOK Electron App (uses system electron; requires v34.5.8+)"
arch=('x86_64')
url="https://www.kookapp.cn/app/login/"
license=('MIT')
depends=('electron34')
optdepends=(
    'electron35: Alternative Electron 35 runtime'
    'electron36: Alternative Electron 36 runtime'
    'electron37: Alternative Electron 37 runtime'
)
makedepends=('git')
provides=($pkgname)
options=(!emptydirs)

source=(
    "kook-electron-$pkgver.tar.gz"
    "main.js"
    "package.json"
    "icon.png"
)
sha256sums=('SKIP' 'SKIP' 'SKIP' 'SKIP')

package() {
    _datadir="/usr/lib/$pkgname"
    _bindir="/usr/bin"
    _desktopdir="/usr/share/applications"
    _iconsdir="/usr/share/icons/hicolor"

    mkdir -p "$pkgdir$_datadir"
    mkdir -p "$pkgdir$_bindir"
    mkdir -p "$pkgdir$_desktopdir"
    mkdir -p "$pkgdir$_iconsdir/256x256/apps"

    cp "$srcdir/main.js" "$pkgdir$_datadir/"
    cp "$srcdir/package.json" "$pkgdir$_datadir/"
    cp "$srcdir/icon.png" "$pkgdir$_iconsdir/256x256/apps/$pkgname.png"

    cat > "$pkgdir$_bindir/kook-electron" << 'EOF'
#!/bin/sh
APP_DIR="/usr/lib/kook-electron"
cd "$APP_DIR" || exit 1

if [ -n "$ELECTRON_PATH" ] && [ -x "$ELECTRON_PATH" ]; then
  ELECTRON_BIN="$ELECTRON_PATH"
elif command -v electron37 >/dev/null 2>&1; then
  ELECTRON_BIN="$(command -v electron37)"
elif command -v electron36 >/dev/null 2>&1; then
  ELECTRON_BIN="$(command -v electron36)"
elif command -v electron35 >/dev/null 2>&1; then
  ELECTRON_BIN="$(command -v electron35)"
elif command -v electron34 >/dev/null 2>&1; then
  ELECTRON_BIN="$(command -v electron34)"
elif command -v electron >/dev/null 2>&1; then
  ELECTRON_BIN="$(command -v electron)"
else
  echo "Electron runtime not found. Please install 'electron34' or higher." >&2
  exit 127
fi

echo "[Tip] 首次加载资源可能需要 10s 左右"
exec "$ELECTRON_BIN" main.js "$@"
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
