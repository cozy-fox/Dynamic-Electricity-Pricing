# Dynamic Electricty Pricing

This project was made for the Summer Internship, GAIP at National University of Singapore under NUS and Hewlett Packard Enterprise faculty. It presents an IoT solution where power consumption of varioud households and industries and is sent to a cloud service on an hourly basis. On basis of this data, a graph is plotted of various sectors and their hourly consumption. Machine Learning is used to predict the peak hours of consumption.
The problem is that Power Supply grids in cities have a slow response time according to the demand and hence waste a lot of power duw to delayed response and uneven distribution. If the cost of electricty is dynamically regulated high during the peak hours and low during the other hours, people will be incentivised to shift work which is not urgent to the cheaper hours, saving a lot of economic resources.


## Project

The first Raspberry Pi simulator is a code for https://azure-samples.github.io/raspberry-pi-web-simulator/#GetStarted to simulate incoming data from an online RaspberryPi to IoT Hub.
The second backend directory has all the scripts to host a web service, to show the data ,check prices, see personal profile and bill etc.
