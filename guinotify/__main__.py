import gettext
from .guinotify import guinotifyApp

if __name__ == "__main__":
    gettext.install("guinotify") # replace with the appropriate catalog name

    guinotify = guinotifyApp(0)
    guinotify.MainLoop()
