#!/bin/bash


################################################################################
# SCRIPT_COMMON_CONFIG
################################################################################
export TODAY_TIMESTAMP_FULL=`date +"%Y%m%d_%H%M%S"`
export TODAY_TIMESTAMP_DATE=`date +"%Y%m%d"`


################################################################################
# APP_CONFIG
################################################################################
export APP_NAME=notifyOutboundIP_LINE
export APP_HOME=/home/colaman/WORKS/WORKS_COLAMAN/pythonWorks/notifyOutboundIP_LINE
export APP_LOG=$APP_HOME/logs/$APP_NAME.log.$TODAY_TIMESTAMP_DATE.txt
export FILE_OUTBOUND_IP=/home/colaman/WORKS/WORKS_COLAMAN/networkWorks/checkOutboundIP/data/ip.txt
export FILE_LINE_ACCESS_TOKEN=/home/colaman/WORKS/WORKS_COLAMAN/pythonWorks/notifyOutboundIP_LINE/conf/line_access_token.txt


################################################################################
# APP_EXECUTE
################################################################################
cd $APP_HOME/src
/usr/bin/python3 $APP_HOME/src/notifyOutboundIP.py $FILE_LINE_ACCESS_TOKEN $FILE_OUTBOUND_IP >> $APP_LOG

