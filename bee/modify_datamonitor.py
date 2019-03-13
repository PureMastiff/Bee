# codint=utf-8

def alter(file, new_str):
    file_data = ""
    with open(file, 'r') as f:
        for line in f:
            if line.startswith('id'):
                line = line.replace(line ,new_str)
            file_data += line

    with open(file, 'w') as f:
        f.write(file_data)

alter("/Users/guogx/git/Bee/config.yaml", 'ddddddd\n')