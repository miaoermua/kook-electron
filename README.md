# kook-electron
使用 electron 打包的 KOOK Linux 客户端

版权声明，本项目只是打包网页版 KOOK，并无做其他修改，服务和版权提供商依旧为: 北京逍遥一下科技有限公司

## 构建应用

需要安装 nodejs 环境，并且 clone 本项目

```bash
npm init -y
npm install electron --save-dev
npm run build
```

## 安装

Archlinux(Arch 系):

> 待稳定后上传 AUR

```bash
wget https://github.com/miaoermua/kook-electron/releases/download/v0.96.1/kook-electron-0.96.1.pkg.tar.zst
sudo pacman -U kook*
```

Debian/Ubuntu:

```bash
wget https://github.com/miaoermua/kook-electron/releases/download/v0.96.1/kook-electron_0.96.1_amd64.deb
sudo apt install kook*
```