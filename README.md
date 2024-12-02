# casa

### Services
- [Traefik reverse proxy](https://github.com/traefik/traefik)
- [pihole](https://github.com/pi-hole/docker-pi-hole)
- [CNCF Registry](https://hub.docker.com/_/registry)
- [dmm](https://github.com/allfro/device-mapping-manager)
- [Home Assistant](https://github.com/home-assistant/core)
- [ESPHome](https://esphome.io/)
- [Frigate](https://frigate.video/)

### Cluster
- 2x [RPi 5](https://www.raspberrypi.com/products/raspberry-pi-5/)
    - Each with [Coral TPUs](https://coral.ai/products/m2-accelerator-bm)
    - and [pineboard hats](https://pineboards.io/products/hatdrive-poe-for-raspberry-pi-5)
- 6x [RPi 4b](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/)
    - Each with a [POE Hat](https://www.raspberrypi.com/products/poe-hat/)
- 2x [RPi racks](https://www.amazon.com/gp/product/B09D7RR6NY/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)
- 1x [PDU](https://www.amazon.com/gp/product/B0035PS5AE/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)
- 1x 1u UPS
- POE Switch
- [docker swarm](https://docs.docker.com/engine/swarm/)

### NAS
- Not managed here, was built from base armbian image and `armbian-config`
- [rockpro64](https://www.pine64.org/rockpro64/)
- [armbian](https://www.armbian.com/rockpro64/)
- [openmediavault](https://www.openmediavault.org/)
- 2x 1TB SSDs Mirrored

### VPN
- Just using [tailscale](https://tailscale.com/) for now
