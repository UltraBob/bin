bin
===

test scripts and scripts that I use for automating my system

*tvcast.py* reads the files in a directory, finds the files that have a mimetype, sorts them in descending order by mtime and spits out an rss feed with enclosures.

*vidhunter.py* is used in conjunction with a LaunchDaemon to watch a folder where video files are downloaded.  when new files show up this script is run, it scans for compressed files and uncompresses them, then scans again to find video files.  It triggers converttotvcast.sh with a list of video files if there are any, or sends an e-mail warning that there was no video file.  Once the shell script successfully returns, this script wipes out all the files it has already scanned.

*converttotvcast.sh* this script takes a list of files and feeds them to handbrakeCLI to convert and move to the desired location
