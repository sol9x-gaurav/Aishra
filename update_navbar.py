import os
import re

def update_navbar(root_dir):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith(".html"):
                filepath = os.path.join(dirpath, filename)
                
                # compute relative path prefix to the root directory
                rel_path = os.path.relpath(root_dir, dirpath)
                if rel_path == '.':
                    prefix = ""
                else:
                    prefix = rel_path.replace("\\", "/") + "/"
                
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()
                
                # regex to find the Products li block
                import re
                # We need to find the <li class="has-dd"> that contains Products
                # It looks like:
                # <li class="has-dd">
                #   <a href="#" class="has-dropdown(...)">Products</a>
                #   <ul class="nav-dropdown"> ...
                #   </ul>
                # </li>
                
                pattern = re.compile(
                    r'<li\s+class="has-dd">\s*<a\s+href="#"\s+class="[^\"]*has-dropdown[^\"]*"\s*>Products</a>\s*<ul\s+class="nav-dropdown">.*?</ul>\s*</li>',
                    re.DOTALL
                )
                
                replacement = f"""<li class="has-dd">
          <a href="#" class="has-dropdown">Products</a>
          <ul class="nav-dropdown">
            <li class="has-dd has-nested-dd">
              <a href="#" class="has-dropdown">PEB Structure &amp; Structural Steel</a>
              <ul class="nav-nested-dropdown">
                <li><a href="{prefix}products/pre-engineered-buildings.html">Pre-Engineered Buildings</a></li>
                <li><a href="{prefix}products/multistory-buildings.html">Multistory Buildings</a></li>
                <li><a href="{prefix}products/steel-structure-fabricator.html">Steel Structure Fabricator</a></li>
                <li><a href="{prefix}products/structural-steel-fabricator.html">Structural Steel Fabricator</a></li>
                <li><a href="{prefix}products/pre-engineered-structural-steel.html">Pre-Engineered Structural Steel</a></li>
              </ul>
            </li>
            <li><a href="{prefix}products/lgsf.html">LGSF</a></li>
            <li><a href="{prefix}products/puf-panel.html">PUF Panel</a></li>
            <li><a href="{prefix}products/purlin-girt.html">Purlin / Girt</a></li>
            <li><a href="{prefix}products/roofing-sheet.html">Roofing Sheet</a></li>
            <li><a href="{prefix}products/space-frame.html">Space Frame</a></li>
            <li><a href="{prefix}products/tensile-fabric.html">Tensile Fabric</a></li>
            <li><a href="{prefix}products/air-ventilation.html">Air Ventilation</a></li>
          </ul>
        </li>"""
                
                new_content, count = pattern.subn(replacement, content)
                
                if count > 0:
                    with open(filepath, "w", encoding="utf-8") as f:
                        f.write(new_content)
                    print(f"Updated {filepath}")

if __name__ == "__main__":
    update_navbar(r"c:/Users/gaura/Downloads/Aishra-updated (1)/aishra_updated")
