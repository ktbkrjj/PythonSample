#!/usr/bin/python
# coding: UTF-8
 
import re

# 対象のファイルをすべて読み込む
readf = open('test.txt')
lines = readf.readlines()
readf.close()

# 検索する文字列パターンを指定
pattern = r"[0-9]+,[0-9]+,[0-9]+,[0-9]+"

writef = open('out.txt', 'w')
for line in lines:
    match = re.search(pattern, line)
    # 読み込んだ行に指定したパターンが含まれる場合
    if match:
        nArray = re.findall(r"[0-9]+", match.group())
        # 3つ目の数字をインクリメント
        nArray[2] = str(int(nArray[2]) + 1)
        newVersion = nArray[0] + ',' + nArray[1] + ',' + nArray[2] + ',' + nArray[3]
        line = line.replace(match.group(), newVersion)
    writef.write('%s' % (line))
writef.close()
