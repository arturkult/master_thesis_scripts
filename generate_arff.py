import logging
from os import listdir
from os.path import join, splitext, abspath, isdir
from subprocess import run, DEVNULL

# TODO: parametrize input/output

inputDirectoryPath = './datasets/customized/'
smileAbsolutePath = abspath('./datasets/scripts/openSmile/SMILExtract_Release.exe')
base_command = [smileAbsolutePath, '-C', abspath('./datasets/scripts/openSmile/IS09_emotion_modified_arff.conf')]
# base_command = [smileAbsolutePath, '-C', abspath('./datasets/scripts/openSmile/IS09_emotion.conf')]
output_extension = ".arff"
outputDirectoryPath = './datasets/output/arff/IS09_emotion_modified_arff'
classes = "{ang,bor,neu,joy,sad,fea,sur,bor,dis}"

logger = logging.getLogger('my-logger')
logger.propagate = False


def generate(inputDirectoryPath, outputDirectoryPath):
    print(outputDirectoryPath)
    for file in listdir(inputDirectoryPath):
        if (isdir(join(inputDirectoryPath, file))):
            generate(join(inputDirectoryPath, file), join(outputDirectoryPath, file))
        else:
            inputPath = join(inputDirectoryPath, file)
            outputPath = outputDirectoryPath + output_extension
            command = [smileAbsolutePath, '-C', abspath('./datasets/scripts/openSmile/IS09_emotion_modified_arff.conf')]
            command.append('-I')
            command.append(abspath(inputPath))
            command.append('-O')
            command.append(abspath(outputPath))
            command.append('-classes')
            command.append(classes)
            command.append('-classlabel')
            command.append(splitext(file)[0][3:6])
            run(command, shell=True, stdout=DEVNULL, stderr=DEVNULL, check=True)


generate(inputDirectoryPath, outputDirectoryPath)
