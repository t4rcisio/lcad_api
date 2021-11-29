import sys
import os
from threading import Thread

nodeList = [
    ["compute-3-1","lsi"],
    ["compute-3-2","lsi"],
    ["compute-3-3","lsi"],
    ["compute-3-4","lsi"],
    ["compute-3-5","lsi"],
    ["compute-3-6","lsi"],
    ["compute-3-7","lsi"],
    ["compute-3-8","lsi"],
    ["compute-1-0","large"],
    ["compute-1-1","large"],
    ["compute-1-2","large"],
    ["compute-1-3","large"],
    ["compute-2-0","sorai"],
    ["compute-2-1","sorai"],
    ["compute-2-2","sorai"]
    ]

JobConf = {
    'COMMAND'  : None,
    'N_CPUS'   : 1,    # Default
    'DISK_MEM' : None,
    'JOB_NAME' : None,
    'THREAD'   : 1,
    'STATE'    : None, # Auto fill
    'OWNER'    : None, # Auto fill
    'FILE_NAME': None,
    'JOB_ID'   : None  # Auto generate
}

def errorCommnadLine():
    print("creteJob filename")
    exit(1)

def errorSbatchFile(line):
    print("Invalid Parameter: ", line)
    exit(1)

def errorInputCommandLine():
    print("Input error : [",sys.argv[1],"] not foud")
    exit(1)


def createJob():
    print("Running :",JobConf["COMMAND"])
    os.system(JobConf["COMMAND"] + ">> out.txt")


def batchFile(file):
    for line in file:
        s_line = line.split('=')
        if s_line[0] in JobConf:
            value = s_line[1].replace('\n','')
            JobConf[s_line[0]] = value
        else:
            errorSbatchFile(line)
    process = Thread(target = createJob)
    process.start()


def readFile():
    try:
        file = open(sys.argv[1], 'r')
    except:
        errorInputCommandLine()
        
    batchFile(file)


############# Start here ###################
if(len(sys.argv) != 2):
    errorCommnadLine()
else:
    readFile()
