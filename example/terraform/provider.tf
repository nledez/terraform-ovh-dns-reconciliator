provider "ovh" {
  version  = "~> 0.3"
  endpoint = "ovh-eu"
	application_key = var.application_key
	application_secret = var.application_secret
	consumer_key = var.consumer_key
}
