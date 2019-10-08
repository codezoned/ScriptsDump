def Tower(start, end, middle, blockNo):
    # start , middle , end , blockNo =
    # params[0] , params[1] , params[2] , params[3]
    if blockNo == 1:
        print("Moved block 1 from", start, "to", end)
        return
    Tower(start, middle, end, blockNo-1)
    print("Moved block", blockNo, "from", start, "to", end)
    Tower(middle, end, start, blockNo-1)


# paramList = ['Tower A', 'Tower C', 'Tower B' , 3]
Tower('Tower A', 'Tower C', 'Tower B', 3)
