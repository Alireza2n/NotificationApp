build_worker:
	export DOCKER_BUILDKIT=1 && docker build . -f Worker.dockerfile -t notification_worker:latest

build_api:
	export DOCKER_BUILDKIT=1 && docker build . -f API.dockerfile -t notification_api:latest