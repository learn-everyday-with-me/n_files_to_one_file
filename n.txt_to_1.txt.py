import os
path = r'Enter your path here'
final_string = os.path.join(path,"final.txt")
final = open(final_string,"w")
for _ in os.listdir(path):
    final.write(str(_) + ".txt : " + "\n\n")
    temp = os.path.join(path,str(_) + ".txt")
    file = open(temp,"r")
    final.write(file.read())
    file.close()
    final.write("\n\n")
final.close()
