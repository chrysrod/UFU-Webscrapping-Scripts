import sys

f = open (sys.argv[1],'r')
file = f.readlines()
f.close()

file_new = open(sys.argv[1],'w')

text_tag = "conforme a figura abaixo:"
text_tag_2 = "conforme a imagem abaixo:"
caption_tag = "<figcaption>"
referencia = 0
figura = 1

for line in file:
        
        if (text_tag in line) or (text_tag_2 in line):
                file_new.write(line[:line.find('conforme')] + 'conforme a Figura ' + str(figura) + ":" + '\n')
                referencia = 1
        elif (caption_tag in line) and referencia == 1:
                file_new.write(line[:line.find('<figcaption>')] + '<figcaption>Figura ' + str(figura) + ' - ' + 
                line[line.find('<figcaption>')+12:line.find('</figcaption>')] + '</figcaption>' + '\n')
                referencia = 0
                figura += 1
        else:
                file_new.write(line)             

file_new.close()