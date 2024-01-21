import argparse
import os
from PIL import Image
# This import allows us to parse arguments from the command line



# global variable for the option

qual = 40               #sets the default quality of the image
type_file = '.jpg'      #set the default file type
file_replace = False

def removeFileName(file:str)->str:

    newPath = file
    if file.find('/') != -1:
        arr = file.split('/')
        arr=arr[:-1]
        newPath = str.join('/',arr)
    elif file.find('\\') != -1:
        arr = file.split('\\')
        arr = arr[:-1]
        newPath = str.join('\\',arr)
    return newPath

def createOutput(path:str)->str:
    path = path.replace("/","\\")
    f,e = os.path.splitext(path)
    output=removeFileName(f)
    output = os.path.join(output,"output") 
    if os.path.exists(output):
        if not file_replace: 
            print("An output already exists please move it elsewhere or use -r to replace it")
            exit(0)
        else:
            imag = getAllImages(output)
            for image in imag:
                os.remove(image)
            os.rmdir(output)
    os.mkdir(output)
    return output

def getFileName(file:str)->str:
    fileName = ''
    if file.find('/') != -1:
        arr = file.split('/')
        fileName=arr[-1]

    elif file.find('\\') !=-1:
        arr = file.split('\\')
        fileName = arr[-1]
    return fileName

def getExtension(file:str)->str:
    f,e = os.path.splitext(file)
    return e

def getFilePathWithoutExt(file:str)->str:
    f,e = os.path.splitext(file)
    return f


def getAllImages(path:str)->list:
    files = []
    lis = []
    if path.find('\\') != -1:
        temp = path.split('\\')
        path = str.join('/',temp)

    if path.find('/') != -1:
        files = os.listdir(path)
        for file in files:
            file = path+"/"+file
            lis.append(file)
    return lis

def saveFileToOutput(file:str,output:str):
    im = Image.open(file)
    if Image.isImageType(im):
        filep = getFilePathWithoutExt(file)
        fileName = getFileName(filep)
        fileName = fileName + type_file
        filePath = os.path.join(output,fileName)
        im.save(filePath,quality=qual)




parser = argparse.ArgumentParser(prog='File Compressor',
                                 description='Allows you to compress a batch of files',
                                 epilog='Well just a simple script:)')
parser.add_argument('-F','--Folder',type=str,help='Compresses a batch of images from a folder')
parser.add_argument('-f','--files',type=str,nargs='*',help='Compress a list of files')
parser.add_argument('-q','--quality',type=int,help='Specify the quality of the images from 1-100')
parser.add_argument('-t','--type',type=str,help='Specify the file type of each file')
parser.add_argument('-r','--replace',type=bool,help="Replace an already existing output:(Use with caution)")
args = parser.parse_args()


# set the global options mention at the begining of the code

if args.quality:
    qual = args.quality

if args.type:
    type_file = "." + args.type

if args.replace:
    file_replace = args.replace







if args.Folder:
    direc = args.Folder.replace("\"","")
    files = getAllImages(direc)
    output = createOutput(files[0])
    if files :
        for file in files:
            saveFileToOutput(file=file,output=output)

elif args.files:

    file1 = args.files[0]
    output = createOutput(file1)

    for file in args.files:
        saveFileToOutput(file=file,output=output)

else:
    print("Error please check your arguments or use -h")


