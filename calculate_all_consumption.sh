#!/bin/bash

export PROJECT='gen6035'

# Follow project consumption:
DATE=`date --rfc-3339=date`
TOTAL=`ccc_myproject |grep Total |head -3| tail -1 |awk '{print $2}'`
ALLOC=`ccc_myproject |grep Alloc |head -3| tail -1 |awk '{print $2}'`
if [ -f /ccc/cont003/dsku/blanchet/home/user/ige/jourdain/CONSO_GROUPE/consommation_proj_${PROJECT}.txt ]; then
  LAST_DATE=`tail -1 consommation_proj_${PROJECT}.txt | awk '{print $1}'`
  if [ ! $LAST_DATE == $DATE ]; then
    echo "$DATE $TOTAL $ALLOC" >> /ccc/cont003/dsku/blanchet/home/user/ige/jourdain/CONSO_GROUPE/consommation_proj_${PROJECT}.txt
    for USER in cailletj mathiotp chekkimo kittelch mosbeuxc
    do
      CONS=`ccc_myproject -P rome -a |grep ${USER} |head -1 |awk '{print $2}'`
      echo "$DATE $CONS" >> /ccc/cont003/dsku/blanchet/home/user/ige/jourdain/CONSO_GROUPE/consommation_proj_${PROJECT}_${USER}.txt 
    done
    CONS=`ccc_myproject -P rome -a |grep jourdain |head -2 |tail -1 |awk '{print $2}'`
    echo "$DATE $CONS" >> /ccc/cont003/dsku/blanchet/home/user/ige/jourdain/CONSO_GROUPE/consommation_proj_${PROJECT}_jourdain.txt
  fi
fi
RATIO=`echo "100 * $TOTAL / $ALLOC" |bc -l |cut -d '.' -f1`
echo "Consommation au $DATE : $TOTAL / $ALLOC  (${RATIO}%)"
