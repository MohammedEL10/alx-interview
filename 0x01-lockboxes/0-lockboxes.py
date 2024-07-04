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
    counter = 0
    total_boxes = len(boxes)
    for key in boxes[0]:
        if key < total_boxes and key not in setOfkeys and key > 0:
            setOfkeys.append(key)
            counter += 1
    index = 0
    while index < len(setOfkeys):
        setkey = setOfkeys[index]
        # print("setOfkeys", setOfkeys)
        # print("key number:", setOfkeys[index])
        # print("setOfkeys length start", len(setOfkeys))
        # print("opening box:", boxes[setkey])
        setkey = setOfkeys[index]
        for key in boxes[setkey]:
            print("opening box:", boxes[index])
            if key < total_boxes and key not in setOfkeys and key > 0:
                setOfkeys.append(key)
                counter += 1
            index += 1
            # print("setOfkeys", setOfkeys)
            # print("setOfkeys length end:", len(setOfkeys))
            # print("++++++")
        print("total keys:", counter)
        if (counter == total_boxes-1):
            return True
        else:
            return False