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
Run tests from tests.txt.         
        
    python main.py -f yourbin 

#### tests.txt format: 

* Use **<--IS-->/<--IE-->** to enclose inputs.
* Use **<--OS-->/<--OE-->** to enclose wanted outputs.
* Do not use empty rows in the test file as this will result into failure.

#### Advanced usage:
* **-t** flag is used to time restrict tests e.g: -t 0.001 will timeout everything that runs longer(in ms)
* **-c** flag is to compile and run tests on compiled bin e.g: -c test.c will compile and run tests with compiled binary
----------------------------
