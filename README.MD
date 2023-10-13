# Sprint 6, LAB 3

## Steps:

1. Copied sample .py.
2. Modified Dockerfile to reduce filesize.
3. Modified app1 and app2 in order to get the Container ID as Server ID.
4. Removed unnecessary imports.
5. Created docker-compose.yaml
6. Set up alias assignment in Compose file
7. Set up healthchecks for apps in Compose file
8. Added nginx to Compose file.
9. *Created nginx config so requests from the outside are directed to app1 or app2 as it wasn't made clear enough from the problem PDF **if app2 was the only one meant to be exposed**. Request recognition achieved through a simple header.*
10. Added header to app2 .py.
11. Changed fixed IPs to solvable Hostnames in app.py's.
12. Debugging and release.

## TODO:
- [X] Local network hostname solving
- [X] Both app1 and app2 accesible from the outside.
- [X] Optimize imports
- [x] Reduce image filesize
- [X] Healthcheck for apps
- [ ] ***(NON-FIXED VALUE)*** Minimum 5 instances per app 
- *I attempted limiting the worker connections to 1, and then do a hot .conf reload container after spawning 5 instances, this new .conf containing 1000 connections instead, to no avail. So I will have to use "replicas: 5" even if it implies a hard cap and the application isn't actually scalable. Looking forward to the Kubernetes module.*
- [ ] Some sort of front-end
- [ ] TLS compatibility