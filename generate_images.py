#!/usr/bin/env python3
"""
Generate AI images for IntuitAI website using Hugging Face Inference API.
Uses Stable Diffusion XL for high-quality image generation.
"""

import os
import sys
import time
import requests
from io import BytesIO
from PIL import Image

# Hugging Face API configuration
API_URL = "https://router.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
HEADERS = {}

# Check for HF token in environment
HF_TOKEN = os.environ.get("HUGGINGFACE_TOKEN") or os.environ.get("HF_TOKEN")
if HF_TOKEN:
    HEADERS["Authorization"] = f"Bearer {HF_TOKEN}"
    print("✓ Using Hugging Face API token")
else:
    print("ℹ Using public Hugging Face API (no token found)")
    print("  Note: May have rate limits. Set HUGGINGFACE_TOKEN env var for better performance.")

def query_huggingface(prompt, negative_prompt="", retry_count=3):
    """Query Hugging Face API to generate image."""
    payload = {
        "inputs": prompt,
        "parameters": {
            "negative_prompt": negative_prompt,
            "num_inference_steps": 30,
            "guidance_scale": 7.5,
        }
    }

    for attempt in range(retry_count):
        try:
            print(f"  Attempt {attempt + 1}/{retry_count}...", end=" ")
            response = requests.post(API_URL, headers=HEADERS, json=payload, timeout=120)

            if response.status_code == 200:
                print("✓ Success")
                return Image.open(BytesIO(response.content))
            elif response.status_code == 503:
                # Model is loading
                print("Model loading, waiting 20s...")
                time.sleep(20)
                continue
            else:
                print(f"✗ Error {response.status_code}")
                print(f"  Response: {response.text}")
                if attempt < retry_count - 1:
                    print(f"  Retrying in 10s...")
                    time.sleep(10)
        except Exception as e:
            print(f"✗ Exception: {e}")
            if attempt < retry_count - 1:
                print(f"  Retrying in 10s...")
                time.sleep(10)

    return None

def generate_and_save(prompt, filename, size, negative_prompt=""):
    """Generate image and save to file."""
    print(f"\n📸 Generating: {filename}")
    print(f"   Size: {size[0]}x{size[1]}")
    print(f"   Prompt: {prompt[:80]}...")

    # Generate image
    image = query_huggingface(prompt, negative_prompt)

    if image is None:
        print(f"✗ Failed to generate {filename}")
        return False

    # Resize image to target size
    image = image.resize(size, Image.Resampling.LANCZOS)

    # Save as PNG
    output_path = f"images/{filename}"
    image.save(output_path, "PNG", optimize=True)

    file_size = os.path.getsize(output_path) / 1024  # KB
    print(f"✓ Saved: {output_path} ({file_size:.1f} KB)")

    return True

def main():
    """Generate all images for the website."""
    print("=" * 70)
    print("IntuitAI Website - AI Image Generation")
    print("=" * 70)

    # Negative prompts to avoid unwanted elements
    neg_prompt = "text, words, letters, watermark, signature, people, faces, realistic photo, photograph, blurry, low quality, ugly"

    images_to_generate = [
        {
            "prompt": "Abstract geometric background with teal and cyan gradients, flowing curves, minimal polygonal shapes, tech startup aesthetic, clean modern design, white space, soft shadows, professional, digital art, 8k quality",
            "filename": "hero-background.png",
            "size": (1920, 1080),
            "negative": neg_prompt
        },
        {
            "prompt": "Abstract icon of connected nodes and networks in teal gradient, geometric shapes, minimal design, flat vector style, technology concept, digital illustration, clean white background",
            "filename": "icon-democratizing.png",
            "size": (400, 400),
            "negative": neg_prompt
        },
        {
            "prompt": "Abstract geometric icon with gears and lightbulb in cyan and teal colors, modern tech illustration, minimal flat design, innovation concept, vector style, clean white background",
            "filename": "icon-solutions.png",
            "size": (400, 400),
            "negative": neg_prompt
        },
        {
            "prompt": "Abstract icon showing puzzle pieces connecting in teal gradient, geometric shapes, seamless integration concept, minimal design, technology illustration, clean white background",
            "filename": "icon-integration.png",
            "size": (400, 400),
            "negative": neg_prompt
        },
        {
            "prompt": "Abstract illustration of data visualization and AI concepts, teal and cyan color palette, geometric shapes, flowing lines, bar charts, neural networks, modern tech aesthetic, professional digital art, clean background",
            "filename": "research-illustration.png",
            "size": (800, 800),
            "negative": neg_prompt
        },
        {
            "prompt": "Professional abstract avatar placeholder in teal gradient, geometric human silhouette, minimal design, circular format, modern tech aesthetic, simple icon style, clean background",
            "filename": "team/team-placeholder.png",
            "size": (300, 300),
            "negative": neg_prompt
        },
        {
            "prompt": "Abstract geometric avatar icon in cyan and teal, professional style, minimal circular design, simple geometric shapes, modern tech aesthetic, clean background",
            "filename": "testimonials/testimonial-placeholder.png",
            "size": (150, 150),
            "negative": neg_prompt
        },
    ]

    print(f"\n📋 Will generate {len(images_to_generate)} images")
    print(f"⏱  Estimated time: {len(images_to_generate) * 2}-{len(images_to_generate) * 4} minutes\n")
    print("🚀 Starting generation...")

    success_count = 0
    failed = []

    for i, img_config in enumerate(images_to_generate, 1):
        print(f"\n[{i}/{len(images_to_generate)}] {'=' * 60}")

        success = generate_and_save(
            prompt=img_config["prompt"],
            filename=img_config["filename"],
            size=img_config["size"],
            negative_prompt=img_config["negative"]
        )

        if success:
            success_count += 1
        else:
            failed.append(img_config["filename"])

        # Wait between requests to avoid rate limiting
        if i < len(images_to_generate):
            wait_time = 3
            print(f"\n⏳ Waiting {wait_time}s before next generation...")
            time.sleep(wait_time)

    # Summary
    print("\n" + "=" * 70)
    print("GENERATION SUMMARY")
    print("=" * 70)
    print(f"✓ Successfully generated: {success_count}/{len(images_to_generate)}")

    if failed:
        print(f"✗ Failed: {len(failed)}")
        for f in failed:
            print(f"  - {f}")
    else:
        print("🎉 All images generated successfully!")

    print("\n💡 Next steps:")
    print("   1. Review generated images in the 'images/' directory")
    print("   2. Update HTML file to use .png instead of .svg extensions")
    print("   3. Optionally compress images further with tools like TinyPNG")
    print("   4. Commit and push to GitHub Pages")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠ Generation cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n✗ Unexpected error: {e}")
        sys.exit(1)
