import subprocess
from typing import Optional
from pathlib import Path
from os import listdir

def run_bin(path  ,stdin : list[str]|None = None) -> Optional[str]:
    p = subprocess.Popen((path),stdout=subprocess.PIPE,stdin=subprocess.PIPE)
    if stdin:
        [p.stdin.write(input.encode()) for input in stdin]
        p.stdin.close()
    p.wait()
    output = p.stdout.read()   
    return output.decode()


def compile(path:str):
    p = subprocess.Popen(("gcc","-o","compiled",path),stdout=subprocess.PIPE,stdin=subprocess.PIPE)
    p.wait()
    #Windows workaround
    compiled_path = filter(lambda x : x.startswith("compiled"),listdir())
    return f"./{list(compiled_path)[0]}"


def parse_tests(map:tuple[int,int] = (1,1),path : str|None = None) -> tuple[list,list]:
    inputs = []
    results = []
    test_files = ("i.txt","o.txt") if not path else (Path(f"{path}/i.txt"),Path(f"{path}/o.txt"))
    for i in range(2):
        with open(test_files[i]) as out:
            line = out.readline()
            while line:
                local_input = []
                for _ in range(map[i]):
                    local_input.append(line.strip() if i == 1 else line)
                    line = out.readline()

                inputs.append(local_input) if i == 0 else results.append(local_input)

    return inputs,results
    

def test(std_pulled,desired) -> bool:
    try:
        assert std_pulled.split() == desired.split()
        return True
    except AssertionError:
        return False

def string2tuple(value:str) -> tuple:
    try:
        return tuple(map(int,value.split(",")))
    except:
        raise ValueError
     
