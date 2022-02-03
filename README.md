# News Aggregator

This is a backend API aggregator of [Reddit](https://reddit.com/), 

## Getting Started

The product is built on the stack below:

* Python 3.8
* FastAPI

All are in a dockerized environment so please ensure you have Docker and docker-compose setup and running.

## Installing

Again, to have a smooth setup process, please ensure you have Docker, and Make installed on your machine prior the run the commands below in order

```shell
# clone the project
$ git clone https://github.com/BarnaTB/news-aggregator.git

# open the project directory
$ cd news-aggregator

# add environment variables
$ touch .env
```

Copy the values in the `.env_example` file to the `.env`, carefully following the instructions therein, then follow the instructions that follow here.

```shell
# build the project
$ make build

# run the project
$ make up
```

If you want to add your own API as explained by the .env_example, ensure that the key holding the list of your articles is at the top level of your API's json response.

The project should be ready to run so now you can check out the [documentation here](https://locahost:8000/docs/).

## Running the tests

Run the tests by running `pytest` in your terminal.

## Deployment

The application is running solely on localhost but a frontend is being worked on in addition with CI/CD.

## Acknowledgements

Kudos to the recruitment team at [HeliumDoc](https://heliumdoc.com/) for their unmatched support during the development of this project.
