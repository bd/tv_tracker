# tv_tracker
experiments in web scraping. collection of tv episodes and other media on websites like Hulu

## Development
In order to follow along, you must meet these pre-requisites, setup for which is out of scope for this project.
 - a working `docker` daemon locally, i.e. on your development (host) machine.
 - `docker-compose` works from command line 

```bash
alias dc='docker-compose'
cd tv_tracker
# build the collector
dc build collector

# get a shell on the container
dc run --rm --entrypoint=bash collector
```