# import fabrics API functions - self-explanatory once you see
from fabric.api import *
def git():
    local('git push') # runs the command on the local environment
    run('cd /home/pi/myProject/mijit; git pull') # runs the command on the remote environment
