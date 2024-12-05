# Demo UV Workspaces

Demo of how to us UV workspaces and share code between apps

It was not exactly clear how to use UV workspaces, so I made this small fastapi example that also has a Gradio app inside.

You can follow the individual commits to see how to make it in small steps.

The most important is setting up hatchling and have hatchling correctly build the python package with having the addition folder mymath, so eg. ./packages/mymath/mymath

## Improvements

If you know how to make hatchling build with `["."]`, because I am not a fan of the repeated folder name, then please create a PR
