from __future__ import with_statement
from fabric.api import env, local, run, lcd
import os

env.hosts = ['pi@192.168.81.1:22']

dojoGit = 'https://github.com/dojo/'
cssSandPaperGit = 'https://github.com/zoltan-dulac/'
emacsConfigGit = 'https://github.com/purcell/'

dojoSubDirs = [ 'dojo','dojox','dijit','util','docs','demos' ]
cssSandPaperDir = 'cssSandPaper'
emacsConfigDir = 'emacs.d'

def git():
    local('git push') # runs the command on the local environment
    run('cd /home/pi/myProject/mijit; git pull') # runs the command on the remote environment

def pullDojo():
    print 'ok'


def localPull(sdir, ddir):
    a = '../../' + ddir
    if not os.path.exists(a):
        local('git clone ' + sdir + ddir + '.git ' + a)
    else:
        with lcd(a):
            print 'Pull ' + ddir
            local('git pull --all')

def localDojoPull():
    for dir in dojoSubDirs:
        localPull(dojoGit, dir)

def localCssSandPaperPull():
    localPull(cssSandPaperGit, cssSandPaperDir)

def  localEmacsConfigPull():
    localPull(emacsConfigGit, emacsConfigDir)

def localMijitPull():
    local('git pull --all')

def setup():
    #prepare some third party code source from github
    localDojoPull()
    localCssSandPaperPull()
    localEmacsConfigPull()
    localMijitPull()

    #setup some tools configurations
    localGitConfig()
    localEmacsConfig()

def done():
    #push to github from local
    localPush()

    #pull from github in pi
    remotePull()
