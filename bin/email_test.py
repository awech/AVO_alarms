#!/usr/bin/env python
import os
import sys
from obspy import UTCDateTime

sys.path.append(work_dir)
from alarm_codes import utils
os.chdir(work_dir)

if os.getenv('FROMCRON') == 'yep':
    file=os.environ['LOGS_DIR']+'/Email_test-'+UTCDateTime.now().strftime('%Y%m%d-%H')+'.out'
    os.system('touch {}'.format(file))
    f=open(file,'a')
    sys.stdout=sys.stderr=f


message = 'Body'
subject = 'Alarm Email Test'
attachment=os.environ['HOME_DIR']+'/alarm_aux_files/oops.jpg'

utils.send_alert('Error',subject,message,attachment)