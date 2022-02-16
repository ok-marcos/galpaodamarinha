from git import Repo

PATH_OF_GIT_REPO = "C:\\Users\\marcos.silva\\Desktop\\tdm_testing\\10112022\\git_repo"
COMMIT_MESSAGE = 'teste'


def git_push():
    # try:
    repo = Repo(PATH_OF_GIT_REPO)
    repo.git.add(update=True)
    repo.index.commit(COMMIT_MESSAGE)
    origin = repo.remote("https://github.com/ok-marcos/galpaodamarinha.git")
    origin.push()
    # except:
    #     print('ocorreu um erro')


git_push()
