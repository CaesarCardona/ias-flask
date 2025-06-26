terraform {
  required_providers {
    docker = {
      source = "kreuzwerker/docker"
      version = "~> 3.0"
    }
  }
}

provider "docker" {}

resource "docker_image" "flask_file_server" {
  name         = "flask-file-server"
  build {
    context    = "../flask-server"
    dockerfile = "Dockerfile"
  }
}

resource "docker_container" "flask_server" {
  name  = "flask_file_server"
  image = docker_image.flask_file_server.image_id

  ports {
    internal = 5000
    external = 5050
  }

  command = ["python", "app.py"]
}


