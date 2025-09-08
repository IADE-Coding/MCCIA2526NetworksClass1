from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import sys

# Load pre-trained model and processor
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)


def annotate_image(image: Image.Image) -> str:
    inputs = processor(image, return_tensors="pt")
    output = model.generate(**inputs)
    return processor.decode(output[0], skip_special_tokens=True)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python annotations.py <image_path>")
        sys.exit(1)
    image_path = sys.argv[1]
    image = Image.open(image_path).convert("RGB")
    caption = annotate_image(image)
    print(f"Annotation: {caption}")
