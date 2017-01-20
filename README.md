# rtls


to setup:
server: 
sw: wp_server.py

client1:
sw: wp_client1.py
hw: shimmer dock, S4Sdk, dwm1000
fw: \dwm1000\sdk_dwm1000_6_ds_twr_LS: Anchor, 1

client2:
sw: wp_client2.py
hw: shimmer dock, S4Sdk, dwm1000
fw: \dwm1000\sdk_dwm1000_6_ds_twr_LS: Anchor, 2

Tag: 
hw: S4Sdk, dwm1000
fw: \dwm1000\sdk_dwm1000_6_ds_twr_LS: Tag, 0


refer to http://www.lfd.uci.edu/~gohlke/pythonlibs/ for missing py packets
in Windows to install *.whl, use:
>pip install xxxxxx.whl 
