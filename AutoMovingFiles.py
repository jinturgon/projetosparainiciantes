from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
# pip install watchdog

import os
import time

docsfiles = ['DOC', 'DOCX', 'LOG', 'MSG', 'ODT', 'PAGES', 'RTF', 'TEX', 'TXT', 'WPD', 'WPS','XLR','XLS','XLSX','XLSM','PDF','EPUB','MOBI']
datafiles = ['CSV', 'DAT', 'GED', 'KEY', 'KEYCHAIN', 'PPS', 'PPT', 'PPTX', 'SDF', 'TAR', 'TAX2016', 'TAX2019', 'VCF', 'XML']
audiofiles = ['AIF', 'IFF', 'M3U', 'M4A', 'MID', 'MP3', 'MPA', 'WAV', 'WMA']
videofiles = ['3G2', '3GP', 'ASF', 'AVI', 'FLV', 'M4V', 'MOV', 'MP4', 'MPG', 'RM', 'SRT', 'SWF', 'VOB', 'WMV', 'WEBM']
imagefiles = ['BMP', 'DDS', 'GIF', 'HEIC', 'JPG', 'PNG', 'PSD', 'PSPIMAGE', 'TGA', 'THM', 'TIF', 'TIFF', 'YUV','AI', 'EPS', 'SVG','JPEG']
compressedfiles = ['7Z', 'DEB', 'GZ', 'PKG', 'RAR', 'RPM', 'SITX', 'TAR', 'ZIP', 'ZIPX']
executablefiles = ['APK', 'APP', 'BAT', 'CGI', 'COM', 'EXE', 'GADGET', 'JAR', 'WSF','MSI']
devfiles = ['ASP', 'ASPX', 'CER', 'CFM', 'CSR', 'CSS', 'DCR', 'HTM', 'HTML', 'JS', 'JSP', 'PHP', 'RSS', 'XHTML','C', 'CLASS', 'CPP', 'CS', 'DTD', 'FLA', 'H', 'JAVA', 'LUA', 'M', 'PL', 'PY', 'SH', 'SLN', 'SWIFT', 'VB', 'VCXPROJ', 'XCODEPROJ']


class MyHandler(FileSystemEventHandler):

    def __init__(self):
        self.docsmoved,self.datamoved,self.audiomoved,self.videomoved,self.imagemoved,self.compressedmoved,self.executablemoved,self.devmoved = 0,0,0,0,0,0,0,0

    def print_results(self):
        print("Documents files moved: " + str(self.docsmoved))
        print("Data files moved: " + str(self.datamoved))
        print("Audio files moved: " + str(self.audiomoved))
        print("Video files moved: " + str(self.videomoved))
        print("Image files moved: " + str(self.imagemoved))
        print("Compressed files moved: " + str(self.compressedmoved))
        print("Executable files moved: " + str(self.executablemoved))
        print("Developer files moved: " + str(self.devmoved))
    
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            src = folder_to_track + "\\" + filename

            if filename.split('.').pop().upper() in docsfiles:
                new_destination = folder_documents + "\\" + filename
                os.rename(src, new_destination)
                self.docsmoved += 1
                continue
            elif filename.split('.').pop().upper() in datafiles:
                new_destination = folder_data + "\\" + filename
                os.rename(src, new_destination)
                self.datamoved += 1
                continue
            elif filename.split('.').pop().upper() in audiofiles:
                new_destination = folder_music + "\\" + filename
                os.rename(src, new_destination)
                self.audiomoved += 1
                continue
            elif filename.split('.').pop().upper() in videofiles:
                new_destination = folder_video + "\\" + filename
                os.rename(src, new_destination)
                self.videomoved += 1
                continue
            elif filename.split('.').pop().upper() in imagefiles:
                new_destination = folder_images + "\\" + filename
                os.rename(src, new_destination)
                self.imagemoved += 1
                continue
            elif filename.split('.').pop().upper() in compressedfiles:
                new_destination = folder_compressed + "\\" + filename
                os.rename(src, new_destination)
                self.compressedmoved += 1
                continue
            elif filename.split('.').pop().upper() in executablefiles:
                new_destination = folder_executable + "\\" + filename
                os.rename(src, new_destination)
                self.executablemoved += 1
                continue
            elif filename.split('.').pop().upper() in devfiles:
                new_destination = folder_dev + "\\" + filename
                os.rename(src, new_destination)
                self.devmoved += 1
                continue
            else:
                pass

folder_to_track = os.environ['USERPROFILE'] + "\\Downloads"

folder_documents = os.environ['USERPROFILE'] + "\\Downloads\\Documents"
folder_data = os.environ['USERPROFILE'] + "\\Downloads\\Data"
folder_music = os.environ['USERPROFILE'] + "\\Downloads\\Music"
folder_video = os.environ['USERPROFILE'] + "\\Downloads\\Video"
folder_images = os.environ['USERPROFILE'] + "\\Downloads\\Images"
folder_compressed = os.environ['USERPROFILE'] + "\\Downloads\\Compressed"
folder_executable = os.environ['USERPROFILE'] + "\\Downloads\\Executables"
folder_dev = os.environ['USERPROFILE'] + "\\Downloads\\Developer"

folder_destination = os.environ['USERPROFILE'] + "\\Downloads"

event_handler = MyHandler()
observer = Observer()
observer.start()

observer.schedule(event_handler, folder_to_track, recursive=True)

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
    event_handler.print_results()
observer.join()
