import re, shutil, time, glob

outfilename = 'all_' + str((int(time.time()))) + ".txt"

with open(outfilename, 'wb') as outfile:
    for filename in glob.glob('*.srt'):
        if filename == outfilename:
            # don't want to copy the output into the output
            continue
        with open(filename, 'rb') as readfile:
            shutil.copyfileobj(re.sub('0{2}:0.:.{2},.{3}|-->', '', readfile.read(), flags = re.M), outfile)

