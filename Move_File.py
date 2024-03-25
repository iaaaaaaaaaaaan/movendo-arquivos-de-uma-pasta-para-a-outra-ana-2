import os
import shutil

# .exe, .msi, .gif, .png, .jpg, .jpeg, .csv, .pdf, .xls, .xlsx, .ppt, .pptx

from_dir = "C:\Users\oba\Pictures\Roblox"
to_dir = "C:/Users/oba/Documents/Arquivos_Documentos"

list_of_files = os.listdir(from_dir)
print(list_of_files)

# mova todos os arquivos de imagem da pasta celecionada
# que no caso é a pasta "Roblox"
# para a outra pasta que no caso é Arquivos_Documentos

for file_name in list_of_files:

    name, extension = os.path.splitext(file_name)

    if extension == '':
        continue
    if extension in ['.gif', '.png', '.jpg', '.jpeg']:
        path1 = from_dir + '/' + file_name
        path2 = to_dir + '/' + "Arquivos_Documentos"
        path3 = to_dir + '/' + "Arquivos_Documentos" + '/' + file_name


if os.path.exists(path2):
    print("Movendo" + file_name + ".....")

    # Mover de path1 ----> path3
    shutil.move(path1, path3)

else:
    os.makedirs(path2)
    print("Movendo" + file_name + ".....")
    shutil.move(path1, path3)