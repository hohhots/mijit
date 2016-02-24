from __future__ import with_statement
from fabric.api import env, local, run, lcd, cd, sudo
import os
from fabric.contrib.files import sed

env.hosts = ['pi@192.168.3.254:22']

dependenceDir = '../../'
mijitTestsDir = 'tests'

dojoGit = 'https://github.com/dojo/'
cssSandPaperGit = 'https://github.com/zoltan-dulac/'
emacsConfigGit = 'https://github.com/purcell/'

dojoSubDirs = [ 'dojo','dojox','dijit','util','docs','demos' ]
cssSandPaperDir = 'cssSandPaper'
gitIgnoreGlobal = 'gitignoreGlobal'
emacsConfigDir = 'emacs.d'

livejs = 'live.js'

gitAlias = [ 'user.name  brgd', 'user.email hohhots@gmail.com', 'push.default matching',
             'branch.autosetuprebase always', 'core.editor \'emacs -fs\'', 'color.ui true',
             'color.status auto', 'color.branch auto', 'alias.co checkout',
             'alias.ci commit', 'alias.st status', 'alias.xfetch \'fetch origin\'',
             'alias.xdiff \'diff origin master\'', 'alias.xmerge \'merge origin master\'',
             'alias.xpull \'pull origin master\'', 'alias.xpush \'push origin master\'',
             'alias.br branch', 'alias.type \'cat-file -t\'', 'alias.dump \'cat-file -p\'',
             'alias.hist \'log --pretty=format:%h-%ad-|-%s%d-[%an] --graph --date=short\'',
             'core.excludesfile \'~/.' + gitIgnoreGlobal + '\'' ]



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
    hd = os.path.expanduser("~") + '/.' + gitIgnoreGlobal
    if os.path.exists(hd):
    	print bcolors.FAIL + "WARNING : File ." + gitIgnoreGlobal + " already exist in home directory!\nPlease remove it first!" + bcolors.ENDC
    else:
        local('cp -r ' + gitIgnoreGlobal + ' ' + hd) #copy gitignoreGlobal to user direcroty

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

def startHttpServer():
    with lcd(dependenceDir):
        local('python3 -m http.server &')

def pull():
    #prepare some third party code source from github
    localDojoPull()
    localCssSandPaperPull()
    localMijitPull()
    
def getLivejs():
    a = dependenceDir + livejs
    if os.path.exists(a):
        local('rm ' + a) 	#delete existing live.js file
    with lcd(dependenceDir):
        local('wget http://livejs.com/' + livejs) #get live.js file
    
    local('cat ' + a + ' > ../' + mijitTestsDir + '/' + livejs)
    
    ls = ' ../'  + mijitTestsDir + '/' + livejs
    re = 'document.location.reload()'
    local('sed -i \'s/' + re + '/window.top.' + re + '/g\''  + ls)
    in1 = 'interval = 1000'
    in2 = 'interval = 3000'
    local('sed -i \'s/' + in1 + '/' + in2 + '/g\''  + ls)

def setup():
    pull()
    
    getLivejs()

    #setup some tools configurations
    localGitConfig()
    localEmacsConfig()

    #start temp servers for develop
    startHttpServer()

def localPush():
    local('git push') # runs the command on the local environment

def piPull():
    with cd('/home/pi/myProject/mijit'):
        run('git pull') # runs the command on the remote environment
        sudo('scriptsForDev/initPackages.sh')
        run('cd scriptsForDev; fab pull')

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
