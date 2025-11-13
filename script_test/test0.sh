echo "Running tests..."

CUR=$(pwd)
echo $CUR
SCRIPT_DIR=$CUR"/script_test"
TEST_DIR=$CUR"/tests"
ANS_DIR=$CUR"/answer"
echo $SCRIPT_DIR


output1=$(./fcfs <<EOF
3
1 5
3 18
5 3
^C
EOF
)
PIPET1_OUT=$TEST_DIR"/fcfs_out1"
echo "output--fcfs#1"
echo $output1
echo $output1 > $PIPET1_OUT
cat $PIPET1_OUT

output2=$(./sjf <<EOF
3
1 5
3 18
5 3
^C
EOF
)
PIPET2_OUT=$TEST_DIR"/sjf_out1"
echo "output--sjf#1"
echo $output2
echo $output2 > $PIPET2_OUT
cat $PIPET2_OUT

# output2=$(./psh2 <<EOF
#   ls
#   -lt
#   ^C
# EOF
# )
# PSH1_OUT=$TEST_DIR"/psh2_out"
# echo $output2 > $PSH1_OUT

echo "Output prepared."

exit 0