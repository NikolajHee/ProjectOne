#lavet af Gustav: s214585


import numpy as np

def dataLoad(filename):
    """
    Parameters
    ---------
    filename: Name of file containing Nx3-matrix 

    Returns
    -------
    Nx3-Matrix but filtered (compromised rows are excluded)
    """
    file=open(filename,"r")
    #An array with the txt file's lines
    aMatrix=np.array(file.read().splitlines())
    # Arrays with zeros based on the number of lines in the file
    temp=np.zeros(len(aMatrix))
    growth=np.zeros(len(aMatrix))
    bacteria=np.zeros(len(aMatrix))

    #Converts all the strings to floats
    for i in range(len(aMatrix)):
        A=list(map(float,aMatrix[i].split()))
        B=np.array(A)
        if (10<=B[0]<=60) & (B[1]>0) & (B[2]==1 or B[2]==2 or B[2]==3 or B[2]==4):
            temp[i]=B[0]
            growth[i]=B[1]
            bacteria[i]=B[2]
        elif 10>B[0] or B[0]>60:
            print("Error line", i+1,"\n--> The temperature isn't between 10 and 60!")
        elif B[1]<=0:
            print("Error line", i+1,"\n--> The growth rate isn't above zero!")
        else:
            print("Error line", i+1,"\n--> The chosen type of bacteria doesn't work!")
     
 
    #sætter de tre arrays sammen, men får at få dem som kolonner transponeres matrixen
    bmatrix=np.vstack((temp,growth,bacteria)).T
    #Danner en ny matrix med alle rækkerne, som ikke er nuller
    data= bmatrix[np.all(bmatrix != 0,axis=1)]

    return data




