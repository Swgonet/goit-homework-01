import sys
import os
import shutil
import re
from pathlib import Path


a = Path(sys.argv[1])


folders = ["image", 'documents', 'audio', 'video', 'archives', 'other']


def sort(a):
    for i in os.listdir(a):
        w = os.path.join(a, i)
        if os.path.isdir(w):
            sort(w)
            if not os.listdir(w):
                os.rmdir(w)


def creat_folders():
    for q in folders:
        try:
            os.mkdir(Path(a) + q)
        except FileExistsError:
            pass


def fnc():
    for i in a.glob("**/*"):
        if i.suffix in ['.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx']:
            try:
                shutil.move(i, os.path.join(a, 'documents'))
            except shutil.Error:
                continue
        elif i.suffix in ['.jpeg', '.png', '.jpg', '.svg']:
            try:
                shutil.move(i, os.path.join(a, 'image'))
            except shutil.Error:
                continue
        elif i.suffix in ['.avi', '.mp4', '.mdv', '.mkv']:
            try:
                shutil.move(i, os.path.join(a, 'video'))
            except shutil.Error:
                continue
        elif i.suffix in ['.mp3', '.ogg', '.wav', '.amr']:
            try:
                shutil.move(i, os.path.join(a, 'audio'))
            except shutil.Error:
                continue
        elif i.suffix in ['.zip', '.gz', '.tar']:
            try:
                shutil.move(i, os.path.join(a, 'archives'))
            except shutil.Error:
                continue


archives = os.path.join(a, 'archives')


def unpack(archives):
    archives = os.path.join(a, 'archives')
    for i in Path(archives).iterdir():
        if i.is_file and i.suffix in ['.zip', '.gz', '.tar']:
            shutil.unpack_archive(i, Path(arvhives) / i.stem)


d = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
en = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")
TRANS = {}


def normalize(a):
    path = Path(a)
    os.chdir(path)
    for el in path.glob("**/*"):
        i = re.sub("\W", "_", el.stem) + el.suffix
        for a, b in zip(list(d), en):
            Trans[ord(a)] = b
            Trans[ord(a.upper())] = b.upper()
            s = i.translate(Trans)
        new_i = el.with_name(s)
        os.rename(el.resolve(), new_i.resolve())
                

res = sort(a)
print(res)
print(creat_folders())
print(fnc())
print(unpack(archives))
print(normalize(a))
