import os

in_txt = input("Please enter the text: ")

path = "/home/tarak/Desktop/task/"
print(path)

files = []

count = 0 

# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.txt' in file:
            files.append(os.path.join(r, file))

for txt_file in files:
    with open(txt_file, 'r') as f:
        for line in f.readlines():
            words = line.split()
            for word in words:
                if word == in_txt:
                    count += 1
        if count > 0:            
            print ("the input text count is: ", +count)
            print ("the file name: ",txt_file)
            print(os.stat(txt_file).st_size, "KB")
            
            