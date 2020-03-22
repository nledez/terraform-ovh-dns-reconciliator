resource "ovh_domain_zone_record" "entries" {
	count     = 2
  provider  = ovh
  zone      = var.my_domain
  subdomain = "entry-${count.index}"
  fieldtype = "A"
  ttl       = "3600"
  target    = "127.0.0.1"
}
