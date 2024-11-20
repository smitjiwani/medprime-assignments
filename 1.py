import os

def rename_files_recursively(folder_path, reverse=False, preview=False):
    for root, dirs, files in os.walk(folder_path):
        if files:
            
            if reverse:
                file_count = len(files)
            else:
                file_count = 1

            sorted_files = sorted(files, reverse=reverse)

            for file in sorted_files:
                old_path = os.path.join(root, file)
                new_name = str(file_count) + os.path.splitext(file)[1]
                new_path = os.path.join(root, new_name)

                if preview:
                    print(f"Old: {old_path}")
                    print(f"New: {new_path}")
                else:
                    try:
                        os.rename(old_path, new_path)
                        print(f"File '{file}' renamed to '{new_name}'")
                    except OSError as e:
                        print(f"Error renaming '{file}': {e}")

                if reverse:
                    file_count -= 1
                else:
                    file_count += 1

            if preview:
                if input("Continue renaming files? (y/n): ").lower() == 'n':
                    continue
                else:
                    if reverse:
                      file_count = len(files)
                    else:
                      file_count = 1
                    for file in sorted_files:

                        old_path = os.path.join(root, file)
                        new_name = str(file_count) + os.path.splitext(file)[1]
                        new_path = os.path.join(root, new_name)
                        try:
                            os.rename(old_path, new_path)
                            print(f"File '{file}' renamed to '{new_name}'")
                        except OSError as e:
                            print(f"Error renaming '{file}': {e}")
                            
                        if reverse:
                          file_count -= 1
                        else:
                          file_count += 1

if __name__ == "__main__":
    folder_path = input("Please enter the path to the folder: ")
    reverse_order = input("Rename files in reverse order? (y/n): ").lower() == 'y'
    preview_mode = input("Preview file names before renaming? (y/n): ").lower() == 'y'

    rename_files_recursively(folder_path, reverse_order, preview_mode)