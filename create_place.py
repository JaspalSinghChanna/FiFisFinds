import os

# --- CONFIG --- #
PLACE_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} – FiFi's Finds</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <header>
    <h1>FiFi's Finds</h1>
    <nav>
      <a href="index.html">Home</a>
      <a href="places.html">Finds</a>
    </nav>
  </header>
  <main>
    <h2>{title}</h2>
    <p><strong>Location:</strong> {location}</p>
    <p><strong>Price Range:</strong> {price}</p>
    <p><strong>Summary:</strong> {summary}</p>
    <section>
      <h3>Review</h3>
      <p>{review}</p>
    </section>
    <a class="back-link" href="places.html">← Back to Finds</a>
  </main>
</body>
</html>"""

CARD_TEMPLATE = """
<a href="{filename}.html" class="card">
  <img src="images/{image}" alt="{title}">
  <div class="card-content">
    <h3>{title}</h3>
    <p>{summary}</p>
  </div>
</a>
"""

# --- SCRIPT --- #
def create_place():
    title = input("Place Name (e.g. Little Fern): ").strip()
    filename = title.lower().replace(" ", "-")
    location = input("Location (e.g. Peckham, London): ").strip()
    price = input("Price Range (e.g. ££): ").strip()
    summary = input("Short Summary: ").strip()
    review = input("Full Review Text: ").strip()
    image = input("Image filename (e.g. little-fern.jpg): ").strip()

    html_content = PLACE_TEMPLATE.format(
        title=title, location=location, price=price, summary=summary, review=review
    )

    with open(f"{filename}.html", "w", encoding="utf-8") as f:
        f.write(html_content)

    card_snippet = CARD_TEMPLATE.format(
        filename=filename, image=image, title=title, summary=summary
    )

    print(f"\n✅ Created {filename}.html")
    print("\n📌 Paste this into your places.html inside <section class=\"finds-grid\">:\n")
    print(card_snippet)

if __name__ == "__main__":
    create_place()
    print("\n🔗 Don't forget to add the image to the images folder!")