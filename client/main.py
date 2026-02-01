from git import Repo
import os
from pathlib import Path
import requests

SERVERURL= os.getenv("SERVER_URL")
GITURL = os.getenv("GIT_URL")
path = Path.cwd()
IsServerOn = False
IsGenerating= False
FinishedGenerating= False
Progress = 0


def find_git_repo(path="."):
    try:
        return Repo(path, search_parent_directories=True)
    except:
        return None

def generatePlayload():
    res = {}
    if IsServerOn:
        res.update({"IsServerOn": True})
        return res
    return {"IsServerOn": False}

def getMcStatus():
    '''
    return a dict with IsServerOn, IsGenerating, 
    '''
    pass

def getInstruction():
    playload = generatePlayload()
    r = requests.post(SERVERURL, json=playload)
    r.json()

def main():
    repoExist = find_git_repo()
    print(repoExist)
    if repoExist:
        getInstruction()
    else:
        initializeRepo()


def initializeRepo():
    print(GITURL)
    repo = Repo.clone_from(GITURL, "save")





if __name__ == "__main__":
    main()
