#separate text in file by delimiter

cat filename.txt | cut -d "|" -f 1 >> outfilename.txt


#fasttext classifier

./fasttext supervised -input . -output mr_4class -epoch 50 -wordNgrams 2


#Basename from path

path='folder/other_folder/file.js'
base=${path##*/}
echo ${base%.*} #(=file)

#duration from audio
dur=("`ffmpeg -i $filename 2>&1 | grep Duration | cut -d ' ' -f 4 | sed s/,// | awk -F: '{ print ($1 * 3600) + ($2 * 60) + $3 }'`  ")

#normalise audio
sox --norm=1 input.mp3 output.mp3

#stereo to mono audio
ffmpeg -y -v quiet -i input.mp3 -ac 1 output.mp3

#mp3 to wav
ffmpeg -v quiet -i input.mp3 output.wav 

#change sample rate
sox input.mp3 -r 16000 output.mp3


