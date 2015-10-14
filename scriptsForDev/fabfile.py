from __future__ import with_statement
from fabric.api import env, local, run, lcd, cd, sudo
import os

env.hosts = ['pi@192.168.81.1:22']

dependenceDir = '../../'

dojoGit = 'https://github.com/dojo/'
cssSandPaperGit = 'https://github.com/zoltan-dulac/'
emacsConfigGit = 'https://github.com/purcell/'

dojoSubDirs = [ 'dojo','dojox','dijit','util','docs','demos' ]
cssSandPaperDir = 'cssSandPaper'
emacsConfigDir = 'emacs.d'

gitAlias = [ 'user.name  brgd', 'user.email hohhots@gmail.com', 'push.default matching',
             'branch.autosetuprebase always', 'core.editor \'emacs -fs\'', 'color.ui true',
             'color.status auto', 'color.branch auto', 'alias.co checkout',
             'alias.ci commit', 'alias.st status', 'alias.xfetch \'fetch origin\'',
             'alias.xdiff \'diff origin master\'', 'alias.xmerge \'merge origin master\'',
             'alias.xpull \'pull origin master\'', 'alias.xpush \'push origin master\'',
             'alias.br branch', 'alias.type \'cat-file -t\'', 'alias.dump \'cat-file -p\'',
             'alias.hist \'log --pretty=format:%h-%ad-|-%s%d-[%an] --graph --date=short\'' ]



def localPull(sdir, ddir):
    a = dependenceDir + ddir
    if not os.path.exists(a):
        local('git clone ' + sdir + ddir + '.git ' + a)
    else:
        with lcd(a):
            print bcolors.OKGREEN + "Directory - " + a + bcolors.ENDC
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

def localGitConfig():
    for alias in gitAlias:
        local('git config --global ' + alias)

def localEmacsConfig():
    localEmacsConfigPull()
    hd = os.path.expanduser("~") + '/.' + emacsConfigDir
    if os.path.exists(hd):
        if os.path.exists(hd + '/.git'):
            with lcd(hd):
                print bcolors.OKGREEN + "Directory - " + hd + bcolors.ENDC
                local('git pull') #update .emacs.d content
        else:
            print bcolors.FAIL + "WARNING : Directory .emacs.d already exist in home directory!\nPlease remove it first!" + bcolors.ENDC
    else:
        local('cp -r ' + dependenceDir + emacsConfigDir + ' ' + hd) #copy .emacs.d to user direcroty

def setup():
    #prepare some third party code source from github
    localDojoPull()
    localCssSandPaperPull()
    localMijitPull()

    #setup some tools configurations
    localGitConfig()
    localEmacsConfig()

def localPush():
    local('git push') # runs the command on the local environment

def piPull():
    with cd('/home/pi/myProject/mijit'):
        run('git pull') # runs the command on the remote environment
        sudo('scriptsForDev/initPackages.sh')
        run('cd scriptsForDev; fab setup')

def done():
    #push to github from local
    localPush()

    #pull from github in pi
    piPull()

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
