import os,datetime,csv
import win32security


f = open('./log.csv', 'w')

path = "Folder directory"

data1 = ['File name','Path','Last modified','Created date','Last accessed', 'Size','Level','Inside files','Inside dirs','Created by']

writer = csv.writer(f)
writer.writerow(data1)

tree = os.walk(path)
x = 1
name=''

for i in tree:
    pat=i[0]
    modificationTime = os.path.getmtime(i[0])
    creationTime = os.path.getctime(i[0])
    accessTime= os.path.getatime(i[0])
    fileSize = os.path.getsize(i[0])
    fromFirst = len(i[0].split('\\'))
    subFolders = len(i[0])

    totalFiles = 0
    totalDir = 0
    for base, dirs, files in os.walk(i[0]):
        for directories in dirs:
            totalDir += 1
        for Files in files:
            totalFiles += 1

    def get_file_owner(file_path:str):
        sd = win32security.GetFileSecurity (file_path, win32security.OWNER_SECURITY_INFORMATION)
        owner_sid = sd.GetSecurityDescriptorOwner()
        
        name, domain, type = win32security.LookupAccountSid (None, owner_sid)   
        
        data = [os.path.basename(i[0]), i[0], datetime.datetime.fromtimestamp(modificationTime), datetime.datetime.fromtimestamp(creationTime),datetime.datetime.fromtimestamp(fileSize),fileSize,fromFirst,totalFiles,totalDir,name]
        writer = csv.writer(f)
        writer.writerow(data)
        print()
        
    print(i[0])
    get_file_owner(i[0])
