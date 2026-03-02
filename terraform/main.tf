terraform {
  # Opcional: Descomente após criar o bucket manualmente no GCP
  # backend "gcs" {
  #   bucket  = "nome-do-seu-bucket-terraform-state"
  #   prefix  = "terraform/state"
  # }
}

# Habilita as APIs necessárias automaticamente
resource "google_project_service" "apis" {
  for_each = toset([
    "compute.googleapis.com",
    "container.googleapis.com",
    "sqladmin.googleapis.com",
    "servicenetworking.googleapis.com"
  ])
  service = each.key
  disable_on_destroy = false
}