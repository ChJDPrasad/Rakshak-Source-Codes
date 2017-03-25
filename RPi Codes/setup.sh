#! bin/sh

# Set RPi IP Address 
# The IP Address used for login 
export RPI_IP=10.42.0.61

# Set Master IP Address
# Your laptop's IP ':11311' part doesn't change
export RPI_MASTER_URI=http://10.101.201.12:11311

#build your catkin ws
catkin_make
source devel/setup.bash
