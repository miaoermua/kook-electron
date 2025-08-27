const { app, BrowserWindow, nativeImage } = require('electron')

function createWindow() {
  const win = new BrowserWindow({
    width: 1200,
    height: 800,
    icon: nativeImage.createFromPath(__dirname + '/icon.png'),
    autoHideMenuBar: true,  // 隐藏菜单栏
    webPreferences: {
      partition: 'persist:oopz'
      nodeIntegration: false,    // 禁止网页直接访问 Node
      contextIsolation: true,    // 隔离网页和主进程
      enableRemoteModule: false, // 禁用 remote 模块
      webSecurity: true          // 开启网页安全策略
    }
  })

  win.setMenu(null) // 禁用菜单栏
  win.loadURL('https://web.oopz.cn')
}


app.whenReady().then(() => {
  createWindow()

  app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) createWindow()
  })
})

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') app.quit()
})