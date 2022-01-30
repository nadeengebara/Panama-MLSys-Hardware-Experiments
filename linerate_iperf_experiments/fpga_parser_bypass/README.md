Experiment Steps:

Connect two servers to switch ports.

1. Make sure you have set up the environment variables properly in ../config

2. Start iperf server on the server machine:
	# source run_iperf_server.bash

3. Start iperf client on the client machine:
	# source run_iperf_client.bash

The current client runs for 310 seconds and the bandwidth is recorded every 10 seconds resulting in a total of 300 data points.

Experiment output files in current folder:

fpga_parser_bypass.txt			# dump of iperf output every 10 seconds

fpga_parser_bypass_summary.txt		# Log of the bandwidth observed every 10 seconds obtained from fpga_parser_bypass.txt

raw_fpga_parser_bypass_summary_gbps.txt 	# Generated data point pairs for tikx plotting obtained from fpga_parser_bypass_summary.txt


The resulting output files are then copied into results_summary folder in the RESULTS_FOLDER specified in ../config. 

Note:
plot_cdf.py can be used to plot a CDF in python pyplot using the resulting output file:
	# python plot_cdf.py --fname fpga_parser_bypass_summary.txt
