import os

products = {
    "pre-engineered-buildings": {
        "title": "Pre-Engineered Buildings",
        "desc": "Aishra Technofab offers state-of-the-art Pre-Engineered Buildings (PEB) engineered for superior strength and rapid assembly. Our advanced manufacturing techniques produce customized steel structures tailored for optimum weight-to-strength ratios, ensuring a robust envelope. Whether for vast factories or precise commercial spaces, our PEBs guarantee structural integrity, reduced construction timelines, and immense cost-efficiency.",
        "benefits": ["High Strength & Durability", "Cost-Effective Construction", "Fast Installation & Commissioning", "Weather & Earthquake Resistance", "Minimum Maintenance Setup", "Sustainable & Recyclable Materials"],
        "apps": [{"title": "Warehouses", "cat": "Logistics"}, {"title": "Manufacturing Units", "cat": "Industrial"}, {"title": "Aircraft Hangars", "cat": "Aviation"}],
        "images": { "hero": "hero_peb.png", "intro": "intro_peb.png" }
    },
    "multistory-buildings": {
        "title": "Multistory Buildings",
        "desc": "Designed to maximize vertical space optimization, our multi-story steel buildings combine rapid erection with exceptional architectural versatility. These structures handle high-load capacities while offering wide, column-free internal spaces, perfect for modern offices or residential towers. Utilizing integrated beam and column systems, we deliver towering solutions engineered precisely to Indian seismic codes.",
        "benefits": ["Optimal Vertical Space Utilization", "Rapid Multi-Floor Erection", "Versatile Floor Layouts", "High Seismic & Wind Load Bearing", "Lightweight Foundation Requirement", "Aesthetic Modularity"],
        "apps": [{"title": "Commercial Offices", "cat": "Urban"}, {"title": "Shopping Malls", "cat": "Commercial"}, {"title": "Multi-Level Carparks", "cat": "Infrastructure"}],
        "images": { "hero": "ind_hero.png", "intro": "ind_intro.png" }
    },
    "steel-structure-fabricator": {
        "title": "Steel Structure Fabricator",
        "desc": "As a leading Steel Structure Fabricator, Aishra Technofab utilizes advanced CNC drilling and automated welding to deliver flawless components. We fabricate heavy structural members that strictly align with architectural exactitude and structural demands. From massive girders to intricate trusses, our facilities ensure unparalleled fabrication standards for any heavy engineering application.",
        "benefits": ["Precision CNC Manufactured", "Zero-Defect Robotic Welding", "High Load-Bearing Capacity", "Tailor-Made Configurations", "Strict Quality Control Protocol", "Long-Span Possibilities"],
        "apps": [{"title": "Heavy Industry Plants", "cat": "Industrial"}, {"title": "Bridge Girders", "cat": "Infrastructure"}, {"title": "Power Plants", "cat": "Energy"}],
        "images": { "hero": "hero_steel_structure.png", "intro": "intro_steel_structure.png" }
    },
    "structural-steel-fabricator": {
        "title": "Structural Steel Fabricator",
        "desc": "Our structural steel fabrication processes cater to intricate infrastructure demands across India. We specialize in robust framing, built-up members, and bespoke steel connections engineered to endure extreme stresses. Quality is guaranteed with intensive flaw detection and multi-stage testing, yielding structural elements that form the backbone of lasting architectural landmarks.",
        "benefits": ["Enhanced Torsional Rigidity", "Robust Connection Designing", "Durable Surface Coating", "Quick Site Assembly", "Scalable Production", "Economical Lifespan"],
        "apps": [{"title": "Metro Stations", "cat": "Infrastructure"}, {"title": "Stadiums", "cat": "Sports"}, {"title": "Chemical Plants", "cat": "Industrial"}],
        "images": { "hero": "hero_structural.png", "intro": "intro_structural.png" }
    },
    "pre-engineered-structural-steel": {
        "title": "Pre-Engineered Structural Steel",
        "desc": "Elevating the PEB concept, our Pre-Engineered Structural Steel units combine the swiftness of pre-engineering with the rugged profile of conventional steel architecture. We offer versatile primary framework elements fabricated to precise tolerances. This ensures heavy infrastructure projects can be implemented with unmatched speed without sacrificing the architectural grandeur and load capacity of classic structural steel.",
        "benefits": ["Hybrid Structural Integrity", "Factory-Prepared Assemblies", "Massive Structural Clearance", "Easy Handling & Erection", "Maximized Return on Investment", "Resilient to Varied Climates"],
        "apps": [{"title": "Large Shipyards", "cat": "Industrial"}, {"title": "Auditoriums", "cat": "Commercial"}, {"title": "Logistics Parks", "cat": "Transport"}],
        "images": { "hero": "hero_pe_steel.png", "intro": "intro_pe_steel.png" }
    },
    "lgsf": {
        "title": "LGSF (Light Gauge Steel Framing)",
        "desc": "LGSF by Aishra Technofab represents the pinnacle of accelerated, lightweight construction. Using cold-formed steel profiles, this system drastically reduces dead loads while offering immense design flexibility. Excellent for low to mid-rise constructions, our LGSF frameworks integrate seamlessly with various claddings, boasting superior thermal insulation, dimensional stability, and rapid on-site assembly.",
        "benefits": ["Exceptionally Lightweight", "Galvanized Corrosion Resistance", "Easy & Safe Installation", "Zero Shrinkage or Warping", "Excellent Acoustic Performance", "Eco-Friendly Operations"],
        "apps": [{"title": "Residential Housing", "cat": "Urban"}, {"title": "Site Offices", "cat": "Site Setup"}, {"title": "Hospital Extensions", "cat": "Healthcare"}],
        "images": { "hero": "hero_lgsf.png", "intro": "intro_lgsf.png" }
    },
    "puf-panel": {
        "title": "PUF Panel Solutions",
        "desc": "Our Polyurethane Foam (PUF) Panels are engineered for supreme thermal efficiency and temperature control. Designed to sandwich a high-density PUF core between precision-profiled metal sheets, they are the industry standard for controlled environments. These lightweight panels lock seamlessly to provide weather-tight enclosures, drastically cutting down energy expenses in climate-sensitive industrial setups.",
        "benefits": ["Superior Thermal Insulation", "Energy Efficiency Maximized", "Temperature Maintained Accurately", "Acoustic Dampening Capabilities", "Lightweight Cellular Structure", "Waterproof and Leak-Free"],
        "apps": [{"title": "Cold Storages", "cat": "Logistics"}, {"title": "Clean Rooms", "cat": "Pharmaceutical"}, {"title": "Food Processing Units", "cat": "Industrial"}],
        "images": { "hero": "hero_puf.png", "intro": "intro_puf.png" }
    },
    "purlin-girt": {
        "title": "Purlin & Girt Profiles",
        "desc": "High-tensile Z and C section purlins and girts form the critical structural secondary framing for premium heavy-duty roofs and walls. Roll-formed to exact specifications, they deliver outstanding spanning capabilities with reduced weight. These sections are pre-punched allowing swift, bolt-on execution in the field, optimizing the integration of primary frameworks with outer claddings seamlessly.",
        "benefits": ["High Weight-to-Strength Ratio", "Precision Roll-Forming", "Pre-Punched for Easy Bolting", "Lower Freight Costs", "Nesting Capability (Z-Purlin)", "Durable Galvanized Finish"],
        "apps": [{"title": "Roof Skeletal System", "cat": "Structural"}, {"title": "Wall Support Cladding", "cat": "Architectural"}, {"title": "Canopy Extensions", "cat": "Exterior"}],
        "images": { "hero": "hero_purlin.png", "intro": "intro_purlin.png" }
    },
    "roofing-sheet": {
        "title": "Premium Roofing Sheets",
        "desc": "Aishra Technofab produces high-grade industrial roofing sheets tailored to endure extreme environmental stress. Our precision-profiled sheets range from bare galvalume to color-coated profiles that securely interlock to form impermeable barriers against rain and intense heat. Formulated to resist fading and corrosion, they assure long-lasting aesthetic appeal to complete any structural design.",
        "benefits": ["Complete Weather Resistance", "U.V. Protected Coatings", "Leak-Proof Interlocking", "Rapid Square-Meter Coverage", "Variety of Color Options", "Low Expansion/Contraction"],
        "apps": [{"title": "Factory Roofing", "cat": "Industrial"}, {"title": "Farm Buildings", "cat": "Agriculture"}, {"title": "Transit Sheds", "cat": "Logistics"}],
        "images": { "hero": "hero_roofing.png", "intro": "intro_roofing.png" }
    },
    "space-frame": {
        "title": "Space Frame Structures",
        "desc": "Space Frames provide unmatched architectural elegance coupled with astonishing geometric rigidity. Composed of interlocking tubular steel arranged in multi-directional grids, they span vast column-free areas effortlessly. The resultant structure is exceptionally light, visually stunning, and geometrically resilient against asymmetric loads, making them the preferred choice for iconic modern infrastructure.",
        "benefits": ["Huge Column-Free Spans", "Even Stress Distribution", "Intricate Geometric Elegance", "Very High Torsional Strength", "Low Weight Ratio", "Integrated Lighting Modularity"],
        "apps": [{"title": "Airport Terminals", "cat": "Aviation"}, {"title": "Sports Arenas", "cat": "Recreation"}, {"title": "Atrium Canopies", "cat": "Commercial"}],
        "images": { "hero": "hero_spaceframe.png", "intro": "intro_spaceframe.png" }
    },
    "tensile-fabric": {
        "title": "Tensile Fabric Architecture",
        "desc": "Fusing engineering exactitude with fluid architectural expression, our Tensile Fabric structures deliver dramatic shelters utilizing tensioned membranes. Engineered with advanced weather-resistant fabrics and supported by steel masts, they easily bridge wide gaps while maximizing natural light penetration. The result is a dynamically appealing, semi-permanent shading solution unmatched in visual impact.",
        "benefits": ["Dynamic Fluid Architecture", "Excellent Natural Translucency", "UV and UV/IR Refractive", "Easily Relocatable Framework", "Dirt & Dust Repellent", "Rapid Fabrication Setup"],
        "apps": [{"title": "Walkway Canopies", "cat": "Infrastructure"}, {"title": "Amphitheaters", "cat": "Open-Air"}, {"title": "Toll Plazas", "cat": "Highway"}],
        "images": { "hero": "hero_tensile.png", "intro": "intro_tensile.png" }
    },
    "air-ventilation": {
        "title": "Air Ventilation Systems",
        "desc": "Aishra Technofab's industrial Air Ventilation Systems are designed to passively extract stale air, heat, and emissions continuously without operational costs. Driven by wind-powered turbo ventilators or ridge extraction systems, they promote constant air circulation inside massive factory sheds. By ensuring cooler work environments, they reduce energy expenditures and profoundly boost workforce productivity over time.",
        "benefits": ["Zero Running Expenses", "Passive Natural Exhaust", "Maintains Inside Temperature", "Durable Aluminum Construction", "Noise & Maintenance Free", "Prevents Condensation Build-up"],
        "apps": [{"title": "Heavy Manufacturing", "cat": "Industrial"}, {"title": "Chemical Processing", "cat": "Hazardous"}, {"title": "Power Generating Plants", "cat": "Energy"}],
        "images": { "hero": "hero_vent.png", "intro": "intro_vent.png" }
    }
}

template = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} — Aishra Technofab Engineers</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;0,800;1,700&family=Nunito+Sans:wght@300;400;600;700;800&family=DM+Mono:wght@400;500&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
  <link rel="stylesheet" href="../css/custom.css">
</head>
<body>
<div class="page-loader" id="pageLoader"><div class="loader-ring"></div><div class="loader-brand">Aishra Technofab</div></div>
<div class="top-bar">✦ Established August 2018 &nbsp;|&nbsp; <span class="hl">Complete PEB Solutions</span> &nbsp;|&nbsp; <span class="hl">www.aishra.in</span> ✦</div>
<header class="header-info"><div class="container">
  <div class="brand-logo"><a href="../index.html"><img src="../images/logo.png" alt="Aishra"></a></div>
  <div class="header-contact-item"><div class="header-icon-wrap"><i class="fa fa-phone"></i></div><div class="header-contact-text"><span class="label">Call / Enquiry</span><strong>+91 74638 43731</strong><small>+91 92298 93797</small></div></div>
  <div class="header-contact-item"><div class="header-icon-wrap"><i class="fa fa-envelope"></i></div><div class="header-contact-text"><span class="label">Email Us</span><strong>Info@aishra.in</strong><small>projects.aishra@gmail.com</small></div></div>
</div></header>

