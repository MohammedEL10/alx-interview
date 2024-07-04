#!/usr/bin/python3
def canUnlockAll(boxes):
    """
    take boxes
        create set of keys
        go to box0
            get all key and set them setOfkeys
        start oppening boxes from setOfkeys
            go to each box from to each key
                and take the keys from it and add them to set of keys
            keep looping through all set of keys
        ignore keys that don't have box
        track opening of boxes by a counter, if at end it equal to length
        of boxes it mean all boxes unlock
    """
    print("boxes", boxes)
    print("total boxes", len(boxes))
    setOfkeys = []
    total_boxes = len(boxes)
    for key in boxes[0]:
        if key < total_boxes and key not in setOfkeys:
            setOfkeys.append(key)
    print("setOfkeys", setOfkeys)
    index = 0
    while index < len(setOfkeys):
        print("setOfkeys", setOfkeys)
        print("key number:", setOfkeys[index])
        print("setOfkeys length start", len(setOfkeys))
        for key in boxes[index]:
            print("opening box:", boxes[index])
            if key < total_boxes and key not in setOfkeys:
                setOfkeys.append(key)
            index += 1
            print("setOfkeys length end:", len(setOfkeys))
            print("++++++")
    print("____")