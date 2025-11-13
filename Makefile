compile1:
	echo "No build -- cannot build ESP32"
	# gcc -pthread ./answer/fcfs.c -o ./fcfs
compile2:
	echo "compiling sjf.c"
	#gcc -pthread ./answer/sjf.c -o ./sjf
compile3:
	#echo "compiling pc_works.c and pc_fig.c"
	#gcc -pthread ./answer/pc_works.c -o ./pc_works
	#gcc -pthread ./answer/pc_fig.c -o ./pc_fig
test:
	bash ./script_test/test1.sh
	# bash ./script_test/test0.sh
	#bash ./script_test/test2.sh

done:
	#rm -rf ./tests/pc_pid_out
	#rm -rf ./tests/mmyfork_out
	echo "finished"

