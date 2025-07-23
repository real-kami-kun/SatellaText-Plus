## sattxtup.py - schedule updater for SatellaText

# import libraries
import xml.etree.ElementTree as ET

"""
TTI READ CODE
"""
def PROC_readTTI():
    ttxBuf = [' ']
    tti = open('base-s.tti','rb')
    ttxBuf.clear()
    for x in tti:
        ttxBuf.append(x)
    tti.close()


"""
TIME CONVERTER
"""
def FN_timeConv(time, utc = False):
    match time:
        case "08:00":
            eTime = "0800"
            uTime = "1200"
        case "11:00":
            eTime = "1100"
            uTime = "1500"
        case "14:00":
            eTime = "1400"
            uTime = "1800"
        case "17:00":
            eTime = "1700"
            uTime = "2100"
        case "20:00":
            eTime = "2000"
            uTime = "0000"
        case "23:00":
            eTime = "2300"
            uTime = "0300"
    if utc:
        return uTime
    else:
        return eTime


"""
XML SETUP
"""
aConf = True
aConfDlg = False
xTree = ET.parse('sched.xml')
xRoot = xTree.getroot()
print(xRoot)
print(xRoot.attrib)
while aConfDlg == False:
    aUsrIn = input("CHECK THAT THIS IS THE CORRECT FILE.\nIf so, type \"Y\".\nIf not, type \"N\".\nCorrect: ")
    match aUsrIn:
        case "Y" | "y":
            aConfDlg = True
        case "N" | "n":
            aConf = False
            aConfDlg = True
        case _:
            aConfDlg = False
if aConf == False:
    raise UserWarning("Process aborted.")
tFoldIds = ('2', '1', '7', '16', '19', '0', '15') # Station, News, Stadium, Temple, Booth, Tower, Plaza
# designations: (N)ews Wall, (S)tadium, (B)agpotamia Temple,
#               (P)hone Booth, Robot (T)ower, (E)vent Plaza

"""
DICTIONARY INIT
"""
dGame1 = {
    "name" : "````````````````",
    "stime" : "20:00",
    "etime" : "20:00",
    "e_stime" : "2000",
    "e_etime" : "2000",
    "u_stime" : "0000",
    "u_etime" : "0000"
}
dGame2 = {
    "name" : "````````````````",
    "stime" : "20:00",
    "etime" : "20:00",
    "e_stime" : "2000",
    "e_etime" : "2000",
    "u_stime" : "0000",
    "u_etime" : "0000"
}
dGame3 = {
    "name" : "````````````````",
    "stime" : "20:00",
    "etime" : "20:00",
    "e_stime" : "2000",
    "e_etime" : "2000",
    "u_stime" : "0000",
    "u_etime" : "0000"
}
dGame4 = {
    "name" : "````````````````",
    "stime" : "20:00",
    "etime" : "20:00",
    "e_stime" : "2000",
    "e_etime" : "2000",
    "u_stime" : "0000",
    "u_etime" : "0000"
}
dGame5 = {
    "name" : "````````````````",
    "stime" : "20:00",
    "etime" : "20:00",
    "e_stime" : "2000",
    "e_etime" : "2000",
    "u_stime" : "0000",
    "u_etime" : "0000"
}
dGameMisc = {
    "isNews" : False,
    "nName" : "````````````````",
    "isStad" : False,
    "sName" : "````````````````",
    "isTemp" : False,
    "bName" : "````````````````",
    "isPhon" : False,
    "pName" : "````````````````",
    "isTowr" : False,
    "tName" : "````````````````",
    "isEvnt" : False,
    "eName" : "````````````````"
}
dGameList = {
    "count" : 5,
    "game1" : dGame1,
    "game2" : dGame2,
    "game3" : dGame3,
    "game4" : dGame4,
    "game5" : dGame5,
    "other" : dGameMisc
}

