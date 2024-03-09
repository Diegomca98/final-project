# Git Branch Strategy and Workflow

## Git Branching Strategy
1. **Master Branch (main):**

* This branch will contain the stable, production-ready code.
* Code from this branch should be deployable at any time.
* Only merge into this branch from feature branches after thorough testing and code review.

2. **Development Branch (dev):**

* This branch serves as the integration branch for ongoing work.
* Team members merge their feature branches into this branch for integration testing.
* Regularly pull changes from the main branch to ensure the dev branch stays up-to-date with the latest stable version.
* All feature branches should branch off from and merge back into dev.

3. **Feature Branches:**

* Each feature or task should have its own dedicated branch.
* Team members work on separate branches for different features or tasks.
* Branch names should be descriptive of the feature or task being worked on (e.g., feature/data-acquisition, feature/model-building).
* Once a feature is complete, it undergoes code review and testing before merging into the dev branch.

4. **Individual Work Branches (Optional):**

* If team members are working on individual tasks within a larger feature, they can create personal branches based on the feature branch.
* These branches are short-lived and should be merged back into the corresponding feature branch once the individual task is completed.

5. **Release Branches (Optional):**

* If necessary, a release branch can be created from the dev branch for final testing and preparation before deployment.
* No new features are added to release branches; they are solely for bug fixes and preparing for deployment.
* Once the release is ready, it can be merged into the main branch for deployment.

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