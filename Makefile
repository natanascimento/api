SHELL := /bin/bash
CONTAINER_ID := $(shell docker ps -qf "name=api-template")

.PHONY: help setup setup-info setup-down api-logs install
.DEFAULT: help

help:
	@echo "make setup"
	@echo "          Setup project"
	@echo "----------"
	@echo "make setup-info"
	@echo "          View infrastructure status"
	@echo "----------"
	@echo "make setup-down"
	@echo "          Removing the infrastructure"
	@echo "----------"
	@echo "make api-logs"
	@echo "          Read logs on docker container"
	@echo "----------"
	@echo "make install"
	@echo "          Install packages"
	@echo "----------"

build:
	@echo "Building docker image of api"
	@echo "----------"
	docker build -t api/template:latest .

setup: build
	@echo "Setting up the project ..."
	@echo "----------"
	docker compose up -d

setup-info:
	@echo "View infrastructure status"
	@echo "----------"
	docker ps -a | grep -E 'api-template'

setup-down:
	@echo "Removing infrastructure ..."
	@echo "----------"
	docker compose down

api-logs:
	docker logs -f ${CONTAINER_ID}

install:
	pip install pdm && pdm install
