from __future__ import annotations

class Dir:
    
    child: list[Dir]
    def __init__(self, name, dir = True, parent:Dir = None, size = 0):
        self.name = name
        self.dir = dir
        self.parent = parent
        if parent:
            parent.child.append(self)
        self.child = []
        self.size = size
    
    def level(self):
        cnt = 0
        parent = self.parent
        while parent:
            parent = parent.parent
            cnt +=1
        return cnt
       
    def __str__(self) -> str:
        out = []
        meta = "(dir)" if self.dir else f"(file, size={self.size})"
        tab = "".join(['\t' for t in range(0, self.level())])
        out.append(f"{tab}- {self.name} {meta}")        
        out.extend([child.__str__() for child in self.child])
        
        return "\n".join(out)

def dir_size(dir:Dir) -> int:
    total = 0
    f_sizes = [c.size for c in dir.child if not c.dir]
    d_sizes = [dir_size(d) for d in dir.child if d.dir]
    
    return sum(f_sizes + d_sizes)

def dirs(dir:Dir):
    arr = []
    arr.append((dir.name, dir_size(dir)))

    for c in dir.child:
        if c.dir:            
            arr.extend(dirs(c))
        
    return arr

def p1(root:Dir):
    total = 0
    max = 100000

    sizes = dirs(root)

    total = sum([s for d, s in sizes if s < max])
    
    print(total)

def p2(root:Dir):
    space = 70000000
    space_needed = 30000000

    sizes = dirs(root)

    space_used = [s for d, s in sizes if d == root.name][0]

    space_available = space - space_used
    space_required = space_needed - space_available

    del_dirs = sorted(filter(lambda t : t[1] > space_required, sizes), key=lambda t: t[1])

    print(del_dirs[0][1])

with open("data/7.txt", 'r', encoding = 'utf-8') as f:
    input = f.read().splitlines()

    root = None
    cf = None
    path = []

    for line in input:
        if line.startswith('$ cd'):
            cd = line.split()[2]
            if cd == '..':
                cf = cf.parent
            else :
                dir = Dir(cd, parent = cf)
                cf = dir
                if cd == '/':
                    root = cf
        elif line.startswith('$ ls'):
            continue
        else:
            if line.startswith('dir'):
                folder = line.split()[1]
                Dir(folder, parent = cf)
            else:
                size, file = line.split()
                Dir(file, dir=False, parent=cf, size = int(size))
    print(root)
    p1(root)
    p2(root)
        
        
