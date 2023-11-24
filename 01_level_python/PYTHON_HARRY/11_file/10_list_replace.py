words=["donkey","kaddu","mote"]
with open("Sample.txt") as f:
    content=f.read()

for word in words:
    content=content.replace(word,"!@#$%")

    with open("Sample.txt","w") as f:
        f.write(content)