"""
DICTIONARY WRITING CODE
"""
def FN_dGameWrite():
    global xFold
    aFileCount = 1
    for xFile in xFold.findall('file'):
        xPName = xFile.attrib["name"]
        xPStart = xFile.attrib["starttime"]
        xPEnd = xFile.attrib["endtime"]
        match xFold.attrib["id"]:
            case "2" if aFileCount == 1:
                dGame1.update({"name" : xFile.attrib["name"],
                               "stime" : xFile.attrib["starttime"],
                               "etime" : xFile.attrib["endtime"],
                               "e_stime" : FN_timeConv(xPStart),
                               "e_etime" : FN_timeConv(xPEnd),
                               "u_stime" : FN_timeConv(xPStart,True),
                               "u_etime" : FN_timeConv(xPEnd,True)})
                aFileCount += 1
                dGameList.update({"count" : 1})
            case "2" if aFileCount == 2:
                dGame2.update({"name" : xFile.attrib["name"],
                               "stime" : xFile.attrib["starttime"],
                               "etime" : xFile.attrib["endtime"],
                               "e_stime" : FN_timeConv(xPStart),
                               "e_etime" : FN_timeConv(xPEnd),
                               "u_stime" : FN_timeConv(xPStart,True),
                               "u_etime" : FN_timeConv(xPEnd,True)})
                aFileCount += 1
                dGameList.update({"count" : 2})
            case "2" if aFileCount == 3:
                dGame3.update({"name" : xFile.attrib["name"],
                               "stime" : xFile.attrib["starttime"],
                               "etime" : xFile.attrib["endtime"],
                               "e_stime" : FN_timeConv(xPStart),
                               "e_etime" : FN_timeConv(xPEnd),
                               "u_stime" : FN_timeConv(xPStart,True),
                               "u_etime" : FN_timeConv(xPEnd,True)})
                aFileCount += 1
                dGameList.update({"count" : 3})
            case "2" if aFileCount == 4:
                dGame4.update({"name" : xFile.attrib["name"],
                               "stime" : xFile.attrib["starttime"],
                               "etime" : xFile.attrib["endtime"],
                               "e_stime" : FN_timeConv(xPStart),
                               "e_etime" : FN_timeConv(xPEnd),
                               "u_stime" : FN_timeConv(xPStart,True),
                               "u_etime" : FN_timeConv(xPEnd,True)})
                aFileCount += 1
                dGameList.update({"count" : 4})
            case "2" if aFileCount == 5:
                dGame5.update({"name" : xFile.attrib["name"],
                               "stime" : xFile.attrib["starttime"],
                               "etime" : xFile.attrib["endtime"],
                               "e_stime" : FN_timeConv(xPStart),
                               "e_etime" : FN_timeConv(xPEnd),
                               "u_stime" : FN_timeConv(xPStart,True),
                               "u_etime" : FN_timeConv(xPEnd,True)})
                dGameList.update({"count" : 5})
            case "1":
                dGameMisc.update({"isNews" : True,
                                  "nName" : f"{xPName}"})
            case "7":
                dGameMisc.update({"isStad" : True,
                                  "sName" : f"{xPName}"})
            case "16":
                dGameMisc.update({"isTemp" : True,
                                  "bName" : f"{xPName}"})
            case "19":
                dGameMisc.update({"isPhon" : True,
                                  "pName" : f"{xPName}"})
            case "0":
                dGameMisc.update({"isTowr" : True,
                                  "tName" : f"{xPName}"})
            case "15":
                dGameMisc.update({"isEvnt" : True,
                                  "eName" : f"{xPName}"})
    print(dGameList)
for id in tFoldIds:
    for xFold in xRoot[1][0].findall('folder'):
        if xFold.attrib["id"] == id:
            print(xFold.attrib)
            xFound = True
            break
    if xFound:
        print("Found:",xFold.attrib["name"])
        FN_dGameWrite()

"""
TTI WRITING CODE
"""
PROC_readTTI()

