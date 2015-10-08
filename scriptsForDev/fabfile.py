import os
# import fabrics API functions - self-explanatory once you see
from fabric.api import env,local,run,cd

env.hosts = ['pi@192.168.81.1:22']

dojoSubDirs = [ 'dojo','dojox','dijit','util','docs','demos' ]
dojoGitDir = 'dojoGitRepository'


def git():
    local('git push') # runs the command on the local environment
    run('cd /home/pi/myProject/mijit; git pull') # runs the command on the remote environment

def pullDojo():
    print 'ok'

def cloneDojo():
    for dir in dojoSubDirs:
        local('git clone https://github.com/dojo/' + dir + '.git ../../dojoGitDir/' + dir)

def initDojo():
    #clone dojo from github
    if not os.path.exists(os.getcwd()+'/../../'+dojoGitDir):
        cloneDojo()
    pullDojo()

def localDojoPull():
    initDojo()
    local('')

def setup():
    #prepare some third party code source from github
    localDojoPull()
    localCssSandPaperPull()
    localEmacsPull()

    #setup some tools configurations
    localGitSetup()
    localEmacsSetup()

def done():
    #push to github from local
    localPush()

    #pull from github in pi
    remotePull()
