##
## Unit tests for ME369P/396P/ES122 Fall 2022 Assignment 4
##

import pytest
import importlib
import os
import io
import sys
import random
import yaml
import traceback

# module import: spec1: memberScheduler  spec2: groupScheduler  spec3: MeetingScheduler

# path  = os.getcwd() + '/' + 'assignment4-main.py' #linux, mac user
path1  = os.getcwd() + '\\' + 'memberScheduler.py' #windows user
spec1 = importlib.util.spec_from_file_location("memberScheduler", path1)
my_script1 = importlib.util.module_from_spec(spec1)

path2  = os.getcwd() + '\\' + 'groupScheduler.py' #windows user
spec2 = importlib.util.spec_from_file_location("groupScheduler", path2)
my_script2 = importlib.util.module_from_spec(spec2)

path3  = os.getcwd() + '\\' + 'scheduleOptimizer.py' #windows user
spec3 = importlib.util.spec_from_file_location("scheduleOptimizer", path3)
my_script3 = importlib.util.module_from_spec(spec3)


try:
    spec1.loader.exec_module(my_script1)
    spec2.loader.exec_module(my_script2)
    spec3.loader.exec_module(my_script3)
    print("PASS: SCRIPT IS EXECUTABLE")
except Exception as ex:
    print('\n\nFAIL: EXCEPTION THROWN WHILE RUNNING FUNCTION:')
    print(type(ex).__name__,': ',ex, end='\n\n', sep='')
except:
    print('\n\nFAIL: NON-STANDARD EXCEPTION THROWN WHILE RUNNING FUNCTION\n\n')
    
    
    
def test_Q1_member_schedule_generator():
    
    with open('memberScheduler_input.yml', 'r') as tests:
        tests = yaml.load(tests, Loader=yaml.FullLoader)
    
    for testcase in tests:
        for testname, specs in testcase.items():
            test_name = specs['name']
            test_input = specs['input']

            # my_output = io.StringIO()
            # old_stdout = sys.stdout
            # sys.stdout = my_output

            print(test_name)
            
            p_list = []
            for p in (test_input):
                kwargs1 = p
                try:
                    instane_member_schedule = my_script1.personSchedule(**kwargs1)
                    instane_member_schedule.view_schedule()
                except Exception as ex:
                    print('\n\nEXCEPTION THROWN WHILE RUNNING FUNCTION:')
                    print(type(ex).__name__,': ',ex, end='\n\n', sep='')
                    print(traceback.format_exc())
                except:
                    print('\n\nNON-STANDARD EXCEPTION THROWN WHILE RUNNING FUNCTION\n\n')
                    
            assert True == True #testing TBD (TODO)

def test_Q2_group_schedule_generator():
    
    with open('groupScheduler_input.yml', 'r') as tests:
        tests = yaml.load(tests, Loader=yaml.FullLoader)
    
    for testcase in tests:
        for testname, specs in testcase.items():
            test_name = specs['name']
            test_input = specs['input']
            meeting_input = specs['input2']

            # my_output = io.StringIO()
            # old_stdout = sys.stdout
            # sys.stdout = my_output

            print(test_name)
            
            p_list = []
            for p in (test_input):
                kwargs1 = p
                try:
                    instane_member_schedule = my_script1.personSchedule(**kwargs1)
                except Exception as ex:
                    print('\n\nEXCEPTION THROWN WHILE RUNNING FUNCTION:')
                    print(type(ex).__name__,': ',ex, end='\n\n', sep='')
                    print(traceback.format_exc())
                except:
                    print('\n\nNON-STANDARD EXCEPTION THROWN WHILE RUNNING FUNCTION\n\n')
                    
                p_list.append(instane_member_schedule)
                
            g1 = my_script2.groupScheduler(p_list)
            g1.MeetingScheduler(**meeting_input)
            assert True == True
            
def test_Q5_group_schedule_optimizer():
    
    with open('groupOptimizer_input.yml', 'r') as tests:
        tests = yaml.load(tests, Loader=yaml.FullLoader)
    
    for testcase in tests:
        for testname, specs in testcase.items():
            test_name = specs['name']
            test_input = specs['input']
            main_schedule = specs['input2']
            meeting_input = specs['input3']

            # my_output = io.StringIO()
            # old_stdout = sys.stdout
            # sys.stdout = my_output

            print(test_name)
            
            p_list = []
            for p in (test_input):
                kwargs1 = p
                try:
                    instane_member_schedule = my_script1.personSchedule(**kwargs1)
                except Exception as ex:
                    print('\n\nEXCEPTION THROWN WHILE RUNNING FUNCTION:')
                    print(type(ex).__name__,': ',ex, end='\n\n', sep='')
                    print(traceback.format_exc())
                except:
                    print('\n\nNON-STANDARD EXCEPTION THROWN WHILE RUNNING FUNCTION\n\n')
                    
                p_list.append(instane_member_schedule)
                
            g1 = my_script2.groupScheduler(p_list)
            
            o1 = my_script3.scheduleOptimizer(g1, main_schedule)
            o1.MeetingScheduler(**meeting_input)
            assert True == True
            
if __name__ == '__main__':

    # test_Q1_member_schedule_generator()
    # test_Q2_group_schedule_generator()
    test_Q5_group_schedule_optimizer()