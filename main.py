import matplotlib.pyplot as plt
import pickle

def main():
    
    # z_dics = dict()
    
    with open("pig_perfect_play.bin", 'rb') as f:
        z_dics = pickle.load(f)

    # with open("test.txt", 'r') as f:
    #     for line in f:
    #         cord = line.rstrip(',\n').split(' ')
    #         for i in range(3):
    #             cord[i] = float(cord[i])
    #             if cord[i] == 0.9:
    #                 cord[i] = int(0)
    #             else:
    #                 cord[i] = int(math.ceil(cord[i]))

    #         z_dics[cord[2]] = z_dics.get(cord[2], list())
    #         z_dics[cord[2]].append(cord)
            
    #         if cord[2] == current_z:
    #             z_dics[current_z].append(cord)
    #         else:
    #             current_z = cord[2]
    #             z_dics[current_z] = list()
    #             z_dics[current_z].append(cord)
    
    #plotData(z_dics[50])

    # for i in z_dics.keys():
    #     #print(i)
    #     plotData(z_dics[i])

    plot2dto3d(z_dics)

    plt.xlim(100, 0)
    plt.xlabel("player 2 points")
    plt.ylabel("player 1 points")
    
    plt.show()

def plot2dto3d(z_dics):
    fig = plt.figure()
    ax = fig.add_subplot(projection = '3d')

    for i in z_dics.keys():
        x = list(z_dics[i].keys())
        y = list(z_dics[i].values())
        ax.plot(x, y, zs=i, zdir="y")

    ax.set_zlabel('round score')
    ax.set_xlim(0,100)
    ax.set_ylim(0,100)
    ax.set_zlim(0,100)


def plotData(higestVal_dic):
    x = higestVal_dic.keys()
    y = higestVal_dic.values()
    
    plt.scatter(x,y)

def findCealing(cordList):
    cordList.reverse()
    higestVal_dic = dict()
    for cord in cordList:
        higestVal = higestVal_dic.get(cord[0], 0)
        if higestVal < cord[1]:
            higestVal_dic[cord[0]] = cord[1]
    higestVal_dic = dict(sorted(higestVal_dic.items()))
    return higestVal_dic

def cleanData(cordList):
    for cord in cordList:
        for i in range(3):
            cord[i] = float(cord[i])
            if cord[i] == 0.9:
                cord[i] = int(0)
            else:
                cord[i] = int(math.ceil(cord[i]))

if __name__ == "__main__":
    main()