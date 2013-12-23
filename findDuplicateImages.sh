index=$(tempfile)
dupmd5sumfile=$(tempfile)

find "${1}" -type f -iname '*.jpg' -exec md5sum {} \; > ${index}
#time find "${1}" -type f -iname '*.jpg' -exec identify -format "%# %M\n" {} \; > index2.txt 

cut -c1-33 ${index} | sort | uniq -c -d | awk '{print $2}' > ${dupmd5sumfile}
while read line
do 
  echo '====='
  grep "$line" ${index}
done < ${dupmd5sumfile}
