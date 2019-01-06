const { app, BrowserWindow } = require('electron')

function createWindow () {
  // Crea la ventana del navegador.
  win = new BrowserWindow({ width: 800, height: 600 })

  // y carga el archivo index.html de la aplicación.
  win.loadFile('index.html')
}

app.on('ready', createWindow)