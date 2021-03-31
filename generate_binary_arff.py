import logging
from os import listdir
from os.path import join, splitext, abspath, isdir
from subprocess import run, DEVNULL

# TODO: parametrize input/output

inputDirectoryPath = './datasets/customized/'
smileAbsolutePath = abspath('./datasets/scripts/openSmile/SMILExtract_Release.exe')
# base_command = [smileAbsolutePath, '-C', abspath('./datasets/scripts/openSmile/IS09_emotion.conf')]
output_extension = ".arff"
outputDirectoryPath = './datasets/output/arff/IS09_emotion_binary_featured'
classes = "{ang,bor,neu,joy,sad,fea,sur,bor,dis}"
classes_list = ['ang', 'bor', 'neu', 'joy', 'sad', 'fea', 'sur', 'dis']

logger = logging.getLogger('my-logger')
logger.propagate = False


def generate(inputDirectoryPath, outputDirectoryPath):
    a = {
        'ang': 0,
        'no-ang': 0,
        'bor': 0,
        'no-bor': 0,
        'neu': 0,
        'no-neu': 0,
        'joy': 0,
        'no-joy': 0,
        'sad': 0,
        'no-sad': 0,
        'fea': 0,
        'no-fea': 0,
        'sur': 0,
        'no-sur': 0,
        'dis': 0,
        'no-dis': 0
    }
    print(outputDirectoryPath)
    for emo in classes_list:
        a[emo] = countFiles(emo, inputDirectoryPath)
    print(a)
    for file in listdir(inputDirectoryPath):
        if isdir(join(inputDirectoryPath, file)):
            generate(join(inputDirectoryPath, file), join(outputDirectoryPath, file))
        else:
            for emo in classes_list:
                emotion = splitext(file)[0][3:6]
                inputPath = join(inputDirectoryPath, file)
                outputPath = outputDirectoryPath + "_" + emo + output_extension
                class_label = emo
                if emotion != emo:
                    class_label = "no-" + class_label
                command = [smileAbsolutePath,
                           '-C', abspath('./datasets/scripts/openSmile/IS09_emotion_min.conf'),
                           '-I', abspath(inputPath),
                           '-O', abspath(outputPath),
                           '-classes', "{" + emo + "," + "no-" + emo + "}",
                           '-classlabel', class_label]
                if emo == emotion or a["no-" + emo] < a[emo]:
                    if class_label != emo:
                        a["no-" + emo] += 1
                    run(command, shell=True, stdout=DEVNULL, stderr=DEVNULL, check=False)
                    # run(command, shell=True)
    print(a)


def countFiles(pattern, path):
    counter = 0
    for file in listdir(path):
        if pattern in file:
            counter += 1
    return counter


generate(inputDirectoryPath, outputDirectoryPath)
