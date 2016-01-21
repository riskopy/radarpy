import platform 
import os
import sys
import requests
import re
from subprocess import Popen, PIPE
from lxml import etree
from StringIO import StringIO
import json


sysPlatform = platform.platform()
sysUname = platform.uname()

sysProfile = {}

try: 
    sysMac = platform.mac_ver()
    sysProfile['platformVersion'] = str(sysMac[0])
except:
    pass

sysProfile['hostName'] = sysUname[1]
sysProfile['releaseVersion'] = sysUname[2]
sysProfile['machine'] = sysUname[4]
sysProfile['processor'] = sysUname[5]

def applicationCollectMac(): #Developed the OS X function first because I have a Mac! 
    appArray = []
    # Execute system profiler
    appCollect = Popen (["system_profiler", "-detailLevel", "full", "SPApplicationsDataType", "-xml"], stdout = PIPE).communicate()[0]
    # appCollect = open("platform_sample_files/osx_sample_system_profiler_output.xml") # Run sample profiler output as the system_profileer command is a little slow 
    xmlApp = appCollect.read()
    xmlTree = etree.parse(StringIO(xmlApp))
    xmlContext = etree.iterparse(StringIO(xmlApp))
    xmlRoot = xmlTree.getroot()

    for eachItem in xmlRoot: # This cascade isn't pretty and needs cleanup! 
        for eachItem in eachItem:
            for eachItem in eachItem:
                for eachItem in eachItem:
                    if eachItem.tag == "dict":
                        appDict = {}
                        for eachItem in eachItem:
                            if eachItem.tag == "key":
                                tagKey = eachItem.text
                            else:
                                tagText = eachItem.text
                            try:
                                if tagText and tagKey:
                                    appDict[str(tagKey)]= str(tagText)
                            except:
                                pass
                        appArray.append(appDict)
    return appArray

def applicationCollectWindows():
    # Suggestions on how to do this
    #http://www.howtogeek.com/165293/how-to-get-a-list-of-software-installed-on-your-pc-with-a-single-command/
    #https://gallery.technet.microsoft.com/ScriptCenter/154dcae0-57a1-4c6e-8f9f-b215904485b7/
    #http://www.blog.pythonlibrary.org/2010/03/03/finding-installed-software-using-python/
    return appArray

def applicationCollectLinux():
    # Please feel free to contribute to this section
    return appArray

def sendApplicationList(url): # Send data to another service through POST request
    client = requests.session() # Gets a CSRF Token - Needs a conditional statement if no csrftoken is found
    recieved = client.get(url)
    statusCode = recieved.status_code
    if statusCode == 200:
        cookies = dict(client.cookies)
        csrfToken = client.cookies['csrftoken'] 
        headers = {"X-CSRFToken":csrfToken}
        r = requests.post(url, data=(sysProfile), headers=headers, cookies=cookies)
        print r.text
    elif statusCode == 404: # Please feel free to expand on this section
        print "An error has occured" 
    else:
        print "Couldn't reach server"


if sysUname[0] == "Windows":
    print "We've got a Windows machine!"


if sysUname[0] == "Darwin" or sysMac == True:
    print "We've got a Mac machine running OS X "+str(sysMac[0])
    sysProfile['platform'] = "OS X"
    appArray = applicationCollectMac()
    sysProfile['appArray'] = str(appArray)

if sysUname[0] == "Linux":
    print "We've got a Linux machine!"
    sysProfile['platform'] = "Linux"
    sysLinux = platform.linux_distribution(full_distribution_name=1)
    sysProfile['distro'] = sysLinux[0]
    sysProfile['platformVersion'] = sysLinux[1]
    if sysProfile['distro'] == "Ubuntu" or sysProfile['distro'] == "Debian":
        appCollect = Popen (["dpkg", "--list"], stdout = PIPE).communicate()[0]
        # appCollect = open("platform_sample_files/ubuntu_sample_dpkg_list.txt") # Run sample profiler output as the system_profileer command is a little slow 
        print appCollect # Need to include parser


# Optional to use sendApplicationList to a service

