#!/bin/sh

for f in "$@"
do
	# SET YOUR OUTPUT DIRECTORY
	outputDir="/Volumes/Hedonismbot/tvtransit"
	# SET YOUR OUTPUT FILE EXTENSION (MP4/MKV/M4V)
	outputFileExt="mp4"
	
	inputFileExt=`echo "$f" | sed 's|.*\.||'`
	inputFileNameNoExt=`basename "$f" ".${inputFileExt}"`

	HandBrakeCLI -i "$f" -o "${outputDir}/${inputFileNameNoExt}.${outputFileExt}" -Z "iPad" --native-language eng --native-dub 　&& mv "${outputDir}/${inputFileNameNoExt}.${outputFileExt}" /Volumes/Hedonismbot/tvcast
done