#!/bin/bash


iperf -B $CLIENT_IP -c $SERVER_IP -P 4 -b $TARGET_BW  -t 310 -i 1  > fpga_parser_bypass.txt

cat switch_baseline.txt | grep SUM | awk ' NR>11 {print $7}' > fpga_parser_bypass_summary.txt

if [ ! -d "$RESULTS_FOLDER" ]; then
	mkdir $RESULTS_FOLDER
fi

python create_raw_file.py fpga_parser_bypass__summary.txt

cp fpga_parser_bypass_summary.txt $RESULTS_FOLDER
cp raw_fpga_parser_bypass_summary.txt $RESULTS_FOLDER
