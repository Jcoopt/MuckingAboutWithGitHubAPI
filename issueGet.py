from github import Github
ACCESS_TOKEN=input("Your access token here: ")

g = Github(ACCESS_TOKEN)

repo = g.get_repo("MozillaFestival/mozfest-program-2018")
# Then play with your Github objects:

for issue in repo.get_issues():
    print(issue)
    print(issue.body)
    print()