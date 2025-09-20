# kook-electron
使用 electron 打包的 KOOK Linux 客户端

版权声明，本项目只是打包网页版 KOOK，并无做其他修改，服务和版权提供商依旧为: 北京逍遥一下科技有限公司

<img width="1322" height="959" alt="截图 2025-08-22 20-58-28" src="https://github.com/user-attachments/assets/d2d88b24-016d-49f7-85ab-b3cf676122b6" />
<img width="1322" height="959" alt="截图 2025-08-22 20-58-39" src="https://github.com/user-attachments/assets/ba5654e0-a10f-4364-814f-b3a019ce2296" />


## 构建应用

需要安装 nodejs 环境，并且 clone 本项目

```bash
npm run build
```

构建完成将 tar.gz 复制出来让 pkgbuild 进行构建 （测试版本）

```bash
rm -rf pkg/ src/ *.pkg.tar.zst
cp dist/kook-electron-0.96.1.tar.gz .
makepkg -r
```

## 安装

Archlinux(Arch 系):

> 待稳定后上传 AUR

```bash
wget https://github.com/miaoermua/kook-electron/releases/download/v0.96.1-1/kook-electron-1.2.9-1-x86_64.pkg.tar.zst
sudo pacman -U kook*
```

Debian/Ubuntu:

```bash
wget https://github.com/miaoermua/kook-electron/releases/download/v0.96.1/kook-electron_0.96.1_amd64.deb
sudo apt install kook*
```
