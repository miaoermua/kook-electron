// build.js
const { build } = require('electron-builder');

build({
  config: {
    appId: "cn.kook.app",
    productName: "kook-electron",
    directories: {
      output: "dist"
    },
    files: [
      "main.js",
      "package.json", 
      "icon.png"
    ],
    linux: {
      target: [
        'AppImage',
        'tar.gz'
      ],
      icon: "icon.png",
      category: "Network"
    }
  }
})
.then(() => {
  console.log('🎉 构建成功！');
  console.log('构建产物位于 ./dist/ 目录下。');
})
.catch((error) => {
  console.error('❌ 构建失败：', error);
  process.exit(1);
});