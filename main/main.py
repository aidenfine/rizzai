import pickle
import string
global Lrdetect_Model

LrdetectFile = open('model.pckl','rb')
Lrdetect_Model = pickle.load(LrdetectFile)
LrdetectFile.close()
input = ""
test = False

if test:
    print(Lrdetect_Model.predict([input])


print(input)