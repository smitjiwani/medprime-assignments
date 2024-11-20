import os
import zipfile
# import pyzipper
import tqdm


def zip_folder(folder_path, name=None):
# def zip_folder(folder_path, name=None, password=None):
    if not name:
        filename = os.path.basename(folder_path) + ".zip"
    else:
        filename = name + ".zip"

    zip_filepath = os.path.join(os.path.dirname(folder_path), filename)

    try:
        # if password:
        #     with pyzipper.AESZipFile(zip_filepath, "w", compression=pyzipper.ZIP_LZMA, encryption=pyzipper.WZ_AES) as zip_file:
        #         zip_file.setpassword(password.encode())
        #         for root, _, files in tqdm.tqdm(os.walk(folder_path), desc="Zipping files with encryption"):
        #             for file in files:
        #                 archive_path = os.path.relpath(os.path.join(root, file), folder_path)
        #                 zip_file.write(os.path.join(root, file), archive_path)
        #     print(f"Folder '{folder_path}' zipped successfully to '{zip_filepath}' with encryption.")
        # else:
            with zipfile.ZipFile(zip_filepath, "w", zipfile.ZIP_DEFLATED) as zip_file:
                for root, _, files in tqdm.tqdm(os.walk(folder_path), desc="Zipping files"):
                    for file in files:
                        archive_path = os.path.relpath(os.path.join(root, file), folder_path)
                        zip_file.write(os.path.join(root, file), archive_path)
            print(f"Folder '{folder_path}' zipped successfully to '{zip_filepath}'.")

    except Exception as e:
        print(f"Error zipping folder: {e}")


if __name__ == "__main__":
    folder_path = input("Enter the path to the folder you want to zip: ")
    name = input("Enter the name of the zip file: (optional) ")
    # password = input("Enter the password for the zip file: (optional) ")

    if not os.path.exists(folder_path):
        print(f"Error: Folder '{folder_path}' does not exist.")
    else:
        # zip_folder(folder_path, name, password)
        zip_folder(folder_path, name)
