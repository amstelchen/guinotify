#!/bin/bash

# FOR TESTING PURPOSES ONLY !!!

sudo cp -v guinotify.png /usr/share/pixmaps/
sudo cp -v guinotify.desktop /usr/share/applications/
cp -v guinotify.desktop ~/Desktop/guinotify.desktop

xgettext -d guinotify -o locales/guinotify.pot *.py
#poedit 2>/dev/null

#python setup.py sdist
#python -m build --wheel --no-isolation
#updpkgsums
#makepkg -fci

#install -Dm755 guinotify.py /usr/bin/guinotify

#xdg-open ~/Desktop/GameInfo.desktop
python -m guinotify
#GoalFM.py