Issue with buildout update.

After buildout dependencie update and after running command  "./bin/buildout" a infinite loop occurs

```
Upgraded:
  setuptools version 32.0.0;
restarting.
mr.developer: Queued 'rpiscan' for checkout.
mr.developer: Queued 'vadain.backend' for checkout.
mr.developer: Queued 'vadain.webservice.curtainconfig' for checkout.
mr.developer: Queued 'vadain.webservice.rpi' for checkout.
mr.developer: Updated 'rpiscan' with git.
mr.developer: Updated 'vadain.webservice.rpi' with git.
mr.developer: Updated 'vadain.backend' with git.
mr.developer: Updated 'vadain.webservice.curtainconfig' with git.
Upgraded:
  setuptools version 32.0.0;
restarting.
mr.developer: Queued 'rpiscan' for checkout.
mr.developer: Queued 'vadain.backend' for checkout.
mr.developer: Queued 'vadain.webservice.curtainconfig' for checkout.
mr.developer: Queued 'vadain.webservice.rpi' for checkout.
mr.developer: Updated 'vadain.webservice.rpi' with git.
mr.developer: Updated 'rpiscan' with git.
mr.developer: Updated 'vadain.backend' with git.
mr.developer: Updated 'vadain.webservice.curtainconfig' with git.
Upgraded:
  setuptools version 32.0.0;
restarting.

```

Solution: Blank project installation
