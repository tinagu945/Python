#!/usr/bin/env python3
'''Draw a plot showing the observed area (in RA, Dec)
of the Atacama Cosmology Telescope in 2016. The color
is based on the length of time the telecsope spent
in that area. Data file needed.'''
import matplotlib.cm as cm
import matplotlib as mpl
import matplotlib.image as mpimg
import sys
import numpy as np
import matplotlib.pyplot as plt
from pylab import *
fig, ax = plt.subplots()
latitude = -22.9586111111111;
longitude = -67.7875;
rad=0.01745329252;
pixel=1;
# create a numpy array
pic= uint8(np.zeros((200,450)));          
#print ("dec1 %s" % pic)
f=open('2017_final.txt');
for l in f:
    a=l.split();
    if a[0]=="askans_schedule":
        print (l.strip())
        continue;
    length=int((a[3]))-int(float(a[2]));
    alt=int(float(a[4]));
    throw=int(float(a[6]));
    az=int(float(a[5]));
    
    
    ctime1=int(float(a[2]));
    ctime2=int(float(a[3]));
    ctime=ctime1;
    while ctime<ctime2:
        julian= (ctime/86400.0) + 2440587.5;
        gmst = 18.697394558 + 24.06570982441908*(julian- 2451545.0)
        gmst -= floor(gmst/24.0)*24.0;
        lst = gmst+(longitude/15.0);
        lst -= floor(lst/24.0)*24.0;
        '''dec1 = math.asin(sin(alt*rad)*sin(latitude*rad) + cos(alt*rad)*cos(latitude*rad)*cos(az));
        dec1 = math.degrees(dec1);
        #print ("dec1 %s" % dec1)
        dec2 = math.asin(sin((alt+throw)*rad)*sin(latitude*rad) + cos((alt+throw)*rad)*cos(latitude*rad)*cos(az));
        dec2 = math.degrees(dec2);
        #print ("dec2 %s" % dec2)'''
        b=int(az-throw);
        while b<int(az+throw):
            dec1 = math.asin(sin(alt*rad)*sin(latitude*rad) + cos(alt*rad)*cos(latitude*rad)*cos(b*rad));
            LHA=math.degrees(math.asin((sin(alt*rad)-sin(dec1)*sin(latitude*rad))/(cos(dec1)*cos(latitude*rad))));
            if LHA<0:
                LHA = LHA+360;
            RA=int(lst*15-LHA);
            #print ("RA %s" % RA)
            dec1=int(math.degrees(dec1));
            #print ("dec %s" % dec1)
            '''if RA>0 and dec1>0:
                pic[dec1+90][RA+90]=min(300,(pic[dec1][RA]+uint8(length*0.8)));
            if RA>0 and dec1<0:
                pic[90+dec1][RA+90]=min(255,(pic[dec1][RA]+uint8(length*0.8)));
            if RA<0 and dec1<0:
                pic[90+dec1][60+RA]=min(255,(pic[dec1][RA]+uint8(length*0.8)));
            if RA<0 and dec1>0:
                pic[90+dec1][60+RA]=min(255,(pic[dec1][RA]+uint8(length*0.8)));
            #print ("dec1 %s" % pic)'''
        
            pic[90+(dec1/pixel)][90+(RA/pixel)]=min(255,(pic[dec1][RA]+uint8(length*0.5)));
            #print ("dec1 %s" % pic[dec1+90][RA+90])
            b=b+1;
        ctime=ctime+10;
'''xticks=([250, 200, 150, 100, 50, 0, -50])
ax.set_xticks(xticks, minor=False)
yticks=([-20,0,20])
ax.set_yticks(yticks, minor=False) 
ax.set_xlim(300, -60)
ax.set_ylim(-70, 30)'''

ax.imshow(pic,origin='lower',interpolation='gaussian', cmap=mpl.cm.get_cmap('jet'))
plt.ylabel('RA (deg)')
plt.xlabel('Dec (deg)')
fig.colorbar(pic, cax=cbar_ax)
plt.show()
        
        
  


