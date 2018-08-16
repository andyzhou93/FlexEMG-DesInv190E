# FlexEMG-DesInv190E
This is a simple GUI for recording data using the FlexEMG system. Users can visualize 4 channels of real time streamed data while automatically saving streamed data from all channels. Data is saved in HDF file format for post processing.

The GUI is composed of three components:
1. Data Visualizer (top)
1. Connection settings (bottom tab)
1. Command Window (bottom tab)

## Connecting to a board
In the bottom of the GUI window, click to the "Connection" tab. If a receiver (control module) is connected, it will populate the dropdown box as "cp2130". Otherwise, connect the control module via USB to the computer and click "Refresh". Once the control module is detected, click "Connect" to connect to the board. The command window should display "Connected to cp2130".

## Command Window
Command Window outputs can be saved by clicking the "Save Log" button. This will open up a dialog allowing the user to specify a save location. The command window can be cleared by clicking the "Clear" button. 

## Data Visualizer
The Data Visualizer shows four plots with real time updated waveforms of user selectable channels. Channels are selected from the four input boxes at the bottom. A checkbox to display stream data can be unchecked in order to save data without any visualization. Data is always saved, regardless of whether it is plotted.

Data streaming is started by pressing the "Stream Data" button. Upon starting, the Command Window will display some configuration steps, followed by the phrase "FlexEMG board connected and ready" and a timestamp of the start time to indicate that the device is connected and operational. Pressing the "Stream Data" button again ends the stream. The Command Window will display the steam stop timestamp, followed by statistics of the received packets. 

## Saved data and loading into Matlab
Saved data streams are located in the directory "data/hdfs/" in HDF file format. Filenames are the timestamp of the start of the stream in "YYYYMMDD-hhmmss.hdf" format.

A Matlab function "load_FlexEMG_HDF.m" for loading the data is included. The function can be called with a filename as its only argument, or with no arguments. When called without arguments, the function opens a dialog box to select the file to be loaded. The function returns an N x 64 array, where N is the number of samples recorded. Samples are recorded at 1 kS/s.

## Real time processing
A blank function for inserting any potential real time processing commands has been included. The function is called "FlexEMG_DataOp", located in the file "DataOp.py". It is called every 50ms when streaming. The passed argument "data" is a 50 x 64 element list containing 50 data samples from each of the 64 recorded channels.
