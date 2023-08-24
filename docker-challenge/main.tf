terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 2.22.0"
    }
  }
}

provider "docker" {} 

variable "internal_port" {
  description = "Internal port inside the Docker container"
  default     = 9876
}

variable "external_port" {
  description = "Port on the host machine to access the container"
  default     = 5432
}

variable "container_name" {
  description = "Name of the Docker container"
  default     = "AltaResearchWebService"
}

resource "docker_container" "simplegoservice" {
  name  = var.container_name
  image = "registry.gitlab.com/alta3/simplegoservice"

  ports {
    internal = var.internal_port
    external = var.external_port
  }
}

