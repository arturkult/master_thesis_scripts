from os import listdir
from os.path import join, abspath, isdir, splitext
from subprocess import check_output

# TODO: parametrize input/output

inputDirectoryPath = './datasets/customized'
smileAbsolutePath = abspath('./datasets/scripts/openSmile/SMILExtract_Release.exe')
base_command = [smileAbsolutePath, '-C', abspath('./datasets/scripts/openSmile/emo_large_csv.conf')]
output_extension = ".csv"
outputDirectoryPath = './datasets/output/csv'
classes = "{ang,bor,neu,joy,sad,fea,sur,bor,dis}"


def generate(inputDirectoryPath, outputDirectoryPath):
    for file in listdir(inputDirectoryPath):
        if (isdir(join(inputDirectoryPath, file))):
            generate(join(inputDirectoryPath, file), join(outputDirectoryPath, file))
        else:
            inputPath = join(inputDirectoryPath, file)
            outputPath = join(outputDirectoryPath + output_extension)
            command = [smileAbsolutePath, '-C', abspath('./datasets/scripts/openSmile/emo_large_csv.conf')]
            command.append('-I')
            command.append(abspath(inputPath))
            command.append('-O')
            command.append(abspath(outputPath))
            command.append('-classes')
            command.append(classes)
            command.append('-classlabel')
            command.append(splitext(file)[0][3:6])
            check_output(command, shell=True)


generate(inputDirectoryPath, outputDirectoryPath)