def PROC_writeTTI():
    
    ttxGame1 = dGame1["name"].upper()
    ttxTime1E = str(dGame1["e_stime"] + "-" + dGame1["e_etime"])
    ttxTime1U = str(dGame1["u_stime"] + "-" + dGame1["u_etime"])
    ttxGame2 = dGame2["name"].upper()
    ttxTime2E = str(dGame2["e_stime"] + "-" + dGame2["e_etime"])
    ttxTime2U = str(dGame2["u_stime"] + "-" + dGame2["u_etime"])
    if len(ttxGame2) > 19:
        ttxGame2 = ttxGame2[:20]
    ttxGame2 = ttxGame2.ljust(19)
    ttxGame3 = dGame3["name"].upper()
    ttxTime3E = str(dGame3["e_stime"] + "-" + dGame3["e_etime"])
    ttxTime3U = str(dGame3["u_stime"] + "-" + dGame3["u_etime"])
    if len(ttxGame3) > 17:
        ttxGame3 = ttxGame3[:18]
    ttxGame3 = ttxGame3.rjust(17)
    ttxGame4 = dGame3["name"].upper()
    ttxTime4E = str(dGame3["e_stime"] + "-" + dGame3["e_etime"])
    ttxTime4U = str(dGame3["u_stime"] + "-" + dGame3["u_etime"])
    ttxGame5 = dGame4["name"].upper()
    ttxTime5E = str(dGame4["e_stime"] + "-" + dGame4["e_etime"])
    ttxTime5U = str(dGame4["u_stime"] + "-" + dGame4["u_etime"])
    ttxGame6 = dGame5["name"].upper()
    ttxTime6E = str(dGame5["e_stime"] + "-" + dGame5["e_etime"])
    ttxTime6U = str(dGame5["u_stime"] + "-" + dGame5["u_etime"])
    ttxNews = dGameMisc["nName"].upper()
    ttxStad = dGameMisc["sName"].upper()
    ttxTemp = dGameMisc["bName"].upper()
    ttxPhon = dGameMisc["pName"].upper()
    ttxTowr = dGameMisc["tName"].upper()
    ttxEvnt = dGameMisc["eName"].upper()
        
    tti = open("//pages//SVP101.tti","wt")
    toWrite = f"""DE,BS schedule
DS,inserter
SP,C:\\Users\\Ben\\ttx\\svp\\pages\\SVP101.tti
PN,10101
SC,0001
PS,8000
CT,8,T
RE,0
OL,0,        SATVW+ %%# %%a%d %%b TXT\x1bC%H%M:%S
OL,1,\x1b]\x1bT\x7f+\x7d ~//  "ot?! \x1bT ||| | | | ||t |||    
OL,2,\x1b]\x1bU\x7fnw +m4\x7f\x7f  \x7f5  \x1bT \x7f(| \x7f \x7f \x7f \x7f \x7f \x7f,,    
OL,3,\x1b]\x1bS\x7fx? ||=  `~"ot \x1bT /// /// / //' ///    
OL,5,  TONIGHT:                              
OL,6,\x1bM\x1bA{ttxGame1}
OL,8,\x1bL\x1bG{ttxTime1E} EST                         
OL,9, \x1bB{ttxTime1U} UTC                         
OL,10, \x1bELOCATION: BROADCAST STN.              
OL,11,  =========================             
OL,16,  LATER:                                
OL,17,\x1bM\x1bA{ttxGame2}{ttxGame3}\x1bL 
OL,19,  {ttxTime2E} EST    ||    {ttxTime3E} EST  
OL,20, \x1bB{ttxTime2U} UTC    ||    {ttxTime3U} UTC  
OL,21, \x1bEBROADCAST STN.   ||    BROADCAST STN  
OL,23,\x1bD\x1b]\x1bCSatellaview+: BS-X, without the BS  \x1b\
OL,24,\x1bAHome     \x1bBSoundLink+\x1bCInfoReel\x1bFIndex    
FL,100,200,152,199,8ff,199
PN,10102
SC,0002
PS,8000
CT,8,T
RE,0
OL,0,        SATVW+ %%# %%a%d %%b TXT\x1bC%H%M:%S
OL,1,\x1b]\x1bT\x7f+\x7d ~//  "ot?! \x1bT ||| | | | ||t |||    
OL,2,\x1b]\x1bU\x7fnw +m4\x7f\x7f  \x7f5  \x1bT \x7f(| \x7f \x7f \x7f \x7f \x7f \x7f,,    
OL,3,\x1b]\x1bS\x7fx? ||=  `~"ot \x1bT /// /// / //' ///    
OL,5,  LATER TONIGHT:                        
OL,6,\x1bM\x1bA{ttxGame4}
OL,8,  {ttxTime4E} EST                         
OL,9, \x1bB{ttxTime4U} UTC                         
OL,10, \x1bEBROADCAST STN.                        
OL,11,\x1bM\x1bA{ttxGame5} 
OL,13,  {ttxTime5E} EST                         
OL,14, \x1bB{ttxTime5U} UTC                         
OL,15, \x1bEBROADCAST STN.                        
OL,16,\x1bM\x1bA{ttxGame6}
OL,18,  {ttxTime6E} EST                         
OL,19, \x1bB{ttxTime6U} UTC                         
OL,20, \x1bEBROADCAST STN.                        
OL,23,\x1bD\x1b]\x1bCSV+: Now adopting UTC!    See\x1bFp123  \x1b\
OL,24,\x1bAHome     \x1bBSoundLink+\x1bCInfoReel\x1bFIndex    
FL,100,200,152,199,8ff,199
PN,10103
SC,0003
PS,8000
CT,8,T
RE,0
OL,0,        SATVW+ %%# %%a%d %%b TXT\x1bC%H%M:%S
OL,1,\x1b]\x1bT\x7f+\x7d ~//  "ot?! \x1bT ||| | | | ||t |||    
OL,2,\x1b]\x1bU\x7fnw +m4\x7f\x7f  \x7f5  \x1bT \x7f(| \x7f \x7f \x7f \x7f \x7f \x7f,,    
OL,3,\x1b]\x1bS\x7fx? ||=  `~"ot \x1bT /// /// / //' ///    
OL,5,  TONIGHT:                              
OL,6,\x1bM\x1bA{ttxNews}
OL,8,  0800-2300 EST                         
OL,9, \x1bB1200-0300 UTC                         
OL,10, \x1bENEWS WALL                             
OL,11,\x1bM\x1bC{ttxStad}
OL,13,  1100-2300 EST                         
OL,14, \x1bB1500-0300 UTC                         
OL,15, \x1bESTADIUM                               
OL,16,\x1bM\x1bB{ttxTemp}
OL,18,  0800-2300 EST                         
OL,19, \x1bB1200-0300 UTC                         
OL,20, \x1bETEMPLE                                
OL,23,\x1bD\x1b]\x1bCSatellaview+: BS-X, without the BS  \x1b\
OL,24,\x1bAHome     \x1bBSoundLink+\x1bCInfoReel\x1bFIndex    
FL,100,200,152,199,8ff,199
PN,10104
SC,0004
PS,8000
CT,8,T
RE,0
OL,0,        SATVW+ %%# %%a%d %%b TXT\x1bC%H%M:%S
OL,1,\x1b]\x1bT\x7f+\x7d ~//  "ot?! \x1bT ||| | | | ||t |||    
OL,2,\x1b]\x1bU\x7fnw +m4\x7f\x7f  \x7f5  \x1bT \x7f(| \x7f \x7f \x7f \x7f \x7f \x7f,,    
OL,3,\x1b]\x1bS\x7fx? ||=  `~"ot \x1bT /// /// / //' ///    
OL,5,  TONIGHT:                              
OL,6,\x1bM\x1bF{ttxPhon}
OL,8,  0800-2300 EST                         
OL,9, \x1bB1200-0300 UTC                         
OL,10, \x1bEPHONE BOOTH [300G]                    
OL,11,\x1bM\x1bD{ttxTowr}
OL,13,  1100-2300 EST                         
OL,14, \x1bB1500-0300 UTC                         
OL,15, \x1bEROBOT TOWER                           
OL,16,\x1bM\x1bE{ttxEvnt}
OL,18,  0800-2300 EST                         
OL,19, \x1bB1200-0300 UTC                         
OL,20, \x1bEEVENT PLAZA                           
OL,23,\x1bD\x1b]\x1bCSV+: Now adopting UTC!    See\x1bFp123  \x1b\
OL,24,\x1bAHome     \x1bBSoundLink+\x1bCInfoReel\x1bFIndex    
FL,100,200,152,199,8ff,199"""
    tti.write(toWrite)
    tti.close()

PROC_writeTTI()
