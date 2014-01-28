#!/usr/bin/python
import mimetypes, os, urllib, time, datetime, sys
from operator import attrgetter

try:
    from tvcast_config import *
except ImportError:
    pass

class File:
    def __init__(self, file, mime, size, url, mtime, pubdate):
        self.file = file
        self.mime = mime
        self.size = size
        self.url = url
        self.mtime = mtime
        self.pubdate = pubdate
    def __repr__(self):
        return repr((self.file, self.mime, self.size, self.url, self.mtime, self.pubdate))
        
filelist = [ f for f in os.listdir(start_path) if os.path.isfile(os.path.join(start_path,f)) and not f.startswith('.')] # get a listing of this directory exclluding subdirectories and hidden files
#print filelist

file_objects = []

#print filelist

for file in filelist:
    #print start_path + file
    try:
        statinfo = os.stat(start_path + file)
    except:
        print sys.exc_info()
    #print statinfo
    mimetype = str(mimetypes.guess_type(urllib.pathname2url(file))[0])
    if mimetype != "None":
        file_objects.append(File(file, mimetype, str(statinfo.st_size), url_path + file, str(statinfo.st_mtime), datetime.datetime.fromtimestamp(statinfo.st_mtime).strftime("%a, %d %b %Y %H:%M:%S +0900")))
    
sorted_files = sorted(file_objects, key=attrgetter('mtime'), reverse=True)
    

print '<?xml version="1.0" encoding="utf-8"?>'
print '<rss xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd" version="2.0">'
print ' <channel>'
print '     <description>tvcast</description>'
print '     <link>{}</link>'.format(link)
print '        <title>TVCast</title>'
print '     <pubDate>{}</pubDate>'.format(time.strftime("%a, %d %b %Y %H:%M:%S +0900"))

for file in sorted_files:
    print "         <item>"
    print "             <title>{}</title>".format(file.file)
    print '             <enclosure type="{}" length="{}" url="{}" />'.format(file.mime, file.size, file.url)
    print "             <pubDate>{}</pubDate>".format(file.pubdate)
#    print "             <description>Mtime: {}, size: {}, pubdate: {}</description>".format(file.mtime, file.size, file.pubdate)
    print "             <guid>{}{}</guid>".format(file.mtime, file.size)
    print "         </item>"
        
print " </channel>\n</rss>"
