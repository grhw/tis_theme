import os

compiled = []

def get_vars(file):
    vars = {}
    for line in file.splitlines():
        if line.startswith("@"):
            data = line[line.find("@"):].split(" ")
            key = data[0][1:]
            if key not in vars.keys():
                vars[key] = []
            vars[key].append(" ".join(data[1:]))
    print(vars)
    return vars

for folder in os.listdir("src"):
    if os.path.isdir("src/"+folder):
        for i in os.listdir("src/"+ folder):
            with open(f"src/{folder}/{i}","r") as f:
                read = f.read()
                if folder == "users":
                    matches = get_vars(read)["user"]
                    for match in matches:
                        compiled.append(read.replace("[ott_inj]",f'[data-author-id="{match}"]'))
                elif folder == "messages":
                    vars = get_vars(read)
                    if vars["where"][0] == "content":
                        for message in vars["message"]:
                            compiled.append(read.replace("[ott_inj]",f'#message-content-{message}'))
                elif folder == "last":
                    compiled.append(read)