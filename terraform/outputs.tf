output "kubernetes_cluster_name" {
  value = module.gke.name
}

output "cloud_sql_instance_ip" {
  value = google_sql_database_instance.main.private_ip_address
}

output "get_credentials_command" {
  value = "gcloud container clusters get-credentials ${module.gke.name} --region ${var.region}"
}