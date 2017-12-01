import pylast
from credentials import *

# Authentication
password_hash = pylast.md5("PASSWORD")
network = pylast.LastFMNetwork(api_key=KEY, api_secret=SECRET,
                               username=USERNAME, password_hash=password_hash)
