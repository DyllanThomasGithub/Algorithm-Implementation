#Group 11: JT Ellis, Dyllan Thomas

# Tyler Moore
# P3 Starter Code, CS 2123 The University of Tulsa
# Implementation of interval partitioning algorithm

#Reference: https://stackoverflow.com/questions/1679384/converting-dictionary-to-list

import datetime
from heapq import heappush , heappop , heapify

def scheduleRooms(rooms,cls):
    """
    Input: rooms - list of available rooms
           cls   - dictionary mapping class names to pair of (start,end) times
    Output: Return a dictionary mapping the room name to a list of
    non-conflicting scheduled classes.
    If there are not enough rooms to hold the classes, return 'Not enough rooms'.
    """
    rmassign = {}
    clslist = []  #initialize list of classes, to be kept in a min heap based on start time
    heapify(clslist)
    numrooms = 0
    sortedrooms = []  #initialize priority queue based on finish time of each classroom's last lecture
    heapify(sortedrooms)

    for key, value in cls.iteritems():
        heappush(clslist, [value, key])  #flipping pairs of classes and times, pushing them into the heap to be sorted

    if len(rooms) is 0:  #if we don't have any rooms
        return 'Not enough rooms'

    while clslist:  #run the code
        consider = heappop(clslist)  #consider a class

        if numrooms == 0:  #if this is the first class, place it in a room
            temp = rooms[numrooms]
            numrooms += 1
            heappush(sortedrooms, (consider[0][1], temp))  #allocate a room, add it to the priority queue (key = finish time of its last lecture)
            rmassign[temp] = [consider[1]]  #add the room to dictionary, with the class

        else:  #this is not the first class
            roomk = heappop(sortedrooms)  #the room, k, with the earliest end time
            if consider[0][0] >= roomk[0]:  #if our class begins after k, push it into the room and update the room's key
                heappush(sortedrooms, (consider[0][1], roomk[1]))
                rmassign[roomk[1]].append(consider[1])  #add the class to dictionary
            else:  #our class begins before k, we need to allocate a new room
                heappush(sortedrooms, roomk)
                try:  #do we have enough rooms?
                    temp = rooms[numrooms]
                except:  #we don't: code fails
                    return 'Not enough rooms'
                numrooms += 1  #we do: allocate the next one
                heappush(sortedrooms, (consider[0][1], temp))
                rmassign[temp] = [consider[1]]

    return rmassign


if __name__=="__main__":
    cl1 = {"a": (datetime.time(9),datetime.time(10,30)),
           "b": (datetime.time(9),datetime.time(12,30)),
           "c": (datetime.time(9),datetime.time(10,30)),
           "d": (datetime.time(11),datetime.time(12,30)),
           "e": (datetime.time(11),datetime.time(14)),
           "f": (datetime.time(13),datetime.time(14,30)),
           "g": (datetime.time(13),datetime.time(14,30)),
           "h": (datetime.time(14),datetime.time(16,30)),
           "i": (datetime.time(15),datetime.time(16,30)),
           "j": (datetime.time(15),datetime.time(16,30))}
    rm1 = [1,2,3]
    #print(cl1)
    #print(scheduleRooms(rm1,cl1))
    #print(scheduleRooms([1,2],cl1))
    ensrooms = ['KEH U1','KEH M1','KEH M2','KEH M3','KEH U2','KEH U3','KEH U4','KEH M4','KEH U8','KEH U9']
    csclasses = {'CS 1043': (datetime.time(9,30),datetime.time(11)),
              'CS 2003': (datetime.time(10,30),datetime.time(12)),
              'CS 2123': (datetime.time(11,15),datetime.time(12,45)),
              'CS 3003': (datetime.time(8,15),datetime.time(11,30)),
              'CS 3353': (datetime.time(11),datetime.time(12)),
              'CS 4013': (datetime.time(13),datetime.time(14,45)),
              'CS 4063': (datetime.time(12,30),datetime.time(14,30)),
              'CS 4123': (datetime.time(14),datetime.time(15)),
              'CS 4163': (datetime.time(14),datetime.time(16,30)),
              'CS 4253': (datetime.time(12),datetime.time(16)),
    }

    print("List of classes in ensrooms:")
    print(csclasses)

    print("\nTest with no rooms:")
    print(scheduleRooms([],cl1))

    print("\nTest with sufficient rooms:")
    print(scheduleRooms(ensrooms,csclasses))

    print("\nTest with insufficient rooms, but more than zero:")
    print(scheduleRooms(ensrooms[:4],csclasses))