import argparse
import time
import utils
from os import remove

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("-f","--file-path",type=str,required=True,help="Either a path to binary or .c to compile with gcc")
arg_parser.add_argument("-tr","--test-ratio",type=utils.string2tuple)
arg_parser.add_argument("-t","--time-restriction",type=float)
arg_parser.add_argument("-p","--tests-fro-path",type=str)
arg_parser.add_argument("-c","--compile",action="store_true")
args = arg_parser.parse_args()

def main():
    ratio = args.test_ratio if args.test_ratio else (1,1)
    per_test_time_restriction = args.time_restriction if args.time_restriction else None
    inputs,desired_results = utils.parse_tests(ratio) if not args.tests_fro_path else utils.parse_tests(ratio,args.tests_fro_path)
    path = args.file_path
    compile = utils.compile(path) if args.compile else None
    if compile:
        path = compile
    averageruntime = 0 
    test_num = 0
    for input_set in inputs: 
        t1 = time.time()
        program_out = utils.run_bin(path,input_set)
        t2 = time.time()
        timedelta = round(t2 - t1,ndigits=5)
        averageruntime += timedelta 
        
        if not program_out:
            continue
        
        if utils.test(program_out,"\n".join(desired_results[test_num])):
            if not per_test_time_restriction:
                print(f"Test set no.{test_num} ✔")
            else:
                print(f"Test set no.{test_num} ✔✔") if per_test_time_restriction >= timedelta else print(f"Test set no.{test_num} ✔x")

        else:
            print(f"Test set no.{test_num} x")
            print(f"│Should get :\n│{'\n│'.join(desired_results[test_num])}")
            print("├─────────────────")
            print(f"│Instead got :\n│ {'\n│'.join(program_out.split(sep='\n'))}")
            print("╰─────────────────")
        test_num+=1
    remove(compile) if compile else None
    
if __name__ == "__main__":
    main()
