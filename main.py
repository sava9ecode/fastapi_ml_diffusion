import io

from fastapi import FastAPI
# from fastapi.responses import FileResponse
from fastapi.responses import StreamingResponse
# from pydantic import BaseModel

from ml import obtain_image

app = FastAPI(title="ML_Web_App")


# @app.get("/")
# def read_root():
#     return {"Hello": "World"}


# @app.get("/item/{item_id}")
# def read_item(item_id: int):
#     return {"item_id": item_id}


# class Item(BaseModel):
#     name: str
#     price: float
#     tags: list[str] = []


# @app.post("/items/")
# def create_item(item: Item):
#     return item


@app.get("/generate")
def generate_image(
    prompt: str,
    *,
    seed: int | None = None,
    num_inference_steps: int = 50,
    guidance_scale: float = 7.5
):
    image = obtain_image(
        prompt,
        num_inference_steps=num_inference_steps,
        seed=seed,
        guidance_scale=guidance_scale
    )

    # Inefficient
    # image.save("image.png")
    # return FileResponse("image.png")

    memory_stream = io.BytesIO()
    image.save(memory_stream, format="PNG")
    memory_stream.seek(0)
    return StreamingResponse(memory_stream, media_type="image/png")
