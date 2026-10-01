# -*- coding: utf-8 -*-
import json, os

SERVICES_DIR = '/workspace/services'

ALL_SERVICES = [
    ("air-freight",        "Air Freight",           "fa-plane-departure"),
    ("sea-freight",        "Sea Freight",           "fa-ship"),
    ("customs-clearance",  "Customs Clearance",     "fa-file-invoice"),
    ("warehousing",        "Warehousing & Distribution", "fa-warehouse"),
    ("road-rail-freight",  "Road & Rail Freight",   "fa-truck-moving"),
    ("cargo-insurance",    "Cargo Insurance & Risk","fa-shield-alt"),
    ("ecommerce",          "E-commerce Logistics",  "fa-shopping-cart"),
]

def nav(active=None):
    links = []
    for href, label in [("../index.html#home","Home"), ("#services","Services"),
                        ("../index.html#about","About"), ("../index.html#process","Process"),
                        ("../index.html#industries","Industries"), ("../index.html#contact","Contact")]:
        cls = 'nav-link active' if (href=="#services") else 'nav-link'
        links.append(f'<li><a href="{href}" class="{cls}">{label}</a></li>')
    return "\n        ".join(links)

def footer_other(current_slug):
    items = []
    for slug, name, icon in ALL_SERVICES:
        if slug == current_slug: continue
        items.append(f'''<a href="{slug}.html" class="other-card"><i class="fas {icon}"></i><span>{name}<small>View service &rarr;</small></span></a>''')
    return "\n          ".join(items)

