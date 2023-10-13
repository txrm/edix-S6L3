# Sprint 6, LAB 3

## Steps:





## TODO:
- [X] Local network hostname solving
- [X] Both app1 and app2 accesible from the outside.
- [X] Optimize imports
- [x] Reduce image filesize
- [X] Healthcheck endpoints
- [ ] ***(NON-FIXED VALUE)*** Minimum 5 instances per app 
- *I attempted limiting the worker connections to 1, and then do a hot .conf reload container after spawning 5 instances, this new .conf containing 1000 connections instead, to no avail. So I will have to use "replicas: 5" even if it implies a hard cap and the application isn't actually scalable. Looking forward to the Kubernetes module.*
- [ ] Some sort of front-end
- [ ] TLS compatibility