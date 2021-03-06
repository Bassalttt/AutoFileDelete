import os;
import shutil;
from datetime import datetime;

FMT = '%Y-%m-%d %H:%M:%S';
currentTime=datetime.now().strftime(FMT);
print('Current time:{}'.format(currentTime));

def Setting():
    import sys;
    s=input("Set the time by second or day(default)? Please enter sec or day:");
    if(s==''):return 'day';
    elif(s=='sec' or s=='day'):
        return s;
    else:sys.exit("No such option.");

def PathCheck(pc):
    return os.path.exists(pc);

def DeleteTime():
    if(s=='day'):
        t=input("How many days do your files should exist:(default=7)");
        if(t==''):t=7;
        print("Remove the files that exist longer than {} days.".format(t));
    else:
        t=input("How many seconds do your files should exist:(default=1000)");
        if(t==''):t=1000;
        print("Remove the files that exist longer than {} seconds.".format(t));
    return int(t);

def DeletePath():
    p=input("The path of the file that you wish to clean:");
    if(PathCheck(p)==True):
        print("Clean the files in the path '{}'.".format(p));
        print("==========\n");
    else:print('Missing the file');
    return p;

def CombinePath(parentPath,chidFile,con):
    targets=[];
    for i in range(0,len(con)): #file
        fullPath=os.path.join(parentPath,con[i]);
        if(PathCheck(fullPath)==True):
            targets.append(fullPath);
        else:print("\n~~~~~~~~~~~~~~~\n{} is not a path.\n\n".format(fullPath));
    for i in range(0,len(chidFile)): #folder
        fullPath=os.path.join(parentPath,chidFile[i]);
        targets.append(fullPath);
    return targets;

def FileCreationDate(filePath): #creation time for windows
    t=os.path.getctime(filePath);
    t=datetime.fromtimestamp(t).strftime(FMT);
    return t;

def RemoveFile(rf):
    try: os.remove(rf);#a file
    except PermissionError:shutil.rmtree(rf); #a directory and everything in it
    dFile=os.path.split(rf)[-1];
    print("The file '{}' has been deleted!!!!!.".format(rf));
    return 0;

def JudgeAndDelete(JDpath):
    fileTime=FileCreationDate(JDpath);
    print("The creation date of the file: {}".format(fileTime));
    duringTime=datetime.strptime(currentTime, FMT) - datetime.strptime(fileTime, FMT);
    if(s=='sec'):
        dtSec=duringTime.seconds;
        print("The file has existed for {} seconds long.".format(dtSec));
        if(dtSec>existTime):RemoveFile(JDpath);
    else:
        dtDay=duringTime.days;
        print("The file has existed for {} days long.".format(dtDay));
        if(dtDay>existTime):RemoveFile(JDpath);
    print("\n---\n");
    return 0;

#=============================================================
s=Setting();
existTime=DeleteTime();
thePath=DeletePath();
print("")
i=0;
for path,file,cont in os.walk(thePath):
    i=i+1;
    if(file==[] and cont==[]):RemoveFile(path);
    elif(file== 'Allen' or file=='Simon' or file=='Dylan' or
         file=='DL' or file=='Frank' or file=='Paul'):continue;
    else:
        target=CombinePath(path,file,cont);
        for every in target:
            print("Target file: {}".format(every));
            JudgeAndDelete(every);
