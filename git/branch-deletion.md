To delete a Git branch, there are separate commands for your local repository and the remote (origin).

Delete a local branch

If the branch has already been merged:

git branch -d branch-name

If you want to force-delete it even if Git thinks it hasn't been merged:

git branch -D branch-name
Delete the branch from origin
git push origin --delete branch-name

This removes the branch from the remote repository.

Delete both local and remote
git branch -D branch-name
git push origin --delete branch-name

(or use -d instead of -D if appropriate)

See all branches

Local:

git branch

Remote:

git branch -r

Both:

git branch -a
Clean up stale remote-tracking branches

If someone else deleted a branch on GitHub (or you deleted it from another machine), your local repo may still show it under origin/....

Run:

git fetch --prune

or

git remote prune origin

This removes obsolete origin/branch-name references from your local repository.

Important: You cannot delete the branch you're currently on. Switch to another branch first, for example:

git switch main

Then delete the other branch.
