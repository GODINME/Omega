# Omega
Omega - Advanced Data Structures and Algorithms
* The inspiration behind this project is to improve our programming skills and also help others new to programming to pick up while studing this course in team sport and collabration fashion because the best way to learn programming is through algorithms.  


# How to Contribute

* Would love to accept your patches and contributions to the Programming aspect of the course.
* To contribute, use fork and branch workflow.

## Fork & Pull Request Workflow

Also know as **Fork-and-Branch** Workflow

Uses three repos:

* _Original repository_ (remote) - An open source repo on GitHub
* _Forked repository_ (remote) - my forked copy of the open source repo on Github
* _Cloned (local) repository_ (from Forked) - my local copy of my forked repo

### Summary

1. Fork a GitHub repository
1. Clone the forked repository to your local system.
1. Add a Git remote for the original repository.
1. Create a feature branch in which to place your changes.
1. Make your changes to the new branch.
1. Commit the changes to the branch.
1. Push the branch to GitHub.
1. Open a pull request from the new branch to the original repo.
1. Clean up after your pull request is merged.

### Steps to complete **Fork-and-Branch**

1. Fork a repo
    * Click the fork icon in the upper right hand corner of your favorite repository.

1. Clone to desktop from forked repo

    ```bash
    # Use favorite desktop client or do from command line
    git clone https://github.com/GODINME/Omega.git
    ```

1. Add **upstream** remote pointing back to the **original** repo

    ```bash
    # By convention this remote is named "upstream"
    git remote add upstream https://github.com/GODINME/Omega.git
    ```

1. Sync cloned fork with upstream repo

    ```bash
    # fetch from upstream remote
    git fetch upstream

    # view all branches including local ones that represent remote ones
    git branch -va

    # checkout main
    git checkout main

    # merge upstream (again, this is merging two local branches)
    git merge upstream/main
    ```

1. Create feature branch

    ```bash
    # new branch should be based off of main
    git checkout main

    # make it a simple, descriptive name & switch to it
    git branch newfeature
    git checkout newfeatue

    # ALTERNATE OPTION
    # combine previous two lines into one command if desired
    git checkout -b "newfeature"
    ```

1. Develop, test, and commit changes to feature branch

    ```bash
    # commit 1
    git commit -m "Add xyz"

    # commit 2
    git commit -m "Update xyz"

    # commit 3
    git commit -m "Expand xyz functionality"
    ```

