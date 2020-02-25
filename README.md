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
dc build

# get a shell on the container
dc run --rm --entrypoint=bash collect
```

### Spiders -- Don't Freak Out.
The name of the game is spiders. Currently, we're implementing these with [scrapy](https://docs.scrapy.org/). 

##### A workflow: 
```bash
# these commands are taking place on the container 

scrap
```