<nav class="main-nav"><div class="container">
  <ul class="nav-links" id="navLinks">
    <li><a href="../index.html">Home</a></li>
    <li><a href="../about.html">About</a></li>
    <li><a href="../services.html">Services</a></li>
    <li><a href="../project.html">Projects</a></li>
    <li><a href="../manufacturing-facility.html">Manufacturing</a></li>
    <li class="has-dd">
      <a href="#" class="has-dropdown active">Products</a>
      <ul class="nav-dropdown">
        <li class="has-dd has-nested-dd">
          <a href="#" class="has-dropdown">PEB Structure &amp; Structural Steel</a>
          <ul class="nav-nested-dropdown">
            <li><a href="pre-engineered-buildings.html">Pre-Engineered Buildings</a></li>
            <li><a href="multistory-buildings.html">Multistory Buildings</a></li>
            <li><a href="steel-structure-fabricator.html">Steel Structure Fabricator</a></li>
            <li><a href="structural-steel-fabricator.html">Structural Steel Fabricator</a></li>
            <li><a href="pre-engineered-structural-steel.html">Pre-Engineered Structural Steel</a></li>
          </ul>
        </li>
        <li><a href="lgsf.html">LGSF</a></li>
        <li><a href="puf-panel.html">PUF Panel</a></li>
        <li><a href="purlin-girt.html">Purlin / Girt</a></li>
        <li><a href="roofing-sheet.html">Roofing Sheet</a></li>
        <li><a href="space-frame.html">Space Frame</a></li>
        <li><a href="tensile-fabric.html">Tensile Fabric</a></li>
        <li><a href="air-ventilation.html">Air Ventilation</a></li>
      </ul>
    </li>
    <li class="has-dd">
      <a href="#" class="has-dropdown">Our Products</a>
      <ul class="nav-dropdown">
        <li><a href="../our-products/pre-engineered-buildings.html">Pre-Engineered Buildings</a></li>
        <li><a href="../our-products/non-industrial-buildings.html">Non-Industrial Buildings</a></li>
      </ul>
    </li>
    <li class="has-dd">
      <a href="#" class="has-dropdown">Other</a>
      <ul class="nav-dropdown">
        <li><a href="../hr-desk.html">HR Desk</a></li>
        <li><a href="../gallery.html">Gallery</a></li>
      </ul>
    </li>
    <li><a href="../index.html#contact">Contact</a></li>
  </ul>
  <a href="#" class="nav-cta" onclick="openModal();return false;"><i class="fa fa-paper-plane"></i> Request Quote</a>
  <button class="nav-toggle" id="navToggle"><i class="fa fa-bars"></i> Menu</button>