1. **CLEAN-UP BRANCH BEFORE PULL REQUEST**

    If any commits have been made to the upstream master branch, you should rebase your feature branch so that merging it will be a simple fast-forward that won't require any conflict resolution work.
    1. Fetch upstream master & merge

        ```bash
        # Fetch upstream master and merge with your repo's master branch
        git fetch upstream
        git checkout master
        git merge upstream/main
        ```

    1. Rebase feature branch onto _updated_ main

        ```bash
        # If there were any new commits, rebase your feature branch onto updated master
        git checkout newfeature
        git rebase main
        ```

    1. Now, it may be desirable to squash some of your smaller commits down into a small number of larger more cohesive commits. You can do this with an interactive rebase:

        ```bash
        # Rebase all commits on your feature branch
        git checkout
        git rebase -i main
        ```
        See the **Interactive Rebasing** section of Atlassian's [Merging vs. Rebasing Tutorial](https://www.atlassian.com/git/tutorials/merging-vs-rebasing#conceptual-overview)
        
        See GitHub Help [About Git rebase](https://help.github.com/articles/about-git-rebase/) for a walkthrough on how to use `git rebase -i`

1. Push changes to GitHub

    ```bash
    # Pushes feature branch to GitHub
    git push origin newfeature
    ```

1. Initiate a Pull Request from feature branch
    1. Go to forked repo on GitHub
    1. Select feature branch
    1. Click the Pull Request button
1. **CLEAN-UP REPOS AFTER INTEGRATION**

    Once maintainer accepts and merges changes into original repositry
    1. Update local clone (git pull upstream main) - This brings down the updated main branch that includes your new developoment changes and merges it with local main

        ```bash
        # Checkout main
        git checkout main

        # Fetch upstream main and merge with local repo's main branch
        git fetch upstream
        git merge upstream/main

        # ALTERNATE OPTION
        # Update local clone (pull does a fetch & merge)
        git pull upstream main
        ```
    1. We can now delete the feature branch since changes are already in main branch

        ```bash
        # delete local branch
        git branch -d <branch name>
        ```

    1. Then we can update the main branch in the forked repository

        ```bash
        # push to my fork
        git push origin main
        ```

    1. Lastly, we push the deletion of the feature branch to forked repository

        ```bash
        # delete feature branch from my fork
        git push --delete origin <branch name>
        ```

## Using this Workflow Here

There will be three Git repositories involved:

1.  *upstream* - the Omega repository on GitHub.
2.  *origin* - your GitHub fork of `upstream`. This repository
    will typically be at a URL that looks like `github.com/_your_user_name_/Omega`
3.  *local* - your local clone of `origin`

### First time setup

Follow these steps to get ready for making changes to Omega.  These
steps are only needed once and not for subsequent changes you might want to
make:

1.  Fork the `Omega` repository on GitHub to create `origin`.
    Visit [Omega](https://github.com/GODINME/Omega) GitHub repository and click the `Fork` button.

2.  Make a `local` clone of your fork.

    ```shell
    git clone git@github.com:_your_user_name_/Omega.git
    ```

3.  Add a remote pointing from `local` to `upstream`.

    ```shell
    cd Omega
    git remote add upstream git@github.com:GODINME/Omega.git
    ```
### Making changes

Here is a detailed outline of the steps needed to make changes to Omega.


1. Make a local branch in your clone and pull any recent changes into it.

   ```shell
   git switch -c my_branch  # Pick a name appropriate to your work
   git pull upstream main
   ```

2. Make changes and commit to local branch.

   ```shell
   # ... editing, testing, ... 
   git commit ...
   ```

3. Pull any changes that may have been made in the upstream repository
   main branch.

   ```shell
   git switch my_branch
   git pull --rebase upstream main
   ```

   Note that this command may result in merge conflicts. Fix those if
   needed.

4. Push your branch to the corresponding branch in your fork (the `origin` repository).

   ```shell
   git switch my_branch
   git push origin my_branch
   ```

5. Select the branch you are working on in the drop-down menu of branches on
   https://github.com/_your_user_name_/Omega . Then hit the `Compare and pull
   request` button.

6. Respond to feedback, which may involve making new commits.
   If you made any changes, push them to github again.

   ```shell
   git switch my_branch
   git push origin my_branch
   ```

   Repeat as necessary until all feedback has been handled.

   Note: the preceding approach will cause the pull request to become a sequence
   of commits. Some people like to keep just a single commit that is amended as
   changes are made. If you are amending commits that had already been pushed,
   you will have to add `--force` to the `git push` command above.

7. Once I review, pull any main branch changes that may
   have happened since step 3.
   
    ```shell
    git switch my_branch
    git pull --rebase upstream main
    ```

    If some changes were pulled, push again to the PR, but this time you will
    need to force push since the rebase above will have rewritten your commits.

    ```shell
    git switch my_branch
    git push --force origin my_branch
    ```

8.  Ask somebody who has permissions (or do it yourself if you
    have permissions) to merge your branch into the main branch
    of the `upstream` repository. The reviewer (which is me) may do this without
    being asked.

    Select the `Squash and merge` option on https://github.com/GODINME/Omega
    or use the command line instructions found on that page. Edit the commit message
    as appropriate for the squashed commit.

9.  Delete the branch from `origin`:

    ```
    git push origin --delete my_branch
    ```

10. Delete the branch from `local`

    ```
    git switch main
    git branch -D my_branch
    ```


