# c4h-spack-packages

Spack package repository (namespace `code4hep`) for Code4hep and the packages it
needs beyond Spack's builtin repository. Add it to a Spack installation with

```bash
spack repo add spack_repo/code4hep
```

The container images and the binary cache that use these packages are built in
[c4h-dist](https://github.com/code4hep/c4h-dist).

## Triggering c4h-dist

Every push to `main` runs `.github/workflows/trigger-c4h-dist.yaml`, which
dispatches the full-image workflow (`full.yaml`) in c4h-dist with the pushed
commit as its `packages_ref` input.