</div></nav>

<!-- PAGE HERO -->
<div class="page-hero" style="background-image:none;">
  <div class="page-hero-bg" style="background-image:url('../images/{hero_img}'); opacity: 0.4;"></div>
  <div class="container"><div class="page-hero-content reveal">
    <div class="breadcrumb-nav"><a href="../index.html">Home</a><span class="sep">›</span><a href="#">Products</a><span class="sep">›</span><span>{title}</span></div>
    <h1 class="page-hero-title" style="max-width:800px;">{title_split_1}<br><span class="accent">{title_split_2}</span></h1>
  </div></div>
</div>

<!-- ABOUT THE PRODUCT -->
<section class="section section-white" style="padding:0;">
  <div class="product-intro-grid">
    <div class="product-intro-img reveal">
      <img src="../images/{intro_img}" alt="{title} Structure">
    </div>
    <div class="product-intro-content reveal reveal-delay-2">
      <div class="sec-label">About the Product</div>
      <h2 class="sec-title">Premium {title} Manufacturing</h2>
      <p style="color:var(--text-mid);line-height:1.8;margin-bottom:14px;">{desc}</p>
      <div style="display:flex;gap:12px;margin-top:28px;flex-wrap:wrap;">
        <a href="../index.html#contact" class="btn-primary"><i class="fa fa-paper-plane"></i> Contact Us</a>
        <a href="#" class="btn-outline-navy" onclick="openModal();return false;"><i class="fa fa-file-invoice"></i> Request a Quote</a>
      </div>
    </div>
  </div>
</section>

<!-- ADVANTAGES -->
<section class="section section-cream">
  <div class="container">
    <div class="text-center mb-40">
      <div class="sec-label" style="justify-content:center;">Key Advantages</div>
      <h2 class="sec-title">Engineered to Perfection</h2>
      <p class="sec-lead" style="margin:0 auto;">Reliability and efficiency engineered directly into every structured component for ultimate performance.</p>
    </div>
    <div class="design-grid reveal">
      {benefits_html}
    </div>
  </div>
</section>

<!-- APPLICATIONS -->
<section class="section section-white">
  <div class="container">
    <div class="text-center mb-40">
      <div class="sec-label" style="justify-content:center;">Applications</div>
      <h2 class="sec-title">Where We Build</h2>
      <p class="sec-lead" style="margin:0 auto;">{title} serves a wide range of massive infrastructural landscapes and premium projects.</p>
    </div>
    <div class="product-app-grid" style="grid-template-columns: repeat(3, 1fr); display: grid; gap: 24px;">
      {apps_html}
    </div>
  </div>
</section>

<div class="cta-band">
  <div class="container" style="position:relative;">
    <h2>Ready to Deploy {title}?</h2>
    <p>Our structural expert team will provide a free consultation and tailored quote for your project requirements.</p>
    <a href="#" class="btn-outline-white" onclick="openModal();return false;"><i class="fa fa-paper-plane"></i> Request a Free Quote</a>
  </div>
</div>

<footer class="footer"><div class="footer-top"><div class="container"><div class="footer-grid">
  <div><img src="../images/logo.png" alt="Aishra" class="footer-brand-logo"><p class="footer-brand-desc">Aishra Technofab Engineers — complete PEB and steel structure solutions across India since 2018.</p><div class="footer-socials"><a href="#" class="footer-social-btn"><i class="fa-brands fa-twitter"></i></a><a href="#" class="footer-social-btn"><i class="fa-brands fa-facebook-f"></i></a><a href="#" class="footer-social-btn"><i class="fa-brands fa-instagram"></i></a></div></div>
  <div><div class="footer-heading">Quick Links</div><ul class="footer-links"><li><a href="../index.html"><i class="fa fa-chevron-right"></i> Home</a></li><li><a href="../about.html"><i class="fa fa-chevron-right"></i> About Us</a></li><li><a href="../services.html"><i class="fa fa-chevron-right"></i> Services</a></li><li><a href="../project.html"><i class="fa fa-chevron-right"></i> Projects</a></li></ul></div>
  <div><div class="footer-heading">Services</div><ul class="footer-links">
    <li><a href="../services.html"><i class="fa fa-chevron-right"></i> PEB Design & Engineering</a></li>
    <li><a href="../services.html"><i class="fa fa-chevron-right"></i> Fabrication & Manufacturing</a></li>
    <li><a href="../services.html"><i class="fa fa-chevron-right"></i> Installation & Erection</a></li>
    <li><a href="../services.html"><i class="fa fa-chevron-right"></i> Turnkey Solutions</a></li>
    <li><a href="../services.html"><i class="fa fa-chevron-right"></i> Industrial Shed & Warehouse</a></li>
    <li><a href="../services.html"><i class="fa fa-chevron-right"></i> Pre Engineered Buildings</a></li>
    <li><a href="../services.html"><i class="fa fa-chevron-right"></i> Z & C Purlins</a></li>
    <li><a href="../services.html"><i class="fa fa-chevron-right"></i> Ceiling System</a></li>
  </ul></div>
  <div><div class="footer-heading">Contact</div><ul class="footer-contact-list"><li class="footer-contact-item"><span class="icon"><i class="fa fa-location-dot"></i></span><span>NS-11, BIADA Gate No.5, Patliputra Industrial Area, Patna – 800013</span></li><li class="footer-contact-item"><span class="icon"><i class="fa fa-phone"></i></span><div><a href="tel:+917463843731">+91 74638 43731</a><br><a href="tel:+919229893797">+91 92298 93797</a></div></li><li class="footer-contact-item"><span class="icon"><i class="fa fa-envelope"></i></span><div><a href="mailto:Info@aishra.in">Info@aishra.in</a></div></li></ul></div>
</div></div></div>
<div class="footer-bottom"><div class="container"><div class="footer-bottom-inner"><span>© <script>document.write(new Date().getFullYear())</script> <span class="hl">Aishra Technofab Engineers</span>. All rights reserved.</span><span>www.aishra.in</span></div></div></div></footer>

