# STU.Pid

**S**imple **T**esting **U**tility for **P**rpr **i**ncluding **d**sa. Can run binaries aswell as compile from source.

### Prerequisites:
* Python 3.12 <
* Gcc for for .c compilation
* Brain
### Setup:
No need to setup venvs or install anything with pip.
Everything is std python.
    
### Usage:
#### Basic usage:
Run tests from i.txt and compare with o.txt. Test ratios(how many inputs will result in how many outputs) is infered at runtime. However if this fails you can use -tr flag.   
        
        python main.py -f yourbin 

#### Advanced usage:
* **-tr** flag is used to modify test ratio e.g: -tr 1,2 will test 1 input against 2 outputs
* **-t** flag is used to time restrict tests e.g: -t 0.001 will timeout everything that runs longer(in ms)
* **-p** flag is used to test from given path e.g: -p prprtests/cv1/u5 will be used for tests
* **-c** flag is to compile and run tests on compiled bin e.g: -c test.c will compile and run tests with compiled binary
----------------------------
    python main.py -f 7.c -c -p ./prprtests/cv1/u7 -tr 1,2

This will take file 7.c compile it and use tests from specified directory. One input should return 2 outputs hence the test ratio 1,2.
    
    python main.py -7.c -c -p ./prprtests/cv1/u7 

Same as first example, except the -tr flag. Tester will automatically infer that 1 input will result in 2 outputs.
