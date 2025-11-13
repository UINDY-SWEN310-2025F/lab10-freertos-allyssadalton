# import pytest
# import os
# from pathlib import Path
# import filecmp


# # def test_check_sum():
# #   cwd = os.getcwd()
# #   stdout_file = cwd + "/tests/thread_child_join_out"
# #   f = open(stdout_file)
# #   stdout_file_content = f.read()
# #   f.close()

# #   #ARRRRG sum is 12079685
# #   arr = stdout_file_content.split()

# #   if int(arr[3]) != 10000000:
# #     assert True
# #   else:
# #     assert False


# def test_fcfs_output1():
#   cwd = os.getcwd()
#   stdout_file = cwd + "/tests/fcfs_out1"
#   f = open(stdout_file)
#   stdout_file_content = f.read()
#   f.close()

#   substring = "ID"
#   count = stdout_file_content.count(substring)

#   if count == 1:
#     assert True
#   else:
#     assert False

# def test_fcfs_output2():
#   cwd = os.getcwd()
#   stdout_file = cwd + "/tests/fcfs_out1"
#   f = open(stdout_file)
#   stdout_file_content = f.read()
#   f.close()

#   substring = "1 1 5 6 0 5 2 3 18 24 3 21 3 5 3 27 19 22"
#   count = stdout_file_content.count(substring)

#   if count == 1:
#     assert True
#   else:
#     assert False

# def test_sjf_output1():
#   cwd = os.getcwd()
#   stdout_file = cwd + "/tests/sjf_out1"
#   f = open(stdout_file)
#   stdout_file_content = f.read()
#   f.close()

#   substring = "ID"
#   count = stdout_file_content.count(substring)

#   if count == 1:
#     assert True
#   else:
#     assert False

# def test_sjf_output2():
#   cwd = os.getcwd()
#   stdout_file = cwd + "/tests/sjf_out1"
#   f = open(stdout_file)
#   stdout_file_content = f.read()
#   f.close()

#   substring = "ID AT BT CT WT TAT 1 1 5 6 0 5 2 3 18 27 6 24 3 5 3 9 1 4"
#   count = stdout_file_content.count(substring)

#   if count == 1:
#     assert True
#   else:
#     assert False

# def test_bk_output1():
#   cwd = os.getcwd()
#   stdout_file = cwd + "/answer/table1-1-fcfs"
#   f = open(stdout_file)
#   stdout_file_content = f.read()
#   f.close()

#   substring = "5	7	23	11	18"
#   count = stdout_file_content.count(substring)

#   if count == 1:
#     assert True
#   else:
#     assert False


# def test_bk_output2():
#   cwd = os.getcwd()
#   stdout_file = cwd + "/answer/table1-1-fcfs"
#   f = open(stdout_file)
#   stdout_file_content = f.read()
#   f.close()

#   substring = "5	14	6	11"
#   count = stdout_file_content.count(substring)

#   if count == 1:
#     assert True
#   else:
#     assert False


# def test_bk_output3():
#   cwd = os.getcwd()
#   stdout_file = cwd + "/answer/table1-1-sjf"
#   f = open(stdout_file)
#   stdout_file_content = f.read()
#   f.close()

#   substring = "5	7	25	13	20"
#   count = stdout_file_content.count(substring)

#   if count == 1:
#     assert True
#   else:
#     assert False


# def test_bk_output4():
#   cwd = os.getcwd()
#   stdout_file = cwd + "/answer/table1-1-sjf"
#   f = open(stdout_file)
#   stdout_file_content = f.read()
#   f.close()

#   substring = "1	4	1	2"
#   count = stdout_file_content.count(substring)

#   if count == 1:
#     assert True
#   else:
#     assert False


# def test_bk_output5():
#   cwd = os.getcwd()
#   stdout_file = cwd + "/answer/table1-2-fcfs"
#   f = open(stdout_file)
#   stdout_file_content = f.read()
#   f.close()

#   substring = "3	17	11	14"
#   count = stdout_file_content.count(substring)

#   if count == 1:
#     assert True
#   else:
#     assert False


# def test_bk_output6():
#   cwd = os.getcwd()
#   stdout_file = cwd + "/answer/table1-2-fcfs"
#   f = open(stdout_file)
#   stdout_file_content = f.read()
#   f.close()

#   substring = "2	9	6	8"
#   count = stdout_file_content.count(substring)

#   if count == 1:
#     assert True
#   else:
#     assert False


# def test_bk_output7():
#   cwd = os.getcwd()
#   stdout_file = cwd + "/answer/table1-2-sjf"
#   f = open(stdout_file)
#   stdout_file_content = f.read()
#   f.close()

#   substring = "34	20	28"
#   count = stdout_file_content.count(substring)

#   if count == 1:
#     assert True
#   else:
#     assert False


# def test_bk_output8():
#   cwd = os.getcwd()
#   stdout_file = cwd + "/answer/table1-2-sjf"
#   f = open(stdout_file)
#   stdout_file_content = f.read()
#   f.close()

#   substring = "3	9	1	4"
#   count = stdout_file_content.count(substring)

#   if count == 1:
#     assert True
#   else:
#     assert False

# def test_pipet5_output1():
#   cwd = os.getcwd()
#   stdout_file = cwd + "/tests/pipe_t5_out"
#   f = open(stdout_file)
#   stdout_file_content = f.read()
#   f.close()
#   print("-----")
#   print(stdout_file)
#   substring = "30"
#   count = stdout_file_content.count(substring)

#   if count == 1:
#     assert True
#   else:
#     assert False

# def test_write_read_output1():
#   cwd = os.getcwd()
#   stdout_file = cwd + "/tests/wr_shared_out1"
#   f = open(stdout_file)
#   stdout_file_content = f.read()
#   f.close()
#   print("-----")
#   print(stdout_file)
#   substring = "This is first write"
#   count = stdout_file_content.count(substring)

#   if count == 1:
#     assert True
#   else:
#     assert False

# def test_psh1_output2():
#   cwd = os.getcwd()
#   stdout_file = cwd + "/tests/psh1_out"
#   f = open(stdout_file)
#   stdout_file_content = f.read()
#   f.close()
#   print("-----")
#   print(stdout_file)
#   substring = "TIME "
#   count = stdout_file_content.count(substring)

#   if count > 0:
#     assert True
#   else:
#     assert False
    
# def test_exec_output1():
#   cwd = os.getcwd()
#   stdout_file = cwd + "/tests/exec_out1"
#   f = open(stdout_file)
#   stdout_file_content = f.read()
#   f.close()
#   print("-----")
#   print(stdout_file)
#   substring = "Hello, Alex"
#   count = stdout_file_content.count(substring)

#   if count == 1:
#     assert True
#   else:
#     assert False

# def test_exec_output2():
#   cwd = os.getcwd()
#   stdout_file = cwd + "/tests/exec_out2"
#   f = open(stdout_file)
#   stdout_file_content = f.read()
#   f.close()
#   print("-----")
#   print(stdout_file)
#   substring = "Hello,"
#   count = stdout_file_content.count(substring)

#   if count == 1:
#     assert True
#   else:
#     assert False