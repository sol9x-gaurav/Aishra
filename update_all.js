const fs = require('fs');
const path = require('path');

const rootDir = 'c:/Users/gaura/Downloads/Aishra-updated (1)/aishra_updated/';

function processDir(dir) {
  const files = fs.readdirSync(dir);
  for (const file of files) {
    const fullPath = path.join(dir, file);
    if (fs.statSync(fullPath).isDirectory()) {
      if (!fullPath.includes('node_modules') && !fullPath.includes('.git') && !fullPath.includes('css') && !fullPath.includes('js') && !fullPath.includes('images')) {
        processDir(fullPath);
      }
    } else if (file.endsWith('.html')) {
        try {
          let content = fs.readFileSync(fullPath, 'utf8');
          let orig = content;

          // Add dropdown-toggle if missing
          content = content.replace(/class=\"has-dropdown\"/g, 'class="has-dropdown dropdown-toggle"');
          
          // Wrap nav-cta in a wrapper if not wrapped
          if (!content.includes('class="nav-cta-wrapper"')) {
            content = content.replace(/<a[^>]*class=\"nav-cta[^>]*>.*?<\/a>\s*<a[^>]*class=\"nav-cta[^>]*>.*?<\/a>/gs, (match) => {
              return `<div class="nav-cta-wrapper">\n${match}\n      </div>`;
            });
          }

          // #contact to contact.html
          content = content.replace(/href=\"(index\.html)?#contact\"/g, 'href="contact.html"');

          // HDFC Bank references completely removed from DOM
          const hdfcCardRegex = /<!--\s*<div class=\"client-card\">\s*<div class=\"client-logo-wrapper\">\s*<img src=\"images\/HDFC-Bank-logo\.png\" alt=\"HDFC Bank CSR\">\s*<\/div>\s*<div class=\"client-name\">HDFC Bank CSR<\/div>\s*<\/div>\s*-->/gi;
          content = content.replace(hdfcCardRegex, '');
          const hdfcCardRegex2 = /<div class=\"client-card\">\s*<div class=\"client-logo-wrapper\">\s*<img src=\"images\/HDFC-Bank-logo\.png\" alt=\"HDFC Bank CSR\">\s*<\/div>\s*<div class=\"client-name\">HDFC Bank CSR<\/div>\s*<\/div>/gi;
          content = content.replace(hdfcCardRegex2, '');

          // Remove text mentions in project.html
          content = content.replace(/HDFC Bank CSR and /g, '');
          content = content.replace(/HDFC Bank CSR — Sanitation/g, 'Sanitation Unit');
          content = content.replace(/Steel Modular Toilet — HDFC Bank CSR Initiative/g, 'Steel Modular Toilet Initiative');

          // Add loading lazy (very robust regex)
          content = content.replace(/<img(?:\s+[^>]+?)?>/gi, (match) => {
            if (match.toLowerCase().includes('loading=')) return match;
            return match.replace('<img', '<img loading="lazy"');
          });

          // Mobile script resize update
          content = content.replace(/window\.innerWidth\s*<=\s*768/g, 'window.innerWidth <= 992');

          if (content !== orig) {
            fs.writeFileSync(fullPath, content);
            console.log('Fixed', fullPath);
          }
        } catch(e) {
          console.error('Error in file:', fullPath, e);
        }
    }
  }
}

processDir(rootDir);
console.log('DONE.');
