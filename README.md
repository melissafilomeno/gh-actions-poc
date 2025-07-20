# Github Actions PoC (reusable workflow)
- defines reusable workflows used by [gh-actions-2-poc](https://github.com/melissafilomeno/gh-actions-2-poc)
- features :
  - accept parameters from calling repository
  - call GitHub API to get contents of a file from [gh-actions-3-poc](https://github.com/melissafilomeno/gh-actions-3-poc)
  - return an output (multi-line string) for another workflow
  - use outputs from another workflow
  - from the output (multi-line string)
    - write to file
    - create a new branch
    - add a commit for the file creation
    - push the branch
    - create a pull request

## Links :
- https://docs.github.com/en/actions/reference/workflow-commands-for-github-actions#multiline-strings
