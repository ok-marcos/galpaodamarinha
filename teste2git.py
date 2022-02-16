from git import Repo

PATH_OF_GIT_REPO = "https://github.com/ok-marcos/galpaodamarinha.git"
COMMIT_MESSAGE = 'teste'


def git_push():
    # try:
    repo = Repo(
        "C://Users//marcos.silva//Desktop//tdm_testing//10112022//git_repo")
    repo.git.add(update=True)
    repo.index.commit('COMMIT_MESSAGE')
    origin = repo.remote(
        name='https://github.com/ok-marcos/galpaodamarinha.git')
    origin.push().raise_if_error()
    # except:
    #     print('ocorreu um erro')


git_push()
