import os
import sys
import socket
import time
import subprocess

hostIp = "192.168.4.1"
hostPort = 7878
delay = 0.02
retries = 2
retryDelay = 0.01
keyUpAction = "CK0\t0"
pressEnter = "CK0\t40"
password = str(sys.argv[1:][0])

def pingHost(host):
    response = os.system("ping -c 1 " + host + "  >/dev/null")
    if response:
        return(0)
    else:
        return(1)

def checkHostAlive():
    count = 0
    while True:
        count += 1
        print("Connecting...")
        if pingHost(hostIp):
            break
        if count > 4:
            print("Device is not responding!")
            sys.exit(1)

# Germand Keyboard Scancodes
keyboardActions = { "a": "CK0\t04",
                    "b": "CK0\t05",
                    "c": "CK0\t06",
                    "d": "CK0\t07",
                    "e": "CK0\t08",
                    "f": "CK0\t09",
                    "g": "CK0\t10",
                    "h": "CK0\t11",
                    "i": "CK0\t12",
                    "j": "CK0\t13",
                    "k": "CK0\t14",
                    "l": "CK0\t15",
                    "m": "CK0\t16",
                    "n": "CK0\t17",
                    "o": "CK0\t18",
                    "p": "CK0\t19",
                    "q": "CK0\t20",
                    "r": "CK0\t21",
                    "s": "CK0\t22",
                    "t": "CK0\t23",
                    "u": "CK0\t24",
                    "v": "CK0\t25",
                    "w": "CK0\t26",
                    "x": "CK0\t27",
                    "z": "CK0\t28",
                    "y": "CK0\t29",
                    "1": "CK0\t30",
                    "2": "CK0\t31",
                    "3": "CK0\t32",
                    "4": "CK0\t33",
                    "5": "CK0\t34",
                    "6": "CK0\t35",
                    "7": "CK0\t36",
                    "8": "CK0\t37",
                    "9": "CK0\t38",
                    "0": "CK0\t39",
                    " ": "CK0\t44",
                    "ß": "CK0\t45",
                    "´": "CK0\t46",
                    "ü": "CK0\t47",
                    "+": "CK0\t48",
                    "#": "CK0\t49",
                    "ö": "CK0\t51",
                    "ä": "CK0\t52",
                    "^": "CK0\t53",
                    ",": "CK0\t54",
                    ".": "CK0\t55",
                    "-": "CK0\t56",
                    "<": "CK0\t100",
                    "A": "CK2\t04",
                    "B": "CK2\t05",
                    "C": "CK2\t06",
                    "D": "CK2\t07",
                    "E": "CK2\t08",
                    "F": "CK2\t09",
                    "G": "CK2\t10",
                    "H": "CK2\t11",
                    "I": "CK2\t12",
                    "J": "CK2\t13",
                    "K": "CK2\t14",
                    "L": "CK2\t15",
                    "M": "CK2\t16",
                    "N": "CK2\t17",
                    "O": "CK2\t18",
                    "P": "CK2\t19",
                    "Q": "CK2\t20",
                    "R": "CK2\t21",
                    "S": "CK2\t22",
                    "T": "CK2\t23",
                    "U": "CK2\t24",
                    "V": "CK2\t25",
                    "W": "CK2\t26",
                    "X": "CK2\t27",
                    "Z": "CK2\t28",
                    "Y": "CK2\t29",
                    "!": "CK2\t30",
                    '"': "CK2\t31",
                    "§": "CK2\t32",
                    "$": "CK2\t33",
                    "%": "CK2\t34",
                    "&": "CK2\t35",
                    "/": "CK2\t36",
                    "(": "CK2\t37",
                    ")": "CK2\t38",
                    "=": "CK2\t39",
                    "?": "CK2\t45",
                    "`": "CK2\t46",
                    "Ü": "CK2\t47",
                    "*": "CK2\t48",
                    "'": "CK2\t49",
                    "Ö": "CK2\t51",
                    "Ä": "CK2\t52",
                    "°": "CK2\t53",
                    ";": "CK2\t54",
                    ":": "CK2\t55",
                    "_": "CK2\t56",
                    ">": "CK2\t100",
                    "€": "CK5\t8",
                    "@": "CK5\t20",
                    "²": "CK5\t31",
                    "³": "CK5\t32",
                    "{": "CK5\t36",
                    "[": "CK5\t37",
                    "]": "CK5\t38",
                    "}": "CK5\t39",
                    "\\": "CK5\t45",
                    "~": "CK5\t48",
                    "|": "CK5\t100"
}

checkHostAlive()
socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for character in password:
    # Press key
    key = keyboardActions[character]
    for x in range(retries):
        socket.sendto(bytes(key, "utf-8"), (hostIp, hostPort))
        time.sleep(retryDelay)
    time.sleep(delay)

    # Key up action
    for x in range(retries):
        socket.sendto(bytes(keyUpAction, "utf-8"), (hostIp, hostPort))
        time.sleep(retryDelay)
    time.sleep(delay)
