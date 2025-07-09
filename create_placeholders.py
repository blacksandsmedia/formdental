import base64

# Create simple SVG placeholder images
def create_svg_placeholder(text, color="#f6f3f2"):
    svg = f'''<svg width="800" height="600" xmlns="http://www.w3.org/2000/svg">
    <rect width="800" height="600" fill="{color}"/>
    <circle cx="400" cy="200" r="80" fill="#2b2b2b" stroke="#d4c8b8" stroke-width="4"/>
    <circle cx="360" cy="180" r="8" fill="#2b2b2b"/>
    <circle cx="440" cy="180" r="8" fill="#2b2b2b"/>
    <path d="M 350 220 Q 400 250 450 220" stroke="#2b2b2b" stroke-width="6" fill="none"/>
    <rect x="370" y="230" width="60" height="12" fill="white" stroke="#2b2b2b"/>
    <text x="400" y="400" text-anchor="middle" font-family="Arial" font-size="32" fill="#2b2b2b">{text}</text>
    <text x="400" y="450" text-anchor="middle" font-family="Arial" font-size="18" fill="#666">Beautiful Natural Smile</text>
</svg>'''
    return svg

# Create placeholder files
placeholders = [
    ("Confident Smile", "#f6f3f2"),
    ("Elegant Smile", "#f0ede8"), 
    ("Natural Smile", "#f6f3f2"),
    ("Perfect Smile", "#f0ede8")
]

for i, (text, color) in enumerate(placeholders, 1):
    svg_content = create_svg_placeholder(text, color)
    with open(f'images/smile-{i}.svg', 'w') as f:
        f.write(svg_content)

print("Created SVG placeholder files")
