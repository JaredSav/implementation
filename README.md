# CS 3030 Final Project Implementation

## Purpose
This program is designed to run a Greenhouse
At 15 minute intervals it will be run to check:
1. Sunlight. If between the hours of 0800 - 1600 the sunlight senors do not detect enough sunlight outside the internatl lights will come on to ensure the best growing contitions.
2. Temperature. It will continually monitor that the temperature stay within the proper range for plant development. If deviations are found it will have the ability to access the heating and cooling systems.
3. Moisture. Soil sensors will keep track of soil saturation. If needed the system can turn on it's own watering systems.


## Agruments
This program is designed to run entirely on it's own however it will support the following agrumnets when run manualy.
-a | --all		This will run the file and present all information
-s | --sun		This will present the current light level
-t | --temperature	This will present the current room temperature
-m | --moisture		This will present the current moisture level
-e FILE | --email FILE	The FILE needs to contain email configuration options. Default to email.conf
-h | --help		Print usage statment and exit


all, will check all of the sensors, and give you the status of the systems that use those systems.
sun, will only check the sunlight sensor, and give you the status of the internal lights
temperture, will check the current room temperture and give you the status of the AC and heater
moisture, will check the soil moisture level, and give you the status of the sprinklers
email, will check the status of all sensors, and send the information to you in an email.

The email.conf file is included, and it outlines the fields that are needed to send an email.
