#!/bin/bash
find $1  -mindepth 2 -maxdepth 2  -type d -mtime -2 >album_path.txt
./scan.rb
./album_art.rb $2
cd $2
rsync -av $2/* $3
