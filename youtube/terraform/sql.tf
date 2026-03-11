resource "google_sql_database_instance" "main" {
  name             = "${var.project_name}-db"
  database_version = "POSTGRES_15"
  region           = var.region

  depends_on = [google_service_networking_connection.private_vpc_connection]

  settings {
    tier              = "db-f1-micro"
    availability_type = "REGIONAL" # Alta Disponibilidade (Multi-AZ)

    ip_configuration {
      ipv4_enabled    = false
      private_network = module.vpc.network_id
    }
  }
}