const fs = require('fs');
const path = require('path');

const dir = 'c:/Users/gaura/Downloads/Aishra-updated (1)/aishra_updated/';

function processHtmlFiles(directory) {
  const items = fs.readdirSync(directory);
  items.forEach(item => {
    const fullPath = path.join(directory, item);
    if(fullPath.includes('node_modules')) return;
    
    if(fs.statSync(fullPath).isDirectory()) {
      processHtmlFiles(fullPath);
    } else if(fullPath.endsWith('.html')) {
      let content = fs.readFileSync(fullPath, 'utf8');
      let originalContent = content;

      // 1. Remove the client card entirely (including commented out version)
      const clientRegex = /<!--\s*<div class=\"client-card\">\s*<div class=\"client-logo-wrapper\">\s*<img src=\"images\/HDFC-Bank-logo\.png\" alt=\"HDFC Bank CSR\">\s*<\/div>\s*<div class=\"client-name\">HDFC Bank CSR<\/div>\s*<\/div>\s*-->/gi;
      content = content.replace(clientRegex, '');
      
      const clientRegex2 = /<div class=\"client-card\">\s*<div class=\"client-logo-wrapper\">\s*<img src=\"images\/HDFC-Bank-logo\.png\" alt=\"HDFC Bank CSR\">\s*<\/div>\s*<div class=\"client-name\">HDFC Bank CSR<\/div>\s*<\/div>/gi;
      content = content.replace(clientRegex2, '');

      // 2. Fix the sliding nav trigger (768 -> 992)
      content = content.replace(/window\.innerWidth\s*<=\s*768/g, 'window.innerWidth <= 992');
      
      // 3. Add loading="lazy" where missing
      // Check every img tag
      content = content.replace(/<img([^>]*)>/gi, (match, attrs) => {
          if (!attrs.includes('loading=')) {
              return `<img loading="lazy" ${attrs.trim()}>`;
          }
          return match;
      });

      if(content !== originalContent) {
        fs.writeFileSync(fullPath, content);
        console.log('Fixed:', fullPath);
      }
    }
  });
}

processHtmlFiles(dir);
