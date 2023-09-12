import subprocess

subprocess.call("python translate.py --model data/model/model.pt --src data/1-1.txt --output data/1-1.en.txt --gpu 0 --verbose", shell=True)

f = open('data/1-1.en.txt','r')

lines = f.readlines()

print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n--------------------")
print(lines[0])
print(lines[1])

