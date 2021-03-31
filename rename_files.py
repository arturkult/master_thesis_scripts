from os import listdir, mkdir
from os.path import join, isdir, abspath, splitext, exists
from shutil import copy

datasets = \
    [
        ['./../original/lublin', './../customized/lub', 'lub'],
        # ['./../original/english', './../customized/eng', 'eng'],
        # ['./../original/LODZ', './../customized/lod', 'lod'],
        # ['./../original/agh', './../customized/agh', 'agh'],
    ]

lod_emo = {
    "n": "neu",
    "h": "joy",
    "s": "sad",
    "f": "fea",
    "a": "ang",
    "u": "sur",
    "d": "dis",
}

agh_person = {
    "AKA": "f01",
    "AKL": "f02",
    "HKR": "f03",
    "MMA": "f04",
    "MIG": "f05",
    "BTO": "f06",
    "JMI": "m01",
    "MCH": "m02",
    "MGR": "m03",
    "MPO": "m04",
    "PJU": "m05",
    "PKE": "m06",
}
agh_emo = {
    "IR": "bor",
    "NE": "neu",
    "RA": "joy",
    "SM": "sad",
    "ST": "fea",
    "ZD": "sur",
    "ZL": "ang"
}


def resolve_name(filename, dataset_type, index):
    if dataset_type == 'lub':
        name_without_extension = splitext(filename)[0]
        newname = name_without_extension[0] + "0" + name_without_extension[1:]
        return newname + splitext(filename)[1]
    elif dataset_type == 'eng':
        return filename
    elif dataset_type == 'lod':
        name_without_extension = splitext(filename)[0]
        newname = name_without_extension[:1] + "0" + name_without_extension[1:2]
        newname += lod_emo.get(name_without_extension[-1:])
        newname += "{:02d}".format(index)
        return newname + splitext(filename)[1]
    else:  # agh
        name_without_extension = splitext(file)[0]
        newname = agh_person.get(name_without_extension[:3])
        newname += agh_emo.get(name_without_extension[4:6])
        newname += "{:02d}".format(index)
        return newname + splitext(filename)[1]


for dataset in datasets:
    print(dataset[0])
    source_path = dataset[0]
    dest_path = dataset[1]
    if not exists(dest_path):
        mkdir(dest_path)
    prefix = dataset[2]
    index = 1
    for file in listdir(source_path):
        newname = resolve_name(file, prefix, index)
        index += 1
        copy(join(source_path, file), join(dest_path, newname))
