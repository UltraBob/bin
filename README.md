bin
===

test scripts and scripts that I use for automating my system

Useful Scripts and Stuff
====

*girl timer.html* This is a timer to help our twin pre-literate daughters to take turns.  One of them loves the color pink, and the other purple, so I fire up this page in the browser, and it randomly selects a color to start with.  It then switches colors every 3 minutes by default to let the girls know who's turn it is.  There is a field on the page to allow one to change the number of minutes to go between switches.  You can very easily break this script, there is no validation as it is for personal use and there is nothing to protect.

*tvcast.py* reads the files in a directory, finds the files that have a mimetype, sorts them in descending order by mtime and spits out an rss feed with enclosures.

*vidhunter.py* is used in conjunction with a LaunchDaemon to watch a folder where video files are downloaded.  when new files show up this script is run, it scans for compressed files and uncompresses them, then scans again to find video files.  It triggers converttotvcast.sh with a list of video files if there are any, or sends an e-mail warning that there was no video file.  Once the shell script successfully returns, this script wipes out all the files it has already scanned.

*converttotvcast.sh* this script takes a list of files and feeds them to handbrakeCLI to convert and move to the desired location

Experiments
====

*buttontest.py* a quick easygui test

*natvpn.sh* An script created when I was trying to figure out how to share my openVPN connection to other machines through my mac.  I went with a different solution in the end and never got this working.  I think it came from [http://rodrigo.sharpcube.com/2010/06/20/using-and-sharing-a-vpn-connection-on-your-mac/](http://rodrigo.sharpcube.com/2010/06/20/using-and-sharing-a-vpn-connection-on-your-mac/)

*stattest.sh* a little test script to look at the stat command.  This helped me figure out what to do in tvcast.py

*test.py* This pops up an easygui window with the working directory and creates a file if it doesn't exist and writes the wroking directory there too.

*walklater.py* This is an experiment with walking through a file tree using os.walk, this jhelped me figure out vidhunter
