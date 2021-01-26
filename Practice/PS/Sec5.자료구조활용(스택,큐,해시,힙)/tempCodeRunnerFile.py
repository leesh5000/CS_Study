    sys.stdout = sys.__stdout__
    if filecmp.cmp("./PS/source/in{}.txt".format(i), "./PS/source/myout{}.txt".format(i)):
        print("Test #%d : Success"%(i))
    else:
        print("Test #%d : Fail"%(i))