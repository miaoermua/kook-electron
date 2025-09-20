Name:           kook-electron
Version:        1.2.9
Release:        1%{?dist}
Summary:        KOOK Electron App (uses system electron; requires v34.5.8+)

License:        MIT
URL:            https://www.kookapp.cn/app
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  make

Requires:       (electron >= 34.5.8 or nodejs-electron)
Recommends:     (electron >= 37 or electron37)
Suggests:       electron37

%description
KOOK 语音软件的 Electron 封装版本，使用系统安装的 Electron 运行时。

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{_libdir}/%{name}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/applications
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/256x256/apps
cp main.js package.json %{buildroot}%{_libdir}/%{name}/
cp icon.png %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/%{name}.png
cat > %{buildroot}%{_bindir}/%{name} << 'EOF'
#!/bin/sh
APP_DIR="%{_libdir}/%{name}"
cd "$APP_DIR" || exit 1

# 允许用户通过环境变量覆盖 Electron 可执行文件
if [ -n "$ELECTRON_PATH" ] && [ -x "$ELECTRON_PATH" ]; then
  ELECTRON_BIN="$ELECTRON_PATH"
elif command -v electron37 >/dev/null 2>&1; then
  ELECTRON_BIN="$(command -v electron37)"
elif command -v electron >/dev/null 2>&1; then
  ELECTRON_BIN="$(command -v electron)"
elif command -v nodejs-electron >/dev/null 2>&1; then
  ELECTRON_BIN="$(command -v nodejs-electron)"
else
  echo "Electron runtime not found. Please install 'electron', 'electron37', or 'nodejs-electron'." >&2
  exit 127
fi

echo "[Tip] 首次加载资源可能需要 10s 左右"
exec "$ELECTRON_BIN" main.js "$@"
EOF

chmod +x %{buildroot}%{_bindir}/%{name}
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=KOOK
Comment=KOOK Electron App
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Network;Chat;
StartupWMClass=%{name}
EOF

%files
%license LICENSE
%doc README.md
%{_libdir}/%{name}/
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/256x256/apps/%{name}.png

%changelog
* Thu Dec 21 2023 miaoermua <miaoermua@gmail.com> - 1.2.9-1
- Initial RPM package release
- Uses system Electron runtime (prefers electron37 if available)
- Reduces installation size by sharing Electron with other apps
- Fixed webPreferences syntax in main.js
