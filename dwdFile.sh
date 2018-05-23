#!/bin/bash
while true
do
array=("NY" "CA" "IL" "TX" "AZ" "PA" "FL")
if [ ! -f tagsoup-1.2.1.jar ]
then
	echo "**************************************************"
	echo "NOTICE!!!! tagsoup-1.2.1.jar not found"
	echo "Downloading TagSoup..3..2..1"
	echo "**************************************************"
	wget http://vrici.lojban.org/~cowan/XML/tagsoup/tagsoup-1.2.1.jar
fi

for((i=0;i<${#array[@]};i++))
do
Date=$(date +"%Y-%m-%d-%l-%M-%S-${array[$i]}.html")
	case ${array[$i]} in
	NY)
		wget -O $Date https://forecast-v3.weather.gov/point/40.78,-73.97?view=plain
	;;
	CA)
		wget -O $Date https://forecast-v3.weather.gov/point/34.02,-118.45?view=plain 
	;;
	IL)
		wget -O $Date https://forecast-v3.weather.gov/point/41.78,-87.76?view=plain 
	;;
	TX)
		wget -O $Date https://forecast-v3.weather.gov/point/29.64,-95.28?view=plain 
	;;
	AZ)	
		wget -O $Date https://forecast-v3.weather.gov/point/33.69,-112.07?view=plain 
	;;
	PA)	
		wget -O $Date https://forecast-v3.weather.gov/point/40.08,-75.01?view=plain 
	;;
	FL)	
		wget -O $Date https://forecast-v3.weather.gov/point/30.23,-81.67?view=plain 
	;;
	esac
java -jar tagsoup-1.2.1.jar --files $Date
python3 WebsiteParser.py
done
sleep 3600
done

#java -jar tagsoup-1.2.1.jar --files yyyy-mm-dd-hh-mm-ss-AB.html
