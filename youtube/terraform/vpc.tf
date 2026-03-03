module "vpc" {
  source       = "terraform-google-modules/network/google"
  version      = "~> 9.0"
  project_id   = var.project_id
  network_name = "${var.project_name}-vpc"

  subnets = [
    {
      subnet_name   = "${var.project_name}-gke-subnet"
      subnet_ip     = "10.0.1.0/24"
      subnet_region = var.region
    }
  ]
}

# Configuração para o Cloud SQL ter IP Privado na VPC
resource "google_compute_global_address" "private_ip_address" {
  name          = "google-managed-services-range"
  purpose       = "VPC_PEERING"
  address_type  = "INTERNAL"
  prefix_length = 16
  network       = module.vpc.network_id
}

resource "google_service_networking_connection" "private_vpc_connection" {
  network                 = module.vpc.network_id
  service                 = "servicenetworking.googleapis.com"
  reserved_peering_ranges = [google_compute_global_address.private_ip_address.name]
}