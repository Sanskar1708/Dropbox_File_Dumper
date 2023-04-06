import os
import dropbox
from dropbox.files import WriteMode

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token
        self.dbx = dropbox.Dropbox(self.access_token)

    def upload_file(self, file_from, file_to):
        for root, dirs, files in os.walk(file_from):
            for filename in files:
                local_path = os.path.join(root, filename)
                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)

                with open(local_path, 'rb') as f:
                    self.dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

def main():
    access_token = 'sl.Bb89rj95Q1Yg1dUVaq--vW_lFSenGXUnoLUzx_xExeMiX39EmWYYv2f-7HMFJQREacNXVueLgOiRU8RvtGEcf6bkoDfCXWMRy4bY5cCnE5IOimIh4B2JseFgrZxAE88_A2RLKpo'
    transfer_data = TransferData(access_token)

    file_from = input("Enter the full path of the folder to be uploaded: ")
    file_to = input("Enter the full path to upload the folder to in Dropbox: ")

    transfer_data.upload_file(file_from, file_to)
    print("Folder uploaded successfully to Dropbox.")

if __name__ == '__main__':
    main()