#!/bin/bash

# This script, when run, creates X amounts of virtual machines in an azure subscription,
# with incrementing names (vm-1, vm-2, vm-3 etc) 
# set all variables, log in to az-cli with 'az login' and run the script.

# The public IPs of the VMs are out printed out 
# at the bottom of the prompt when the operation is complete

# Variables
 vmcount=""					# amount of VMs you want to create
 resourcegroup=""	# Resource Group
 vmname=""					# Name of Virtual Machine, becomes "name-1".."name-30", depends on the number in $vmcount
 	increment="+1"				# Variable to increment Virtual Machine names (DO NOT CHANGE)
 netsecgroup=""			# Network Security Group
 nsgrule="ssh"					# Can be "ssh" or "rdp"
 subnetname=""		# Subnet Name
 loc=""				# Location (west europe, west us, etc.)
 virtualnetwork=""		# Virtual Network Name
 admuser=""				# Admin Username
 sshkeyloc=""	# Location of ssh key file
 os=""					# Operating System
 vmsize=""		# Virtual Machine specs

# Create resource requirements  - operation fails if this does not exist
 az group create -n $resourcegroup
 az network vnet create -g $resourcegroup \
 	-n $virtualnetwork \
 	-l $loc \
 	--subnet-name $subnetname

# Loop to create the virtual machines
 for run in {1..$vmcount}
 do
	az vm create -g $resourcegroup \
		-n $vmname"-"$((increment++)) \
		--nsg $netsecgroup \
		--nsg-rule $nsgrule \
		--subnet $subnetname \
		-l $loc \
		--vnet-name $virtualnetwork \
		--admin-username $admuser \
		--authentication-type ssh \
		--ssh-key-value $sshkeyloc \
		--image $os \
		--size $vmsize \
		#--no-wait
 done

# spits out the public IP addresses in a neatly organized list
 az network public-ip list -g $resourcegroup \
  --out yaml \
  | grep -e "name\|ipAddress" \
  | grep -v "null\|Basic" \
  | awk '{getline x;print x;}1'\
  | awk '{print $2}' \
  | sed 'N;s/\n/ /' \

	# Example
	# vmname-1PublicIP 23.11.158.166
	# vmname-2PublicIP 13.22.45.146
	# vmname-3PublicIP 13.33.3.28
	# vmname-4PublicIP 13.44.182.227
	# vmname-5PublicIP 13.55.179.164
	# vmname-6PublicIP 13.66.176.226
