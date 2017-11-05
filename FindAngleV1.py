
# coding: utf-8

# In[14]:

# To read the file csv file
import numpy as np
import  math
print ("Enter the distance in feet")
distance = input()
with open("googleOCR.csv", encoding="utf8") as f:
    listn=[line.split('\t') for line in f]        # create a list of lists
lis  = np.array(listn)       # convert it into an array
finalAngle = []    #list to store all the final angle value
pk = []    #list to store the primary key value
lat = []
lon = []
googleOCRpk = []
image_url = []
image_fov = []
boundingBox = []
locale = []
content = []
heading = []
latGoogleCar = []
longGoogleCar = []
address = []
# below is the process to calculate the finalAngle value and store it in the above list
for i in range(1, len(lis)):
    FOV = int((lis[i][3]))/2    #it is the field of view with respect to the reference axis
    referencePixel = 960    #it is the pixel of the reference axis
    XValue = lis[i,4].split(',')
    signBoardPixelX1 = XValue[0]
    signBoardPixelX1 = int(signBoardPixelX1[1:])    #it is the X1 coordinate of the sign board
    signBoardPixelX2 = int(XValue[1])    #it is the X2 coordinate of the sign board
    avgSignBoardPixel = (signBoardPixelX1 + signBoardPixelX2)/2    #it is average pixel distance from the starting point of image
    distanceFromReferenceAxis = avgSignBoardPixel - referencePixel    #it is the distance of the avg sign board pixel from the reference axis
    anglePerPixel = FOV/(referencePixel) #it is to calculare angle value for 1 pixel
    angleSignBoard = round((anglePerPixel * distanceFromReferenceAxis),7)    #it is to calculate the angle of pixel from the google camera
    #to retrive the Heading value
    Heading = float(lis[i,7])
    pk.append(lis[i][0])
    googleOCRpk.append(lis[i][1])
    image_url.append(lis[i][2])
    image_fov.append(lis[i][3])
    boundingBox.append(lis[i][4])
    locale.append(lis[i][5])
    content.append(lis[i][6])
    heading.append(lis[i][7])
    longGoogleCar.append(lis[i][8])
    latGoogleCar.append(lis[i][9])
    address.append(lis[i][10])
    finalAngleValue = Heading + angleSignBoard
    
    if float(finalAngleValue) > 359.9999999:
        finalAngle.append(round((float(finalAngleValue) - 360),7))
        AngleValue = round((float(finalAngleValue) - 360),7)
    else:
        finalAngle.append(round(float(finalAngleValue),7))
        AngleValue = round(float(finalAngleValue),7)
    finalAngleRadian = math.radians(AngleValue)
    R = 6378.1 #Radius of the Earth
    d = float(distance) * 0.0003048 #Distance in km
    lat1 = math.radians(float(lis[i,9])) #Current lat point converted to radians
    lon1 = math.radians(float(lis[i,8])) #Current long point converted to radians
    lat2 = math.asin( math.sin(lat1)*math.cos(d/R) + math.cos(lat1)*math.sin(d/R)*math.cos(finalAngleRadian))
    lon2 = lon1 + math.atan2(math.sin(finalAngleRadian)*math.sin(d/R)*math.cos(lat1),math.cos(d/R)-math.sin(lat1)*math.sin(lat2))

    lat.append(math.degrees(lat2))
    lon.append(math.degrees(lon2))
    
    
#to put the values in a new csv file

with open('googleOCRAngle.csv','w',encoding="utf8") as file:
    file.write("pk")
    file.write('\t')
    file.write("googleOCRpk")
    file.write('\t')
    file.write("image_url")
    file.write('\t')
    file.write("image_fov")
    file.write('\t')
    file.write("boundingBox")
    file.write('\t')
    file.write("locale")
    file.write('\t')
    file.write("text")
    file.write('\t')
    file.write("heading")
    file.write('\t')
    file.write("lat")
    file.write('\t')
    file.write("long")
    file.write('\t')
    file.write("address")
    file.write('\t')
    file.write("finalAngle")
    file.write('\t')
    file.write("Signlat")
    file.write('\t')
    file.write("Signlong")
    file.write('\n')
    for line in range(0, len(finalAngle)):
        file.write(str(pk[line]))
        file.write('\t')
        file.write(str(googleOCRpk[line]))
        file.write('\t')
        file.write(str(image_url[line]))
        file.write('\t')
        file.write(str(image_fov[line]))
        file.write('\t')
        file.write(str(boundingBox[line]))
        file.write('\t')
        file.write(str(locale[line]))
        file.write('\t')
        file.write(str(content[line]))
        file.write('\t')
        file.write(str(heading[line]))
        file.write('\t')
        file.write(str(latGoogleCar[line]))
        file.write('\t')
        file.write(str(longGoogleCar[line]))
        file.write('\t')
        file.write(str(address[line]).split('\n')[0])
        file.write('\t')
        file.write(str(finalAngle[line]))
        file.write('\t')
        file.write(str(lat[line]))
        file.write('\t')
        file.write(str(lon[line]))
        file.write('\n')
        
#print (str(address[line]).split('\n')[0])


# In[ ]:



