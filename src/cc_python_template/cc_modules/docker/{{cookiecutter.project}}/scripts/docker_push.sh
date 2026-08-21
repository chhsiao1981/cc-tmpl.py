#!/bin/bash

branch=`git rev-parse --abbrev-ref HEAD`
if [ "${branch}" == "HEAD" ]; then branch=`git describe --tags`; fi

project=`basename \`pwd\``

echo -e "\033[1;32m[INFO]\033[m to tag {{cookiecutter.full_name}}/${project}:${branch}"
docker tag ${project}:${branch} {{cookiecutter.full_name}}/${project}:${branch}
echo -e "\033[1;32m[INFO]\033[m to push {{cookiecutter.full_name}}/${project}:${branch}"
docker push {{cookiecutter.full_name}}/${project}:${branch}

echo -e "\033[1;32m[INFO]\033[m to tag {{cookiecutter.full_name}}/${project}:latest"
docker tag ${project}:${branch} {{cookiecutter.full_name}}/${project}:latest
echo -e "\033[1;32m[INFO]\033[m to push {{cookiecutter.full_name}}/${project}:latest"
docker push {{cookiecutter.full_name}}/${project}:latest
