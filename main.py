from pathlib import Path

def readfile():
    path = Path('')
    items =list(path.rglob('*'))
    for i, items in enumerate(items):
        print(f"{i+1} : {items}")

def create():
    try:
        readfile()
        name = input("enter the file name you want to create: ")
        P = Path(name)
        if not P.exists() and P.is_file():
            with open(P, 'w') as f:
                content = input("enter the content you want to write in the file: ")
                f.write(content)

            print("file created successfully")

        else:
            print("file already exists")

    except Exception as e:
        print(f"error occurred: {e}")




def read():
    try:
        readfile()
        name = input("enter the file name you want to read: ")
        p= Path(name)
        if p.exists() and p.is_file():
            with open(p, 'r') as f:
                data = f.read()
                print(data)

            print("file read successfully")
                
        else:
            print("file does not exist")
    except Exception as e:
        print(f"error occurred: {e}")




def update():
    try:
        readfile()
        name = input("enter the file name you want to update: ")
        p= Path(name)
        if p.exists() and p.is_file():
            print("press 1 to append content")
            print("press 2 to overwrite content")
            print("press 3 to rename the file content")
            choice = int(input("enter your choice: "))
            if choice == 1:
                with open(p, 'a') as f:
                    content = input("enter the content you want to append in the file: ")
                    f.write(content)
                print("file updated successfully")
            elif choice == 2:
                with open(p, 'w') as f:
                    content = input("enter the content you want to overwrite in the file: ")
                    f.write(content)
                print("file updated successfully")
            elif choice == 3:
                new_name = input("enter the new name for the file: ")
                new_p = Path(new_name)
                if not new_p.exists():
                    p.rename(new_p)
                    print("file renamed successfully")
                else:
                    print("file with that name already exists")

        else:
            print("file does not exist")
    except Exception as e:
        print(f"error occurred: {e}")



def delete():
    try :
        readfile()
        name = input("enter the file name you want to delete: ")
        p= Path(name)
        if p.exists() and p.is_file():
            p.unlink()
            print("file deleted successfully")
        else:
            print("file does not exist")

    except Exception as e:
        print(f"error occurred: {e}")

print("enter 1 for creating a file")
print("enter 2 for reading a file")
print("enter 3 for updating a file")
print("enter 4 for deleting a file")

check = int(input("enter your choice: "))

if check == 1:
    create()

if check == 2:
    read()

if check == 3:
    update()

if check == 4:
    delete()

