import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        f = open(file_from, 'rb')
        dbx.file_upload(f.read(), file_to)

def main():
    access_token = 'sl.Auagy0WF8yC19P1KafqP-t0Hmb0LBrLAq0EsbiM64iw1qcphvGnQs9G3DnqXz0vV3UI8F1bRU6yDe1iPTyNR5SD18UxXvORvHybgJwNVQm-4I6xIMwz1-f2WuItQoG0Kfx2JSDg'
    transferData = TransferData(access_token)

    file_from = input("Enter the file paths to transfer: ")
    file_to = input("Enter the full paths to upload to dropbox: ")
    transferData.upload_file(file_from, file_to)

    print("Files have been moved.")

main()

