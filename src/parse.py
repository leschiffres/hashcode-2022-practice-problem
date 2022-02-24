def parse_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

        total_clients = int(lines[0].strip())
        clients = []
        for i in range(1, total_clients+1):
            likes = set([w for w in lines[2*i-1].strip().split()[1:]])
            dislikes = set([w for w in lines[2*i].strip().split()[1:]])
            clients.append((likes, dislikes))
    return clients
