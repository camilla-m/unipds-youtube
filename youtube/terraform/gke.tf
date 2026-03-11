module "gke" {
  source                     = "terraform-google-modules/kubernetes-engine/google"
  version                    = "~> 30.0"
  project_id                 = var.project_id
  name                       = "${var.project_name}-cluster"
  region                     = var.region
  network                    = module.vpc.network_name
  subnetwork                 = module.vpc.subnets_names[0]
  ip_range_pods              = ""
  ip_range_services          = ""
  regional                   = true # Habilita Multi-AZ
  create_service_account     = true
  horizontal_pod_autoscaling = true

  node_pools = [
    {
      name         = "default-node-pool"
      machine_type = "e2-medium"
      min_count    = 1
      max_count    = 3
      disk_size_gb = 50
    },
  ]
}