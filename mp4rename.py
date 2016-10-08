import json, os, os.path, glob
  
import sys  

#reload(sys)  
sys.setdefaultencoding('utf8')

filefolderlist = glob.glob("/users/Administrator/Desktop/VMworld2016/*.mp4")
extendedfiles = [item.replace('/users/Administrator/Desktop/VMworld2016/','') for item in filefolderlist]
filenames = [item.replace('.mp4','') for item in extendedfiles]

with open('networking_and_security.json') as json_data:
    data = json.load(json_data)
    for output in data['PresentationDetailsList']:
        session_name = output['Name']
        for filename in filenames:
            #print filename
            if filename in session_name:
                print "Original: "+filename+".mp4"+" New: "+session_name+".mp4"
                os.rename(filename+".mp4", session_name+".mp4")