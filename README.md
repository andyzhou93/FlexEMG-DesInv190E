# FlexEMG-DesInv190E
This is a simply GUI for recording data using the FlexEMG system. Users can visualize 4 channels of realtime data while automatically saving streamed data from all channels. Data is saved in HDF file format for post processing.

The GUI is composed of three components:
1. Data Visualizer (top)
1. Connection settings (bottom tab)
1. Command Window (bottom tab)

## Connecting to a board
In the bottom of the GUI window, click to the "Connection" tab. If a receiver (control module) is connected, it will populate the dropdown box as "cp2130". Otherwise, connect the control module via USB to the computer and click "Refresh". Once the control module is detected, click "Connect" to connect to the board. When returning to the Command Window, 
