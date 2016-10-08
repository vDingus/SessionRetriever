for i in $(cat raw_download_urls.txt);
do
  LABEL=$(echo $i | awk -F ',' '{print $1}')
  URL=$(echo $i | awk -F ',' '{print $2}')
  curl -o "${LABEL}.mp4" "${URL}"
done