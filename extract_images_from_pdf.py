# Extracts images from a file or file in directory using "pdfimages" command line program

from os.path import isfile, isdir
from subprocess import call
import os
import sys

file_or_path = sys.argv[1]
keyword = None
if len(sys.argv) > 2:
    keyword = sys.argv[2]

onlyfiles = []
if isdir(file_or_path):
    for root, directories, files in os.walk(file_or_path):
        for fname in files:
            addfile = False
            if (keyword is not None) and (keyword in fname.lower()):
                addfile = True
            elif keyword is None:
                addfile = True
            if addfile:
                print("adding", fname)
                onlyfiles.append(os.path.join(root, fname))

if isfile(file_or_path):
    onlyfiles = [file_or_path]

pdffiles = []

for fname in onlyfiles:
    fn_split, file_extension = os.path.splitext(fname)
    if file_extension == ".pdf":
        pdffiles.append(fname)

title_trans = ''.join(chr(c) if chr(c).isalnum() else '_' for c in range(256))

if not os.path.exists("images"):
    os.makedirs("images")

for fname in pdffiles:
    filename = os.path.splitext(os.path.basename(fname))[0]
    lower_f = filename.lower()
    lower_f = lower_f.translate(title_trans)
    print("will translate", fname, "to", lower_f)
    call(["pdfimages", fname, "images/"+lower_f])
