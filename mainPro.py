import usersql
import serialconnect
import camera

from multiprocessing import Process


#sql = usersql.insertUser("alice", "1234", "beijing", 19.62)

#results = usersql.selectUser(4)

def mainLoop():
    qrcodetext = camera.cameraLogin()
    qrcodetext = qrcodetext.decode("utf-8")
    print("recognizing over", qrcodetext)
    #对识别到的字符串做一个拆分
    information = spiltqrcode(qrcodetext)
    
    id = int(information.get("id"))
    results = usersql.selectUser(id)
    
    if(results):
         ser = serialconnect.Ser("/dev/ttyS0")
         ser.send_cmd("OPENCOVER".encode("utf-8"))
         
         #单片机返回盖子关上信号， 暂时定为CCS
         response = ser.listen_port(3)
         print("response is %s"%response)
         if(response == "CCS"):
             #调用识别图像模块
             print("vc")
        
         else:
             print("no")             


def spiltqrcode(qrcodetext):
    #todo
    qrcodetext = qrcodetext.replace(" ","")
    tmp = qrcodetext.split(",")
    result = {}
    for i in tmp:
        tmp_list = i.split("=")
        result[tmp_list[0]] = tmp_list[1]
    
    return result 

   
        
    

