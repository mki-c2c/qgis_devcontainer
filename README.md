# Setup

- make sure xhost is shared (brutal way: `xhost +`)
- Install dev containers extension in vscode https://marketplace.visualstudio.com/items/?itemName=ms-vscode-remote.remote-containers
- open folder
- launch dev container
    - click reopen in container when suggested in popup
    - or manually ctrl+shift+p => Dev Containers: Reopen in Container (remote-containers.reopenInContainer)
- QGIS window opens
- activate my plugin
- open plugin in plugin directory


# Connect vscode debug

- in "run and debug" launch "Python Debugger: Remote Attach"
- when clicking on OK, an exception gets triggered in vscode
- when clicking Cancel, the console output bla gest caught in vscode
