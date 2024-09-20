import os

compiled = []

for folder in os.listdir("src"):
    if os.path.isdir("src/"+folder):
        for i in os.listdir("src/"+ folder):
            with open(f"src/{folder}/{i}","r") as f:
                read = f.read()
                matches = []
                for line in read.splitlines():
                    if line.startswith("@user "):
                        matches.append(line.replace("@user ",""))
                
                for match in matches:
                    compiled.append(read.replace("[ott_inj]",f'[data-author-id="{match}"]'))