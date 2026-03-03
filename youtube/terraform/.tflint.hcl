config {
  call_module_type = "local"
  force            = false
}

plugin "google" {
  enabled    = true
  version    = "0.26.0" # Tente esta versão, que é mais recente
  source     = "github.com/terraform-linters/tflint-ruleset-google"
}