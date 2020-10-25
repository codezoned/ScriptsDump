#!/bin/sh
date=`date +%Y-%m-%d`
time=`date +%H:%M`
logfile=/myuser/rsync/log/$date-$time.log
server=$HOSTNAME
mailto=foo@foo.org
sender="foo@foo.org"
mailbody=/myuser/rsync/body.txt

echo '*************************************'> $logfile
echo '                                     ' >> $logfile
echo '       Starting script `date`        ' >> $logfile
echo '                                     ' >> $logfile
echo "*************************************" >> $logfile 
echo "           $server                   " >> $logfile
echo "         date:   $date               " >> $logfile
echo "*************************************" >> $logfile

rsync -avzPh /dirtobecopied rsyncserver.org::modulename/ >> $logfile

echo "*************************************" >> $logfile
echo " Files has been copied! $time - $date" >> $logfile
mail -s "RSYNC $server $dia" -r $sender $mailto  < $mailbody
echo '**************************************' >> $logfile

echo '                                      ' >> $logfile
echo 'Done at `date`                        ' >> $logfile
echo '                                      ' >> $logfile
echo '**************************************' >> $logfile

exit
