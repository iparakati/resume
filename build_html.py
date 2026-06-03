import markdown
import os

def compile_resume():
    # 1. Read your Markdown text file
    print("Reading llms-full.txt...")
    try:
        with open("llms-full.txt", "r", encoding="utf-8") as f:
            md_text = f.read()
    except FileNotFoundError:
        print("Error: llms-full.txt not found. Please ensure it is in the same directory.")
        return

    # 2. Convert the Markdown to raw HTML
    print("Converting Markdown to HTML...")
    # We include standard extensions to ensure lists, bolding, and links parse perfectly
    raw_html = markdown.markdown(md_text, extensions=['extra', 'nl2br'])

    # 3. Define the HTML Wrapper with Tailwind CSS
    # Notice the '?plugins=typography' in the script src
    html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Isaac Parakati - Agentic Node</title>
    
    <!-- Load Tailwind CSS and the Typography Plugin -->
    <script src="https://cdn.tailwindcss.com?plugins=typography"></script>
</head>
<body class="bg-slate-50 py-10 px-4 sm:px-6 lg:px-8">
    
    <!-- Centered container with a white card background and subtle shadow -->
    <div class="max-w-4xl mx-auto bg-white p-8 sm:p-12 shadow-sm border border-slate-200 rounded-xl">
        
        <!-- The 'prose' class automatically styles the raw HTML output by the markdown library -->
        <article class="prose prose-slate lg:prose-lg prose-a:text-blue-600 hover:prose-a:text-blue-500 max-w-none">
            {raw_html}
        </article>
        
    </div>
    
</body>
</html>"""

    # 4. Save the compiled webpage
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_template)
        
    print("Success! index.html has been compiled.")

if __name__ == "__main__":
    compile_resume()