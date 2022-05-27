FROM python:3.9-slim

LABEL "com.github.actions.name"="Snazzy-Linter"
LABEL "com.github.actions.description"="Automatic code reviewer for GitHub PRs."
LABEL "com.github.actions.icon"="code"
LABEL "com.github.actions.color"="gray-dark"

LABEL "repository"="https://github.com/rbob86/lookml-linter/tree/main/linter/rules"
LABEL "homepage"="https://github.com/rbob86/lookml-linter"
LABEL "maintainer"="Eric"

# RUN python -m pip install --upgrade pip
# RUN pip install looker-sdk
# RUN pip install pyyaml
# RUN pip install jsonschema 
# RUN pip install pytest
# RUN pip install lkml
