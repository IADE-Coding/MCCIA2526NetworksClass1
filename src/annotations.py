from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import sys
from fastapi import FastAPI, UploadFile, File, HTTPException

app = FastAPI()

# Load pre-trained model and processor
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)


def annotate_image(image: Image.Image) -> str:
    inputs = processor(image, return_tensors="pt")
    output = model.generate(**inputs)
    return processor.decode(output[0], skip_special_tokens=True)


# Create an endpoint to upload images and get annotations
@app.post("/annotate")
def annotate_endpoint(file: UploadFile = File(...)):
    try:
        contents = file.file.read()
        with open(file.filename, 'wb') as f:
            f.write(contents)
    except Exception:
        raise HTTPException(status_code=500, detail='Something went wrong')
    finally:
        file.file.close()
    image = Image.open(file.filename).convert("RGB")
    caption = annotate_image(image)
    return {"message": f"Successfully uploaded {file.filename}", "annotation": caption}


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python annotations.py <image_path>")
        sys.exit(1)
    image_path = sys.argv[1]
    image = Image.open(image_path).convert("RGB")
    caption = annotate_image(image)
    print(f"Annotation: {caption}")
