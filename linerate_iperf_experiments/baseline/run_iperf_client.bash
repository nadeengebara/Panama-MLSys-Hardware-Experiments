#!/bin/bash


iperf -B $CLIENT_IP -c $SERVER_IP -P 4 -b $TARGET_BW  -t 310 -i 1  > switch_baseline.txt

cat switch_baseline.txt | grep SUM | awk ' NR>11 {print $7}' > switch_baseline_summary.txt

if [ ! -d "$RESULTS_FOLDER" ]; then
	mkdir $RESULTS_FOLDER
fi

python create_raw_file.py switch_baseline_summary.txt

cp switch_baseline_summary.txt $RESULTS_FOLDER
cp raw_switch_baseline_summary_gbps.txt $RESULTS_FOLDER
