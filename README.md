# floodgates

Calculate the water (gray) in between the gates with the hieght of each gate as input
![image](https://raw.githubusercontent.com/its-a-unixsystem/floodgates/main/Screenshot%20from%202022-08-16%2010-25-31.png)


Usage: `flood.py [gates]`

ie (from the example, also see picture):
![output](https://github.com/its-a-unixsystem/floodgates/blob/main/20220817_13h56m26s_grim.png?raw=true)

    # ./flood.py 0 0 4 0 0 6 0 0 3 0 8 0 2 0 5 2 0 3 0 0
    Flood [ 2 - 5 ] water: 8
    Flood [ 5 - 10 ] water: 21
    Flood [ 10 - 14 ] water: 13
    Flood [ 14 - 17 ] water: 4
    Water amount: 46


The output lists each flood segment with
    `[ start - end position]`
and how many blocks of water it would fill.
At the end the sum of all segments is printed.

The testing (pytest) is very basic.
Hope you like it!
