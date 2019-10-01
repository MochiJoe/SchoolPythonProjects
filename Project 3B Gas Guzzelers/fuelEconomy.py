def convertData(filename):
    infile=open(filename,"r")
    datalist=infile.readlines()
    dlist=[]
    for i in range(len(datalist)):
         dlist.append(float(datalist[i]))
    return(dlist)


def averageMPG(dataList):
    sum=0
    for i in range(len(dataList)):
        sum=sum+(dataList[i])
    return (round(sum/(len(dataList)),2))


def countGasGuzzlers(list1, list2):
    count = 0
    for i in range(len(list1)):
        if (list1[i]) < 22:
            count = count + 1           
        elif (list2[i]) < 27:
            count=count + 1
    return (count)


def output(tot_vehic, avg_city, avg_hwy, gasGuzz):
    print("The total number of vehicles tested was ",
          len(tot_vehic),".",sep="")
    print("The average for the city mpg for all the vehicles tested is ",
          avg_city,".", sep="")
    print("The average for the highway mpg for all the vehicles tested is ",
          avg_hwy,".", sep="")
    print("The number of gas guzzlers among the vehicle models tested is ",
          gasGuzz, ".", sep="")
    

def main():
    # function 1
    dataList_city = convertData("carModelData_city")
    dataList_hwy = convertData("carModelData_hwy")

    # function 2
    avgMPG_city = averageMPG(dataList_city)
    avgMPG_hwy = averageMPG(dataList_hwy)

    # function 3
    gasGuzz = countGasGuzzlers(dataList_city, dataList_hwy)

    # function 4
    Results = output(dataList_city, avgMPG_city, avgMPG_hwy, gasGuzz)

    
main()
