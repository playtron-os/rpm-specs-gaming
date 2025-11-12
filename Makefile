CONTAINER_CMD ?= podman
IMAGE_NAME ?= rpm-builder
IMAGE_TAG ?= latest
FEDORA_VERSION ?= 41
UID ?= $(shell id -u)
GID ?= $(shell id -g)

SOURCES_DIR := $(HOME)/rpmbuild/SOURCES
ARCH ?= $(shell uname -m)

##@ General

# The help target prints out all targets with their descriptions organized
# beneath their categories. The categories are represented by '##@' and the
# target descriptions by '##'. The awk commands is responsible for reading the
# entire set of makefiles included in this invocation, looking for lines of the
# file as xyz: ## something, and then pretty-format the target and help. Then,
# if there's a line with ##@ something, that gets pretty-printed as a category.
# More info on the usage of ANSI control characters for terminal formatting:
# https://en.wikipedia.org/wiki/ANSI_escape_code#SGR_parameters
# More info on the awk command:
# http://linuxcommand.org/lc3_adv_awk.php

.PHONY: help
help: ## Display this help.
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n"} /^[a-zA-Z_0-9-]+:.*?##/ { printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)


.PHONY: clean
clean: ## Clean all built RPMs
	rm -rf dist


##@ Packages

.PHONY: gamescope-plus
gamescope-plus: ## Build gamescope-plus RPM
	$(MAKE) build TARGET_DIR=gamescope-plus


.PHONY: gamescope-session
gamescope-session: ## Build gamescope-session RPM
	$(MAKE) build TARGET_DIR=gamescope-session


.PHONY: gamescope-session-playtron
gamescope-session-playtron: ## Build gamescope-session-playtron RPM
	$(MAKE) build TARGET_DIR=gamescope-session-playtron


.PHONY: kernel
kernel: ## Build kernel RPMs
	$(MAKE) build TARGET_DIR=kernel


.PHONY: legendary
legendary: ## Build legendary RPM
	$(MAKE) build TARGET_DIR=legendary


.PHONY: mangohud
mangohud: ## Build mangohud RPM
	$(MAKE) build TARGET_DIR=mangohud


.PHONY: mesa
mesa: ## Build mesa RPM
	$(MAKE) build TARGET_DIR=mesa


.PHONY: playtron-os-files
playtron-os-files: ## Build playtron-os-files RPM
	$(MAKE) build TARGET_DIR=playtron-os-files ARCH=noarch


.PHONY: python3-edl
python3-edl: ## Build python3-edl RPM
	$(MAKE) build TARGET_DIR=python3-edl


.PHONY: reaper
reaper: ## Build reaper RPM
	$(MAKE) build TARGET_DIR=reaper


.PHONY: tzupdate
tzupdate: ## Build tzupdate RPM
	$(MAKE) build TARGET_DIR=tzupdate


.PHONY: udev-media-automount
udev-media-automount: ## Build udev-media-automount RPM
	$(MAKE) build TARGET_DIR=udev-media-automount


.PHONY: valve-firmware
valve-firmware: ## Build valve-firmware RPM
	$(MAKE) build TARGET_DIR=valve-firmware


.PHONY: build
build: $(SOURCES_DIR) check-target-set
	@echo "Copying internal source files"
	cp ./$(TARGET_DIR)/* ~/rpmbuild/SOURCES/
	@echo "Downloading external source files"
	spectool -g -R ./$(TARGET_DIR)/*.spec
	@echo "Building the source RPM"
	rpmbuild -bs ./$(TARGET_DIR)/*.spec
	@echo "Installing the required build dependencies."
	sudo dnf builddep -y ./$(TARGET_DIR)/*.spec
	@echo "Building the binary RPM"
	rpmbuild -bb ./$(TARGET_DIR)/*.spec
	mkdir -p ./dist
	PKG_NAME=$$(grep '^Name:' ./$(TARGET_DIR)/*.spec | cut -d' ' -f2) \
		cp -r ~/rpmbuild/RPMS/$(ARCH)/$${PKG_NAME}*.rpm ./dist
	chown -R $(UID):$(GID) ./dist
	chmod 777 dist
	chmod 666 dist/*.rpm


.PHONY: check-target-set
check-target-set:
ifndef TARGET_DIR
	$(error TARGET_DIR is not set)
endif


$(SOURCES_DIR):
	mkdir -p ~/rpmbuild/SOURCES/


##@ Development

.PHONY: in-container
in-container: ## Run make commands in a container (e.g. make in-container TARGET=kernel)
	$(CONTAINER_CMD) build \
		--build-arg FEDORA_VERSION=$(FEDORA_VERSION) \
		-f Containerfile \
		-t $(IMAGE_NAME):$(IMAGE_TAG) .
	$(CONTAINER_CMD) run --rm \
		-v "$(PWD):/src" \
		-e UID=$(UID) \
		-e GID=$(GID) \
		-w /src \
		$(IMAGE_NAME):$(IMAGE_TAG) \
		make $(TARGET)
