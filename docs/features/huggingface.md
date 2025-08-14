# Docker container for Huggingface Spaces

If `dockerfile` is set to `"huggingface"`, a `Dockerfile` intended to run on
[Huggingface Spaces](https://huggingface.co/docs/hub/spaces) is added to the
repository. The Dockerfile installs uv, sets up the environment for
huggingface spaces, and runs a simple Python webserver showing `index.html`
when executed.

The `Dockerfile` makes sure that the packages required for Docker-based
Spaces are installed as described in the
[Spaces Dev Mode Documentation](https://huggingface.co/docs/hub/spaces-dev-mode).

See [Spaces Documentation](https://huggingface.co/docs/hub/spaces-overview)
for more information.
