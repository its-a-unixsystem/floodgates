#!/usr/bin/python
"flood"
import sys
import pytest

# known bugs:
# - at least one gate >0 must exist
# - confusing resuing of variables due to python by ref/by value mixing

# example
#  0 0 4 0 0 6 0 0 3 0  8  0  2  0  5  2  0  3  0  0
#  0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19

def find_next_highest(FloodGates, start, last_highest):
    "find the next highest gate from start, returns height and position"

    while start < len(FloodGates):
        # we skip leading zero gates and compare with last_highest
        if int(FloodGates[start])>=last_highest and int(FloodGates[start])>0:
            last_highest=int(FloodGates[start])
            return last_highest,start
        start+=1

        # return False in case we foung nothing
    return False

def findNextLowest(FloodGates,RelevantGates):
    "iterate through lower heights to find something lower"

    # start at last known gate
    lowered_height=RelevantGates[-1]['height']

    # increment position, we worked on pos already
    lowered_pos=RelevantGates[-1]['pos']+1

    # we try to lower the height one by one
    while lowered_height > 0:
        lowered_height-=1
        
        try:
            height,pos=find_next_highest(FloodGates,lowered_pos, lowered_height)

        except TypeError:
            continue

        return height,pos
            
def loopThroughFloodGates(FloodGates,RelevantGates):
    "loop through FloodGates, add relevant ones to RelevantGates"

    height=0
    pos=0
    
    ipos=0

    # we iterate through the full length
    # ipos gets modified during loop to skip
    while ipos<len(FloodGates):
        try:
            height,pos=find_next_highest(FloodGates,ipos,height)

        # Hack, we return only one value in case we reach end of list
        # without finding one, so lets see if we have a lower one
        except TypeError:
            try:
                height,pos=findNextLowest(FloodGates,RelevantGates)
            except TypeError:
                break

        # add to list with relevant gates
        RelevantGates.append({'height':height,'pos':pos})
        
        # we reset the loop to the last known block
        # no need to check in-between RelevantGates
        ipos=pos

        # increment loop
        ipos+=1
    return True

def countFlood(FloodGates,RelevantGates):
    "count waterlevel between RelevantGates in FloodGates"
    pos=0
    flood=0

    # iterating through all relevant gates
    # comping to next, so skip last
    for pos in range(len(RelevantGates)-1):
        flood_segment=0

        # compare each segment/find filling height
        for segment in range(RelevantGates[pos]['pos']+1,RelevantGates[pos+1]['pos']):

            if RelevantGates[pos]['height']<RelevantGates[pos+1]['height']:
                max_height=RelevantGates[pos]['height']
            else:
                max_height=RelevantGates[pos+1]['height']

            flood_segment=flood_segment+max_height-int(FloodGates[segment])

        print("Flood [",RelevantGates[pos]['pos'],"-",RelevantGates[pos+1]['pos'],"] water:",flood_segment)
        flood+=flood_segment

    return flood

def test_loopGates():
    "basic pytest for functions"
    
    RelevantGates=[]
    flood=0
    testgates=["3","0","4"]
    
    assert loopThroughFloodGates(testgates,RelevantGates)
    assert RelevantGates==[{'height': 3, 'pos': 0}, {'height': 4, 'pos': 2}]
    flood=countFlood(testgates,RelevantGates)
    assert flood==3
    
def main(argv=None):
    "main"
    RelevantGates=[]
    flood=0

    loopThroughFloodGates(argv,RelevantGates)

    flood=countFlood(argv,RelevantGates)
    print("Water amount:",flood)
    
# some say it's cargo cult
if __name__ == "__main__":
    main(sys.argv[1:])
