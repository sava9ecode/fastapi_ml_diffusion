# Stable Diffusion with 🧨 Diffusers

This is a simple ML web app developed with FastAPI to generate images from text.

[Stable Diffusion](https://huggingface.co/blog/stable_diffusion) is a text-to-image latent diffusion model created by the researchers and engineers from CompVis, Stability AI and LAION. It is trained on 512x512 images from a subset of the LAION-5B database. LAION-5B is the largest, freely accessible multi-modal dataset that currently exists.

## Quick Start

Clone the repository.

```bash
git clone <url>
```

Set up and activate a virtual environment.

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies.

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Start a development server.

```bash
uvicorn main:app --reload
```

That's it! Open your browser at http://127.0.0.1:8000 and have fun!
