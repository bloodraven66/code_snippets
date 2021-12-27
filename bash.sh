#separate text in file by delimiter

cat filename.txt | cut -d "|" -f 1 >> outfilename.txt

#bash parallel run while iterating through files in folder

NR_CPUS=40
job_count=0
for filename in $1/*
do
  {
  commands
  ...
  } &
  job_count=$((job_count+1))
  if [ "$job_count" -eq $NR_CPUS ]; then
        wait
        job_count=0
  fi
done
wait

#Example: get smaple rate and duration of all files in a folder, command=
  {
    dur=("`ffmpeg -i $filename 2>&1 | grep Duration | cut -d ' ' -f 4 | sed s/,// | awk -F: '{ print ($1 * 3600) + ($2 * 60) + $3 }'`  ")
  	sr=$(sox --i -r $filename)
    if [ $? -eq 0 ]; then
      echo ${filename##*/}, $dur, $sr >> ${1##*/}.txt
    else
      echo skipped  ${filename##*/}
    fi

  } &

#sum of all lines in file

cat filename | cut --d ',' -f2 | paste -sd+ | bc

#conditional sum with awk
cat filename | awk -F, '{if ($2<60 &&  $2>50) print $2}' | paste -sd+ | bc

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


