#!/bin/bash

sudo cp -v 128x128.png /usr/share/pixmaps/guinotify.png
sudo cp -v guinotify.desktop /usr/share/applications/
cp -v guinotify.desktop ~/Desktop/guinotify.desktop

xgettext -d guinotify -o locales/guinotify.pot *.py
#poedit 2>/dev/null

#python setup.py sdist
#python -m build --wheel --no-isolation
#updpkgsums
#makepkg -fci

#xdg-open ~/Desktop/GameInfo.desktop
python -m guinotify
#GoalFM.py