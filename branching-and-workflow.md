# Git Branch Strategy and Workflow

## Git Branching Strategy
This repository is going to have branches for each task with a nomenclature like this `tas-<task-number>-<task-name>`, as in the diagram below, where in which we will have all the branches in the repository as a visual guide through the repository structure:

```
└── main 
    ├── tas-12-data-acquisition
    └── tas-34-analysis-and-preprocessing
```

## Step-by-step Guide

### Repository Cloning or Codespace Creation
1. **Codespace:**
   1. Once in the repo, click on the green `Code` button
   2. Click on Codespace tab
   3. Create or open Codespace
2. **Cloning to Local**
   1. Once in the repo, click on the green `Code` button
   2. Select **HTTPS** and copy the link
   3. Open your terminal, CMD or Powershell
   4. Write the command `git clone` and paste the link you copied
   5. Hit Enter

### Setup the environment
1. Once in your Codespace or Local terminal, type in the following commands in order
   1. `python -m venv .<env-name>`
   2. Activate the env by following the documentation on python venv related to your OS and command line
   3. `pip install -r requirements.txt`
   4. `code .`

### Create or change the git branch
1. Create Branch
   1. In main branch write to the terminal `git branch <branch-name>`
2. Change Branch
   1. In any branch write to the terminal `git checkout <branch-name>`

### Update repository with your changes
1. Run the following commands in order
   1. `git add .`
   2. `git commit -m 'Commit Message'`
   3. `git push origin <branch-name>`

### Notes
* Every time you use the repository after a while, specially the main branch, you have to run the following command `git pull`

## Workflow:

**1. Sprint Planning:**

* At the beginning of each sprint, decide on the features or tasks to be worked on.
* Assign team members to work on specific tasks.

**2. Branching:**
* Each team member creates a feature branch based on the task they're working on.
* Work independently on the assigned tasks within the feature branches.

**3. Continuous Integration:**
* Regularly merge changes from the dev branch into feature branches to ensure integration and avoid conflicts.
* Continuous integration and testing should be performed on the dev branch.

**4. Code Review:**
* Before merging into the dev branch, all code changes should undergo thorough code review by another team member.

**5. Merging:**
* Once a feature is complete and has passed code review and testing, merge it into the dev branch.

**6. Testing:**
* Integration testing should be performed on the dev branch to ensure all features work together seamlessly.

**7. Release:**
* If necessary, create a release branch from the dev branch for final testing and preparation.
* Merge the release branch into the main branch for deployment after thorough testing.

**8. Deployment:**
* Deploy the code from the main branch to the production environment.
* By following this branching strategy, your team can effectively collaborate on the project, manage changes, and ensure a stable and deployable codebase at all times.