#Python script to delete recycle bin contents with CLI without displaying that annoying progess bar but with a cool sound!

import winshell
winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