<div class="modal-overlay" id="quoteModal"><div class="modal-box">
  <button class="modal-close" onclick="closeModal()"><i class="fa fa-times"></i></button>
  <h2 class="modal-title">Request a Quote</h2><p class="modal-subtitle">We'll respond within 24 hours.</p>
  <div class="form-group"><label class="form-label">Full Name</label><input type="text" class="form-input" placeholder="Your full name"></div>
  <div class="form-group"><label class="form-label">Phone</label><input type="tel" class="form-input" placeholder="+91 XXXXX XXXXX"></div>
  <div class="form-group"><label class="form-label">Service Required</label><select class="form-select">
    <option value="">Select a service</option>
    <option>PEB Design & Engineering</option>
    <option>Fabrication & Manufacturing</option>
    <option>Installation & Erection</option>
    <option>Turnkey Solutions</option>
    <option>Industrial Shed & Warehouse</option>
    <option>Pre Engineered Buildings</option>
    <option>Z & C Purlins</option>
    <option>Ceiling System</option>
    <option>Other</option>
</select></div>
  <div class="form-group"><label class="form-label">Message</label><textarea class="form-textarea" placeholder="Describe your project..."></textarea></div>
  <button class="btn-primary" style="width:100%;justify-content:center;"><i class="fa fa-paper-plane"></i> Submit Request</button>
</div></div>
<script>
window.addEventListener("load",()=>{setTimeout(()=>document.getElementById("pageLoader").classList.add("hidden"),700);});
document.getElementById("navToggle").addEventListener("click",()=>{document.getElementById("navLinks").classList.toggle("open");});
document.addEventListener("click",(e)=>{const nav=document.getElementById("navLinks");const tog=document.getElementById("navToggle");if(nav.classList.contains("open")&&!nav.contains(e.target)&&!tog.contains(e.target)){nav.classList.remove("open");}});
function openModal(){document.getElementById("quoteModal").classList.add("active");document.body.style.overflow="hidden";}
function closeModal(){document.getElementById("quoteModal").classList.remove("active");document.body.style.overflow="";}
document.getElementById("quoteModal").addEventListener("click",(e)=>{if(e.target===document.getElementById("quoteModal"))closeModal();});
document.addEventListener("keydown",(e)=>{if(e.key==="Escape")closeModal();});
const obs=new IntersectionObserver(entries=>entries.forEach(e=>{if(e.isIntersecting)e.target.classList.add("visible");}),{threshold:0.1});
document.querySelectorAll(".reveal").forEach(el=>obs.observe(el));
(function(){
  var items=document.querySelectorAll('.has-dd');
  items.forEach(function(item){
    var link=item.querySelector('a.has-dropdown');
    link.addEventListener('click',function(e){
      if(window.innerWidth<=768){e.preventDefault();item.classList.toggle('dd-open');}
    });
  });
  document.addEventListener('click',function(e){
    items.forEach(function(item){if(item && !item.contains(e.target))item.classList.remove('dd-open');});
  });
})();
</script>
</body></html>
"""

import os

os.makedirs("products", exist_ok=True)

# Generate Application 3 Images properly
app_images = ["app_warehouse.png", "app_factory.png", "app_airport.png"]

for slug, data in products.items():
    title = data["title"]
    # split title for the hero span, e.g. first two words
    words = title.split()
    if len(words) > 1:
        split1 = " ".join(words[:len(words)//2])
        split2 = " ".join(words[len(words)//2:])
    else:
        split1 = ""
        split2 = title
    
    # Generate Benefits HTML
    benefits_html = ""
    for b in data["benefits"]:
        benefits_html += f'<div class="design-item"><i class="fa fa-check-circle" style="color:var(--primary);margin-right:8px;"></i> {b}</div>\n      '
        
    # Generate Apps HTML
    apps_html = ""
    for idx, app in enumerate(data["apps"]):
        img = app_images[idx]
        apps_html += f'''<div class="product-app-card reveal reveal-delay-{idx}">
        <div class="product-app-card-img"><img src="../images/{img}" alt="{app['title']}"></div>
        <div class="product-app-card-body">
            <div class="project-cat">{app['cat']}</div>
            <div class="product-app-card-name" style="font-size: 16px;">{app['title']}</div>
        </div>
      </div>\n      '''
        
    html = template
    html = html.replace("{title}", title)
    html = html.replace("{title_split_1}", split1)
    html = html.replace("{title_split_2}", split2)
    html = html.replace("{desc}", data["desc"])
    html = html.replace("{hero_img}", f"hero-{slug}.jpg")
    html = html.replace("{intro_img}", f"intro-{slug}.jpg")
    html = html.replace("{benefits_html}", benefits_html)
    html = html.replace("{apps_html}", apps_html)
    
    with open(f"products/{slug}.html", "w", encoding="utf-8") as f:
        f.write(html)
        print(f"Created products/{slug}.html")

print("All product pages generated successfully.")
