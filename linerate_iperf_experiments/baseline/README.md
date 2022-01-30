Experiment Steps:

1. Connect two servers to switch ports.

1. Make sure you have set up the environment variables properly in ../config

2. Start iperf server on the server machine:
	# source run_iperf_server.bash

3. Start iperf client on the client machine:
	# source run_iperf_client.bash

The current client runs for 310 seconds and the bandwidth is recorded every 10 seconds resulting in a total of 300 data points.

Experiment output files in current folder:

switch_baseline_summary.txt		# Logs the observed bandwidth in every 10 second interval

raw_switch_baseline_summary_gbps.txt 	# Generated data point pairs from the summary log for plotting using tikz in latex


The resulting output files are then copied into results_summary folder in the RESULTS_FOLDER specified in ../config. 

Note:
plot_cdf.py can be used to plot a CDF in python pyplot using the resulting output file:
	# python plot_cdf.py --fname switch_baseline_summary.txt
