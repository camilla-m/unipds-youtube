variable "project_id" {
  description = "O ID do seu projeto no GCP"
  type        = string
}

variable "region" {
  description = "Região onde os recursos serão criados"
  type        = string
  default     = "southamerica-east1" # São Paulo
}

variable "project_name" {
  description = "Nome base para os recursos"
  type        = string
  default     = "meu-app-gcp"
}