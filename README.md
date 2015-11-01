# BreadBoardBlack

Misc. scripts for BeagleBoneBlack


##Create Startup Service

source: https://gist.github.com/tstellanova/7323116

Fixed

1. Create a shell script and note the location.

  * ex. /root/StartScripts/star.sh

  * make sure you have the shebang line(#!) with the tack/dash to ensure that the script will run without any errors.
  ```
  '#!/bin/bash -
  
  # This can be any of your scripts.
  python /root/StartScript/start.py &
  ```

2. Create a service file in /lib/systemd/system/BootUp.service

  * The name of the service can be anything, try to make it reasonably named so you can remember what you did.
  ```
  [Unit]
  Description=My Fancy Service
  
  [Service]
  Type=simple
  ExecStart=/root/StartScripts/star.sh
  
  [Install]
  WantedBy=multi-user.target
  ```

  * The "ExecStart" path should point to whatever base script you want to run.

3. Create a symbolic link between your script and a special location under /etc:
  ```
  ln -s /lib/systemd/system/BootUp.service /etc/systemd/system/BootUp.service
  ```
  
4. Let your system acklowledge your new service
  ```
  systemctl daemon-reload
  systemctl enable BootUp.service
  systemctl start BootUp.service
  systemctl status BootUp.service
  ```
  * You can use the last command any any time to check the status of any service.  Very helpful when debugging if things go south.
  * 
  
```
systemctl stop BootUp.service
systemctl start BootUp.service
systemctl disable BootUp.service
```
* More useful commands

  