def build_page(slug, data):
    name = data['name']
    icon = data['icon']
    title = f'{name} | Fi-Gen Logistics'
    desc = data['meta_description']
    hero_img = data['hero_image']
    chips_html = "\n        ".join(f'<span class="hero-chip"><i class="fas {c[0]}"></i>{c[1]}</span>' for c in data['chips'])

    overview_cards = "\n        ".join(f'''<div class="feature-card reveal-up"><div class="fc-icon"><i class="fas {card["icon"]}"></i></div><h3>{card["title"]}</h3><p>{card["text"]}</p></div>''' for card in data['overview_cards'])

    feat_items = "\n            ".join(f'<li><i class="fas fa-check"></i>{f}</li>' for f in data['features'])

    steps_html = "\n        ".join(f'''<div class="step reveal-up"><div class="step-num"></div><div><h4>{s["title"]}</h4><p>{s["text"]}</p></div></div>''' for s in data['steps'])

    stats_html = "\n        ".join(f'''<div class="stat-item reveal-up"><div class="stat-number counter" data-target="{s["target"]}">0</div><div class="stat-desc">{s["desc"]}</div></div>''' for s in data['stats'])

    faq_html = "\n        ".join(f'''<details class="faq-item reveal-up"><summary>{q["q"]}</summary><div class="faq-body">{q["a"]}</div></details>''' for q in data['faqs'])

    prose_html = "\n          ".join(f'<p>{p}</p>' for p in data['overview_paras'])

    info_rows = "\n            ".join(f'<div class="info-row"><span>{k}</span><span>{v}</span></div>' for k,v in data['info_rows'])

    other_html = footer_other(slug)

    services_list_footer = "\n              ".join(
        f'<li><a href="{s}.html">{n}</a></li>' for s,n,_ in ALL_SERVICES)

    html_out = f'''<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="description" content="{desc}" />
  <meta name="keywords" content="{data['keywords']}" />
  <title>{title}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800;900&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet" />
  <link rel="icon" type="image/png" href="../logo.png" />
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css" />
  <link rel="stylesheet" href="../services.css" />
  <style>
    .page-hero {{ background-image: url('{hero_img}'); }}
    .cta-banner {{ background-image: url('{data["cta_image"]}'); }}
  </style>
</head>
<body>

  <nav id="navbar">
    <div class="nav-container">
      <a href="../index.html" class="nav-logo">
        <img src="../logo.png" alt="Fi-Gen Logo" />
      </a>
      <ul class="nav-links" id="navLinks">
        {nav()}
      </ul>
      <div class="nav-actions">
        <button id="themeToggle" class="theme-toggle" aria-label="Toggle theme">
          <span class="theme-icon sun"><i class="fas fa-sun"></i></span>
          <span class="theme-icon moon"><i class="fas fa-moon"></i></span>
        </button>
        <a href="../index.html#contact" class="btn btn-primary nav-cta">Get a Quote</a>
        <button class="hamburger" id="hamburger" aria-label="Menu">
          <span></span><span></span><span></span>
        </button>
      </div>
    </div>
  </nav>

  <header class="page-hero">
    <div class="container">
      <a href="../index.html#services" class="hero-crumb"><i class="fas fa-arrow-left"></i> Back to all services &nbsp;/&nbsp; <strong>{name}</strong></a>
      <h1>{data['hero_title']}</h1>
      <p class="hero-sub">{data['hero_sub']}</p>
      <div class="hero-chips">
        {chips_html}
      </div>
      <div class="hero-actions">
        <a href="../index.html#contact" class="btn btn-primary btn-lg"><i class="fas fa-paper-plane"></i> Request a Quote</a>
        <a href="mailto:support@fi-gen.com" class="btn btn-ghost btn-lg"><i class="fas fa-envelope"></i> Talk to an Expert</a>
      </div>
    </div>
  </header>

  <section class="section">
    <div class="container">
      <div class="split">
        <div class="reveal-up">
          <div class="section-tag">Overview</div>
          <h2 class="section-title">{data['overview_title']}</h2>
          <div class="prose">
          {prose_html}
          </div>
          <h3 class="subheading">What&rsquo;s included</h3>
          <ul class="feature-list">
            {feat_items}
          </ul>
        </div>
        <aside class="info-card reveal-up">
          <h3><i class="fas {icon}"></i> {name} at a Glance</h3>
          {info_rows}
          <a href="../index.html#contact" class="btn btn-primary"><i class="fas fa-paper-plane"></i> Get Started</a>
          <a href="tel:+919999999999" class="btn btn-ghost" style="margin-top:0.8rem;"><i class="fas fa-phone"></i> Need help? Contact us</a>
        </aside>
      </div>
    </div>
  </section>

  <section class="section section-alt">
    <div class="container">
      <div class="section-header reveal-up">
        <div class="section-tag">Capabilities</div>
        <h2 class="section-title">{data['capabilities_title']}</h2>
        <p class="section-subtitle">{data['capabilities_sub']}</p>
      </div>
      <div class="cards-grid">
        {overview_cards}
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-header reveal-up">
        <div class="section-tag">How It Works</div>
        <h2 class="section-title">Our <span class="gradient-text">{name}</span> Process</h2>
        <p class="section-subtitle">{data['process_sub']}</p>
      </div>
      <div class="steps">
        {steps_html}
      </div>
    </div>
  </section>

  <section class="stats-band">
    <div class="container">
      <div class="stats-grid">
        {stats_html}
      </div>
    </div>
  </section>

  <section class="section section-alt">
    <div class="container">
      <div class="section-header reveal-up">
        <div class="section-tag">FAQ</div>
        <h2 class="section-title">Frequently Asked <span class="gradient-text">Questions</span></h2>
        <p class="section-subtitle">Everything you need to know about our {name.lower()} services.</p>
      </div>
      <div class="faq-list">
        {faq_html}
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="cta-banner reveal-up" style="background-image:url('{data['cta_image']}')">
        <h2>Ready to move with {name}?</h2>
        <p>{data['cta_text']}</p>
        <a href="../index.html#contact" class="btn btn-primary btn-lg"><i class="fas fa-paper-plane"></i> Get Your Free Quote</a>
      </div>
    </div>
  </section>

  <section class="section section-alt">
    <div class="container">
      <div class="section-header reveal-up">
        <div class="section-tag">Explore</div>
        <h2 class="section-title">Other <span class="gradient-text">Services</span></h2>
      </div>
      <div class="other-grid">
        {other_html}
      </div>
    </div>
  </section>

  <footer class="footer">
    <div class="footer-top">
      <div class="container">
        <div class="footer-grid">
          <div class="footer-brand">
            <a href="../index.html" class="nav-logo">
              <img src="../logo.png" alt="Fi-Gen Logo" />
            </a>
            <p class="footer-brand-desc">Your trusted partner for global freight forwarding, customs clearance and e-commerce logistics. 25+ years of professional excellence, zero errors, and 24/7 support.</p>
            <div class="footer-social">
              <a href="#" class="social-link" aria-label="LinkedIn"><i class="fab fa-linkedin-in"></i></a>
              <a href="#" class="social-link" aria-label="WhatsApp"><i class="fab fa-whatsapp"></i></a>
              <a href="#" class="social-link" aria-label="Twitter"><i class="fab fa-twitter"></i></a>
            </div>
          </div>
          <div class="footer-links-col">
            <h4>Services</h4>
            <ul>
              {services_list_footer}
            </ul>
          </div>
          <div class="footer-links-col">
            <h4>Company</h4>
            <ul>
              <li><a href="../index.html#about">About Us</a></li>
              <li><a href="../index.html#process">Our Process</a></li>
              <li><a href="../index.html#industries">Industries</a></li>
              <li><a href="../index.html#contact">Contact</a></li>
            </ul>
          </div>
          <div class="footer-links-col">
            <h4>Get In Touch</h4>
            <ul class="footer-contact-list">
              <li><i class="fas fa-map-marker-alt"></i> 64/38/1, Kalathumedu, Woraiyur, Trichy &ndash; 620003</li>
              <li><i class="fas fa-envelope"></i> support@fi-gen.com</li>
              <li><i class="fas fa-file-alt"></i> declarations@fi-gen.com</li>
              <li><i class="fas fa-clock"></i> 24/7 &mdash; Always Available</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
    <div class="footer-bottom">
      <div class="container">
        <p class="footer-copy">&copy; <span id="year"></span> Fi-Gen Logistics. All rights reserved.</p>
        <p class="footer-copy-right">Designed with <i class="fas fa-heart"></i> for global trade</p>
      </div>
    </div>
  </footer>

  <script src="../services.js"></script>
</body>
</html>'''
    with open(os.path.join(SERVICES_DIR, slug + '.html'), 'w', encoding='utf-8') as f:
        f.write(html_out)
    print('wrote', slug + '.html')

PAGES = {}
