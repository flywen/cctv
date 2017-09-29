#!/usr/bin/env python
import os
import datetime


yes_date = (datetime.datetime.now()+datetime.timedelta(days=-1)).strftime('%Y%m%d')

def getfilename():
    for i,j,k in os.walk(yes_date):
        k.sort()
        return k

for i in range(0,23):
    f = open('yes_date/'+'play'+i.zfill(2)+'.m3u8','w')
    f.write('#EXTM3U'+'\n'+'#EXT-X-VERSION:3'+'\n'+'#EXT-X-TARGETDURATION:2'+'\n'+'#EXT-X-MEDIA-SEQUENCE:0'+'\n')
    f.close()
    filename = getfilename()
    for j in filename:
        f = open('yes_date/'+'play'+i.zfill(2)+'.m3u8','a')
        if  j[:2] == i.zfill(2):
            f.write('#EXTINF:2.000000,'+'\n')
            f.write(j+'\n')
    f.write('#EXT-X-ENDLIST'+'\n')
    f.close()
