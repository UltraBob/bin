import pyexiv2, os, sys

base_path = '/Volumes/Temp/Aperture Export'
from_folder = 'Orientation'
to_folder = 'Keywords'
start_path = os.path.join(base_path, from_folder)
dest_path = os.path.join(base_path, to_folder)
print start_path

extensions = ['.jpg', '.jpeg']
file_list = []

for root, dirs, files in os.walk(start_path):
    for name in files:
        for extension in extensions:
            if name.lower().endswith(extension):
                file_list.append(os.path.join(root, name))
i = 1
skipped = 0
#print file_list
for file in file_list:
    i+=1
    if i % 1000 == 0:
        print "currently processing", file, "which is file #", i, "of", len(file_list), "(", float(i) / len(file_list) * 100, "%) (", skipped, "files skipped)"
    dest_file = file.replace(start_path, dest_path)
    if not (os.path.exists(dest_file) and os.path.isfile(dest_file)):
        print dest_file, "doesn't exist" #continue
        continue
    else:
        #print "replacing metadata in", dest_file, "with metadata from", file
        source_metadata = pyexiv2.ImageMetadata(file)
        dest_metadata = pyexiv2.ImageMetadata(dest_file)
        try:
            source_metadata.read()
            dest_metadata.read()
        except IOError:
            print "failed to read data for", file
            continue
        if 'Exif.Image.Orientation' in source_metadata:
            dest_metadata['Exif.Image.Orientation'].value = source_metadata['Exif.Image.Orientation'].value
        else:
            skipped += 1
        dest_metadata.write()
exit()

if len(file_list) > 0:
    for file in file_list:
        metadata = pyexiv2.ImageMetadata(file)
        metadata.read()
        if 'Exif.Thumbnail.Orientation' in metadata:
            print "processing", file
            thumbOrientation = metadata['Exif.Thumbnail.Orientation']
            imageOrientation = metadata['Exif.Image.Orientation']
            print file, "Thumbnail Orientation:", thumbOrientation, "Image Orientation:", imageOrientation
            if thumbOrientation.value != imageOrientation.value:
                imageOrientation.value = thumbOrientation.value
                metadata.write()
