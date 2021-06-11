const { app, BrowserWindow } = require('electron'); //require electron npm

function createWindow () { //creating window for the app
  const win = new BrowserWindow({
    width: 800,
    height: 600
  });

  win.loadFile('index.html') //loading index.html
}

app.whenReady().then(() => { //when the app is ready
  createWindow(); //open a window for the app
});

app.on('window-all-closed', function () {
  if (process.platform !== 'darwin') app.quit(); //quite when the user close all windows
});
