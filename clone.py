import sys
import os
import git
import pandas as pd

def clone_repos(option, lang, max_repos_per_lang=5):
    repo_list = pd.read_csv(f'./repo-namelists/list_{lang}.csv')

    if (option.lower() == "https"):
        for id, repo_name in repo_list['repo_name'].items():
            if id >= max_repos_per_lang:
                break

            git_url = f'https://github.com/{repo_name}'
            clone_dir = f'./code-repos/{lang}/{id}'
            clone = f'git clone --quiet {git_url} {clone_dir}'

            # if repo has been cloned, do not clone again
            if os.path.exists(clone_dir):
                continue

            # clone the repo
            print(clone_dir, git_url)
            os.system(clone)

    elif (option.lower() == "ssh"):
        for id, repo_name in repo_list['repo_name'].items():
            if id >= max_repos_per_lang:
                break

            git_url = f'git@github.com:{repo_name}.git'
            clone_dir = f'./code-repos/{lang}/{id}'

            # if repo has been cloned, do not clone again
            if os.path.exists(clone_dir):
                continue
            
            # clone the repo
            print(clone_dir, git_url)
            git.Repo.clone_from(git_url, clone_dir, depth=1)    # depth=1

def clone_languages(option, languages = ['html', 'java', 'python', 'c', 'c++', 'ruby', 'php']):
    for lang in languages:
        clone_repos(option, lang)
