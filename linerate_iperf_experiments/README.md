This Directory contains the three subfolders that hold the experiments performed to verify the that the aggregation completes at line-rate and obtain the data values
for Figure 7 in PANAMA.
|
|
|- baseline				: iperf is used to measure the baseline bandwidth of a TCP connection between two servers connected directly to an Arista Switch (7050S) with no FPGA along the path. 
|
|- fpga_parser_bypass	: iperf is used to measure the baseline bandwidth of a TCP connection between two servers connected to a PSwitch consisting of an FPGA followed by our Arista Switch. 
Since the TCP packets are not marked as aggregation packets, they aggregation path is bypassed.
|
|- fpga_datapath		: Multiple udp connections are launched in parallel to measure the maximum bandwidth that can be supported by the aggregation packets. The servers are connected
to a PSwitch consisting of an FPGA followed by our Arista Switch. The UDP packets sent have their dscp field set to 0x38 such that they are identified as aggregation packets
by the accelerator and traverse the aggregation datapath.


The steps to perform each experiment are provided in the README.md file present within each subfolder.


Important Setup Step:
Prior to running the experiments, complete the following steps:

1. Modify the repo path to match the full path of your cloned repository. 	
	export REPO_HOME=<path to Panama-MLSys-Hardware-Experiments repo>

2.Modify the current ip addresses and the bandwidth of the link in the config file to be representative of the interfaces that are connected.
	export CLIENT_IP=<YOUR_CLIENT_IP_ADDRESS_CLIENT>
	export SERVER_IP=<YOUR_SERVER_IP_ADDRESS_CLIENT>
	export TARGET_BW=<10G>	Default value is 10G for NetFPGA	

3. Source the configuration file to set up the variables for the experiments
	# source config

