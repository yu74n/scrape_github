# -*- coding: utf-8 -*-

class Repo():
    def __init__(self):
        pass

    def run(self, decoded):
        repos = []
        for repo in decoded:
            if "owner" in repo:
                owner = repo["owner"]
                if "login" in owner:
                    user = owner["login"]

            if "name" in repo:
                username = repo["name"]
            if "fork" in repo:
                fork = 1 if repo["fork"] == "true" else 0
            if "stargazers_count" in repo:
                stargazers_count = repo["stargazers_count"]
            if "language" in repo:
                language = repo["language"]
            if "created_at" in repo:
                created_at = repo["created_at"]
            if "updated_at" in repo:
                updated_at = repo["updated_at"]
            if "pushed_at" in repo:
                pushed_at = repo["pushed_at"]
            if "description" in repo and repo["description"] != "null":
                description = repo["description"]

            repos.append(dict(username=username, fork=fork, stargazers_count=stargazers_count, language=language, created_at=created_at, updated_at=updated_at, pushed_at=pushed_at, description=description))
        print(repos)
        return repos

