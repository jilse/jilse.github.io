#!/bin/sh
jekyll build --config _config.yml,_config-bob.yml
smbclient //bob/web -A /home/jeff/.smbclient -c "cd backup; lcd /mnt/c/jeff/code/jilse.github.io/_site; prompt; recurse; mput *; exit;"
