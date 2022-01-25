import os
import dropbox 
from dropbox.files import WriteMode
class TransferData:
    def __init__(self,accesstoken):
        self.accesstoken=accesstoken
    def uploadfiles(self,filefrom,fileto):
        dbx=dropbox.Dropbox(self.accesstoken)
        for root,dirs,files in os.walk(filefrom):
            for filename in files:
                localpath=os.path.join(root,filename)
                relativepath=os.path.relpath(localpath,filefrom)
                dropboxpath=os.path.join(fileto,relativepath)
                with open(localpath,"rb")as f:
                    dbx.files_upload(f.read(),dropboxpath,mode=WriteMode("overwrite"))
def main():
    accesstoken="Kk9PDfW-eucAAAAAAAAAAa2OExkjTM0BqSVVjS3NXR4xyE7a_AtEN_mOPH2Sj4SZ"
    transferdata=TransferData(accesstoken)
    filefrom=str(input("Enter The Folder Path :"))
    fileto=input("Enter The Path To Upload To Dropbox")
    transferdata.uploadfiles(filefrom,fileto)
    print("File Has Been Moved")
main()