import gettext
from .guinotify import guinotifyApp

def main():

    gettext.install("guinotify") # replace with the appropriate catalog name

    guinotify = guinotifyApp(0)
    guinotify.MainLoop()

if __name__ == "__main__":
    main()