#!/usr/bin/env python3
"""
Generate AI images using Hugging Face Hub Client.
Alternative approach using gradio_client for better compatibility.
"""

import os
import sys
import time
from PIL import Image, ImageDraw, ImageFont
import colorsys

def create_gradient_image(size, colors, filename):
    """Create a gradient image with geometric patterns."""
    width, height = size
    image = Image.new('RGB', size)
    draw = ImageDraw.Draw(image)

    # Parse hex colors
    color1 = tuple(int(colors[0][i:i+2], 16) for i in (1, 3, 5))
    color2 = tuple(int(colors[1][i:i+2], 16) for i in (1, 3, 5))

    # Create gradient
    for y in range(height):
        ratio = y / height
        r = int(color1[0] * (1 - ratio) + color2[0] * ratio)
        g = int(color1[1] * (1 - ratio) + color2[1] * ratio)
        b = int(color1[2] * (1 - ratio) + color2[2] * ratio)
        draw.line([(0, y), (width, y)], fill=(r, g, b))

    # Add geometric patterns
    pattern_color = tuple(int(colors[2][i:i+2], 16) for i in (1, 3, 5)) if len(colors) > 2 else (255, 255, 255)

    # Draw circles
    for i in range(5):
        x = width * (i + 1) / 6
        y = height * (i % 3 + 1) / 4
        radius = min(width, height) / 20
        draw.ellipse([x-radius, y-radius, x+radius, y+radius],
                    outline=pattern_color + (100,), width=3)

    # Draw connecting lines
    for i in range(4):
        x1 = width * (i + 1) / 5
        y1 = height / 3
        x2 = width * (i + 2) / 5
        y2 = height * 2 / 3
        draw.line([(x1, y1), (x2, y2)], fill=pattern_color + (80,), width=2)

    return image

def create_icon_network(size):
    """Create network/nodes icon."""
    image = Image.new('RGBA', size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(image)

    # Teal colors
    color_main = (0, 188, 212, 255)
    color_light = (77, 208, 225, 200)
    color_pale = (178, 235, 242, 150)

    # Center node
    cx, cy = size[0] // 2, size[1] // 2
    r_main = min(size) // 8
    draw.ellipse([cx-r_main, cy-r_main, cx+r_main, cy+r_main], fill=color_main)

    # Surrounding nodes
    positions = [(0.3, 0.3), (0.7, 0.3), (0.3, 0.7), (0.7, 0.7)]
    r_small = min(size) // 12

    for px, py in positions:
        x, y = int(size[0] * px), int(size[1] * py)
        draw.ellipse([x-r_small, y-r_small, x+r_small, y+r_small], fill=color_light)
        draw.line([(cx, cy), (x, y)], fill=color_pale, width=4)

    # Outer nodes
    outer_positions = [(0.5, 0.15), (0.85, 0.5), (0.5, 0.85), (0.15, 0.5)]
    r_tiny = min(size) // 18

    for px, py in outer_positions:
        x, y = int(size[0] * px), int(size[1] * py)
        draw.ellipse([x-r_tiny, y-r_tiny, x+r_tiny, y+r_tiny], fill=color_pale)

    return image

def create_icon_lightbulb(size):
    """Create lightbulb/solutions icon."""
    image = Image.new('RGBA', size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(image)

    # Cyan colors
    color_main = (77, 208, 225, 255)
    color_dark = (0, 172, 193, 255)
    color_pale = (178, 235, 242, 200)

    # Lightbulb
    cx, cy = size[0] // 2, size[1] // 3
    r = min(size) // 6
    draw.ellipse([cx-r, cy-r, cx+r, cy+r], fill=color_main)

    # Base
    base_y = cy + r
    draw.rectangle([cx-r//2, base_y, cx+r//2, base_y+r//3], fill=color_dark)
    draw.rectangle([cx-r//1.5, base_y+r//3, cx+r//1.5, base_y+r//2], fill=color_dark)

    # Light rays
    ray_length = r * 1.5
    for angle in [0, 45, 90, -45, -90]:
        import math
        rad = math.radians(angle)
        x1, y1 = cx, cy - r
        x2 = cx + math.sin(rad) * ray_length
        y2 = cy - r - math.cos(rad) * ray_length
        draw.line([(x1, y1), (x2, y2)], fill=color_pale, width=6)

    # Gears at bottom
    gear_y = int(size[1] * 0.75)
    for gx in [size[0] // 3, size[0] * 2 // 3]:
        gr = size[0] // 12
        draw.ellipse([gx-gr, gear_y-gr, gx+gr, gear_y+gr], outline=color_main, width=8)
        draw.ellipse([gx-gr//2, gear_y-gr//2, gx+gr//2, gear_y+gr//2], fill=color_main)

    return image

def create_icon_puzzle(size):
    """Create puzzle/integration icon."""
    image = Image.new('RGBA', size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(image)

    # Teal gradient colors
    color_main = (0, 188, 212, 255)
    color_light = (77, 208, 225, 255)
    color_accent = (0, 172, 193, 200)

    # Puzzle pieces (simplified)
    cx, cy = size[0] // 2, size[1] // 2
    piece_size = min(size) // 3

    # Left piece
    left_pts = [
        (cx - piece_size, cy - piece_size//2),
        (cx, cy - piece_size//2),
        (cx, cy + piece_size//2),
        (cx - piece_size, cy + piece_size//2)
    ]
    draw.polygon(left_pts, fill=color_main)

    # Right piece
    right_pts = [
        (cx, cy - piece_size//2),
        (cx + piece_size, cy - piece_size//2),
        (cx + piece_size, cy + piece_size//2),
        (cx, cy + piece_size//2)
    ]
    draw.polygon(right_pts, fill=color_light)

    # Connection indicator
    draw.ellipse([cx-15, cy-15, cx+15, cy+15], fill=color_accent)

    # Decorative squares
    for x, y in [(cx - piece_size//2, cy), (cx + piece_size//2, cy)]:
        draw.rectangle([x-20, y-20, x+20, y+20], outline=color_accent, width=4)

    return image

def create_research_illustration(size):
    """Create research/data visualization illustration."""
    image = Image.new('RGBA', size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(image)

    # Colors
    color1 = (0, 188, 212, 255)
    color2 = (0, 172, 193, 255)
    color3 = (77, 208, 225, 255)
    color_accent = (255, 107, 53, 255)

    # Bar chart
    bar_width = size[0] // 8
    base_y = size[1] * 3 // 4
    heights = [0.4, 0.6, 0.5, 0.7]

    for i, h in enumerate(heights):
        x = size[0] // 6 + i * bar_width * 1.5
        bar_h = int(size[1] * h / 2)
        color = [color1, color2, color3, color1][i]
        draw.rectangle([x, base_y - bar_h, x + bar_width, base_y], fill=color, outline=color)

    # Line graph overlay
    points = [
        (size[0] // 6 + bar_width // 2, base_y - int(size[1] * 0.4 / 2)),
        (size[0] // 6 + bar_width // 2 + bar_width * 1.5, base_y - int(size[1] * 0.6 / 2)),
        (size[0] // 6 + bar_width // 2 + bar_width * 3, base_y - int(size[1] * 0.5 / 2)),
        (size[0] // 6 + bar_width // 2 + bar_width * 4.5, base_y - int(size[1] * 0.7 / 2)),
    ]

    for i in range(len(points) - 1):
        draw.line([points[i], points[i+1]], fill=color_accent, width=6)

    for point in points:
        draw.ellipse([point[0]-10, point[1]-10, point[0]+10, point[1]+10], fill=color_accent)

    # Neural network representation
    nn_x = size[0] * 2 // 3
    nn_y = size[1] // 3

    # Nodes
    node_positions = [
        [(nn_x, nn_y)],
        [(nn_x + 80, nn_y - 40), (nn_x + 80, nn_y + 40)],
        [(nn_x + 160, nn_y - 60), (nn_x + 160, nn_y), (nn_x + 160, nn_y + 60)],
        [(nn_x + 240, nn_y)]
    ]

    # Draw connections
    for layer in range(len(node_positions) - 1):
        for n1 in node_positions[layer]:
            for n2 in node_positions[layer + 1]:
                draw.line([n1, n2], fill=(178, 235, 242, 150), width=3)

    # Draw nodes
    for layer in node_positions:
        for node in layer:
            draw.ellipse([node[0]-12, node[1]-12, node[0]+12, node[1]+12], fill=color1)

    return image

def create_avatar_placeholder(size):
    """Create abstract avatar."""
    image = Image.new('RGBA', size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(image)

    # Teal gradient background circle
    for i in range(size[0] // 2, 0, -5):
        opacity = int(50 * (1 - i / (size[0] // 2)))
        color = (0, 188, 212, opacity)
        draw.ellipse([size[0]//2-i, size[1]//2-i, size[0]//2+i, size[1]//2+i], fill=color)

    # Person silhouette
    cx, cy = size[0] // 2, size[1] // 2

    # Head
    head_r = size[0] // 6
    head_y = cy - size[1] // 8
    draw.ellipse([cx-head_r, head_y-head_r, cx+head_r, head_y+head_r],
                fill=(0, 188, 212, 200))

    # Body
    body_w = head_r * 1.5
    body_h = head_r * 1.8
    body_y = head_y + head_r
    draw.ellipse([cx-body_w, body_y, cx+body_w, body_y+body_h],
                fill=(0, 188, 212, 200))

    # Rings
    draw.ellipse([cx-head_r-5, head_y-head_r-5, cx+head_r+5, head_y+head_r+5],
                outline=(255, 255, 255, 180), width=4)

    return image

def main():
    print("=" * 70)
    print("IntuitAI Website - Programmatic Image Generation")
    print("=" * 70)
    print("\nGenerating high-quality gradient-based images with geometric patterns...")

    images_config = [
        {
            "name": "Hero Background",
            "filename": "images/hero-background.png",
            "generator": lambda: create_gradient_image(
                (1920, 1080),
                ['#00BCD4', '#4DD0E1', '#FFFFFF'],
                "hero-background.png"
            )
        },
        {
            "name": "Icon: Democratizing AI",
            "filename": "images/icon-democratizing.png",
            "generator": lambda: create_icon_network((400, 400))
        },
        {
            "name": "Icon: Real-World Solutions",
            "filename": "images/icon-solutions.png",
            "generator": lambda: create_icon_lightbulb((400, 400))
        },
        {
            "name": "Icon: Intelligent Integration",
            "filename": "images/icon-integration.png",
            "generator": lambda: create_icon_puzzle((400, 400))
        },
        {
            "name": "Research Illustration",
            "filename": "images/research-illustration.png",
            "generator": lambda: create_research_illustration((800, 800))
        },
        {
            "name": "Team Placeholder",
            "filename": "images/team/team-placeholder.png",
            "generator": lambda: create_avatar_placeholder((300, 300))
        },
        {
            "name": "Testimonial Avatar",
            "filename": "images/testimonials/testimonial-placeholder.png",
            "generator": lambda: create_avatar_placeholder((150, 150))
        },
    ]

    print(f"\n📋 Will generate {len(images_config)} images\n")

    for i, config in enumerate(images_config, 1):
        print(f"[{i}/{len(images_config)}] Generating: {config['name']}")

        try:
            image = config['generator']()
            image.save(config['filename'], 'PNG', optimize=True)

            file_size = os.path.getsize(config['filename']) / 1024
            print(f"   ✓ Saved: {config['filename']} ({file_size:.1f} KB)")
        except Exception as e:
            print(f"   ✗ Error: {e}")

    print("\n" + "=" * 70)
    print("✓ Image generation complete!")
    print("=" * 70)
    print("\n💡 Next steps:")
    print("   1. Review generated images")
    print("   2. Update HTML to use .png extensions")
    print("   3. Test the website")
    print("   4. Commit and push to GitHub")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠ Generation cancelled")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n✗ Error: {e}")
        sys.exit(1)
