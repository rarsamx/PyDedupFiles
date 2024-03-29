index=$(mktemp)
dupmd5sumfile=$(mktemp)


#find "${1}" -type f -iname '*.jpg' -exec md5sum {} \; | sort --key=2 --ignore-case > ${index}
find "${1}" -type f -iname '*.jpg' -exec identify -format "%#  %M" {} \; > ${index} #| sort --key=2 --ignore-case > ${index}

cut -c1-33 ${index} | sort | uniq -c -d | awk '{print $2}' > ${dupmd5sumfile}
while read line
do 
  echo '====='
  grep "$line" ${index}
done < ${dupmd5sumfile}
