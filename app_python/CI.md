# CI best practices

## Github actions
1. Use cache to increase the speed and performance of the ci
2. Use `secrets` in github to store the environment variables, that being used, but need to be private
3. Limit actions of the ci to the push to the master
4. Connect two jobs by `needs [other job]` for testing before building

## Jenkins
1. Use docker in docker installation to make it work
2. Use github webhook for automated ci