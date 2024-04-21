from xml.etree import ElementTree as ET

def txt_to_html(txt_file, html_file):
    # Create root element for HTML
    root = ET.Element("html")

    # Create head and body elements
    head = ET.SubElement(root, "head")
    title = ET.SubElement(head, "title")
    title.text = "CBS News Aggregation Site"
    body = ET.SubElement(root, "body")

    # Read text file content
    with open(txt_file, 'r') as f:
        articles = f.read().split('\n\n')  # Assuming each article is separated by two newlines

    # Loop through articles and create HTML elements
    for article in articles:
        lines = article.strip().split('\n')
        if len(lines) >= 2:
            header = lines[0].strip()
            paragraph = "\n".join(lines[1:]).strip()

            # Create header and paragraph elements in body
            h1 = ET.SubElement(body, "h1")
            h1.text = header
            p = ET.SubElement(body, "p")
            p.text = paragraph

    # Write HTML tree to file
    with open(html_file, 'wb') as f:
        tree = ET.ElementTree(root)
        tree.write(f, encoding='utf-8')

txt_file = "CS325_p2/webpage_creation/articles.txt"
html_file = "CS325_p2/webpage_creation/web.html"
txt_to_html(txt_file, html_file)