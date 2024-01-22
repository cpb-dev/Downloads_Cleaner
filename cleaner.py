import os

downloads = "???" #Add the filepath to your downloads folder here

if os.path.exists(downloads) and os.path.isdir(downloads):
    files = os.listdir(downloads)

    for file in files:
        file_path = os.path.join(downloads, file)
        try:
            if os.path.isfile(file_path) and file.lower() != "desktop.ini": # desktop.ini is too important to delete
                os.remove(file_path)
                print(f"Deleted: {file_path}")
        except Exception as e:
            print(f"Error deleting {file_path: {e}}")

else:
    print("Downloads folder does not exist.")
