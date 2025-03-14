import subprocess
import math
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
    compiled_path = filter(lambda x : x.startswith("compiled"),listdir())
    return f"./{list(compiled_path)[0]}"

def parse_tests(path : str|None = None):
    inputs = []
    results = []
    flag = None
    with open(Path("tests.txt")) as out:
        line = out.readline()
        input_cluster = []
        result_cluster = []
        while line:
            match line.strip():
                case "<--IS-->":
                    flag = "IR" 
                case "<--IE-->":
                    flag = None
                    inputs.append(input_cluster)
                    input_cluster = []
                case "<--OS-->":
                    flag =  "OS"
                case "<--OE-->":
                    flag = None
                    results.append(result_cluster)
                    result_cluster = []

            if flag == "IR" and line.strip() != "<--IS-->":
                input_cluster.append(line)
            if flag == "OS" and line.strip() != "<--OS-->":
                result_cluster.append(line)
            
            line = out.readline()

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
