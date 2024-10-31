# Nome dell'immagine e del container
IMAGE_NAME=prova
CONTAINER_NAME=prova
VOLUME_NAME=volumediprova

# Porta del server
PORT=5000

# Target per buildare l'immagine
build:
	@echo "Building Docker image..."
	sudo docker build -t $(IMAGE_NAME) .

# Target per visualizzare le immagini Docker
images:
	@echo "Listing Docker images..."
	sudo docker images

# Target per avviare il container con la porta mappata
run:
	@echo "Running Docker container $(CONTAINER_NAME) with port mapping..."
	sudo docker run -p $(PORT):$(PORT) --name $(CONTAINER_NAME) $(IMAGE_NAME)

# Target per creare un volume Docker
create-volume:
	@echo "Creating Docker volume $(VOLUME_NAME)..."
	sudo docker volume create $(VOLUME_NAME)

# Target per eseguire il container con il volume montato
run-with-volume:
	@echo "Running Docker container $(CONTAINER_NAME) with mounted volume $(VOLUME_NAME)..."
	sudo docker run -p $(PORT):$(PORT) -v $(VOLUME_NAME):/app $(IMAGE_NAME)

# Target per fermare il container
stop:
	@echo "Stopping Docker container $(CONTAINER_NAME)..."
	sudo docker stop $(CONTAINER_NAME)

# Target per rimuovere il container
clean-container:
	@echo "Removing Docker container $(CONTAINER_NAME)..."
	sudo docker rm $(CONTAINER_NAME)

# Target per rimuovere l'immagine Docker
clean-image:
	@echo "Removing Docker image $(IMAGE_NAME)..."
	sudo docker rmi $(IMAGE_NAME)

# Target per rimuovere il volume Docker
clean-volume:
	@echo "Removing Docker volume $(VOLUME_NAME)..."
	sudo docker volume rm $(VOLUME_NAME)

# Target per pulire completamente l'ambiente
clean-all: stop clean-container clean-image clean-volume
	@echo "Cleaned up all Docker resources."

.PHONY: build images run create-volume run-with-volume stop clean-container clean-image clean-volume clean-all
