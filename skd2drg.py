#!/usr/bin/env python3 
# AKIMOTO
# 2025-03-20

import datetime, os, sys, argparse

skd = sys.argv[1]
skd_read = open(skd, "r").readlines()

exper = ""
sources = ""
drg_line = ""
flag = False
for lines in skd_read :
    
    line = lines.split()
    
    if "$EXPER" in line :  exper = lines
        
    if "2000.0" in line :  sources += lines
    
    if "$SKED"  in line :  flag = True
    
    if flag and "$SKED" != line[0] : 
        drg_line += "%-8s  30 s2  PREOB %s  %5s  MIDOB 0 POSTOB K-L-H-T- 1F00000 1F00000 1F00000 1F00000 YNNN\n" % (line[0], line[1], line[2])
    

drg = f"""{exper}*P.I.: HogeHoge
*Correlator: GICO3
*
$PARAM
SYNCHRONIZE ON
$SOURCES
{sources}*
$STATIONS
* ANTENNA INFORMATION
A  K YAMAGU32 AZEL   0.00   15.0    0.0    2.0  358.0   15.0    0.0    5.0   85.0   32.0 YM YM
A  H HITACHI  AZEL   0.00   12.0    0.0    2.0  358.0   12.0    0.0    5.0   85.0   32.0 HI HI
A  T TAKAHAGI AZEL   0.00    4.5    0.0   11.0  349.0    4.5    0.0    5.0   75.0   32.0 TA TA
A  L YAMAGU34 AZEL   0.00   15.0    0.0    2.0  358.0   15.0    0.0    5.0   85.0   34.0 YG YG
* STATION POSITION INFORMATION
P YM YAMAGU32 -3502544.5870  3950966.2350  3566381.1920 00000000
P HI HITACHI  -3961789.1650  3243597.5310  3790597.7000 00000000
P TA TAKAHAGI -3961882.0160  3243372.5190  3790687.4570 00000000
P YG YAMAGU34 -3502567.5760  3950885.7340  3566449.1150 00000000
* MARK III TERMINALS
T YM YAMAGU32 12
T HI HITACHI  14
T TA TAKAHAGI 14
T YG YAMAGU34 12
*
$SKED
*SOURCES CAL FR          START     DUR       IDLE       STATIONS  TAPE
{drg_line}*
$HEAD
* Head position information for MkIIIA recorders
H s2 11(-319) 21(31) 31(-271) 41(79) 51(-223) 61(127) 71(-175) 81(175) 91(-127)
H s2 A1(223) B1(-79) C1(271) D1(-31) E1(319)
*
$CODES
*
"""

drg_name = "%s/%s.DRG" % (os.path.dirname(skd), exper.split()[1].upper())
drg_output = open(drg_name, "w")
drg_output.write(drg)
drg_output.close()

print(f"Make {drg_name}")
