
from constants import TEMPLATEFILE, INVITEESFILE, OUTPUTFOLDER

# get letter template
with open(TEMPLATEFILE) as file:
    template = file.read().split('\n')

# print(template)

# get invitee names
with open(INVITEESFILE) as file:
    invitees = file.read().split('\n')
# print(invitees)

# place names from invitees list into template file and create a new file
outpara = ''
for name in invitees:
    copytemplate = template
    for line in copytemplate:
        # print(line)
        line = line.replace("[name]", name)
        # print(line)
        outpara += line + '\n'
    print(outpara)
    outputfile = OUTPUTFOLDER + name + ".txt"
    with open(outputfile, "w") as file:
        file.write(outpara)
    outpara = ''
