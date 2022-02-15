import git

print("Test 1 2 3 ")

remoteurl = "https://github.com/ok-marcos/galpaodamarinha.git"
localfolder = "temp/galpaodamarinha"

myrepo = git.Repo.clone_from(remoteurl, localfolder)
myrepo.git.checkout("master")
