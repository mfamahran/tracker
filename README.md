# Web Tracker
A simple web server built using flask.
## Usage
```sh
docker compose up
```
Visit http://localhost:5000/ and try any of the available endpoints:
- /ping
- /img

## Improvements
- Serve the GIF through a CDN
- Deploy to K8S cluster and scale it behind a LB for handling large number of concurrent users making use of Kuberenetes native features
- Add telemetry to monitor the health of the service and setup alerts to be notified
