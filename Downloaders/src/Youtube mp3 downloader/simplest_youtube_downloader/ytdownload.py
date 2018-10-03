from __future__
import unicode_literals

import youtube_dl

ydl_opts = {}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:

  ydl.download([raw_input("Enter the url :").strip()])
