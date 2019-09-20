#/usr/bin/bash
python3 htmlDownload.py
python3 parser.py
python3 pgDown.py
mv *.png problems/
