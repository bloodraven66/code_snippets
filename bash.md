separate text in file by delimiter
```
cat filename.txt | cut -d "|" -f 1 >> outfilename.txt
```

fasttext classifier
```
./fasttext supervised -input . -output mr_4class -epoch 50 -wordNgrams 2
```
