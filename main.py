import git

print("Test 1 2 3 ")

remoteurl = "https://github.com/ok-marcos/galpaodamarinha.git"
localfolder = "temp/galpaomarinha"

myrepo = git.push(remoteurl, localfolder)
myrepo.git.checkout("master")
