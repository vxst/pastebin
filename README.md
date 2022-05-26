# Pastebin
> Yet another pastebin

[![Build Status](https://j.vx.st/job/pastebin/badge/icon)](https://j.vx.st/job/pastebin/)

A demo of SemVer and Jenkins CI/CD

The CI/CD pipeline is at the jenkins https://j.vx.st/job/pastebin/

## CI:

 * Run all test
 * Generate coverage report
 * Publish coverage report


## CD:
If the CI pipeline completed seccessfully
 * Deliver the docker image to dockerhub
 * Restart the deployment in kubernetes to use the lastest docker image
