/* ============================================================
   FI-GEN LOGISTICS — SCRIPT.JS
   ============================================================ */

// ---- PRELOADER ----
window.addEventListener('load', () => {
  setTimeout(() => {
    const pre = document.getElementById('preloader');
    if (pre) pre.classList.add('loaded');
  }, 1600);
});

// ---- THEME TOGGLE ----
const html = document.documentElement;
const themeToggle = document.getElementById('themeToggle');
const savedTheme = localStorage.getItem('figenTheme') || 'dark';
html.setAttribute('data-theme', savedTheme);

themeToggle.addEventListener('click', () => {
  const current = html.getAttribute('data-theme');
  const next = current === 'dark' ? 'light' : 'dark';
  html.setAttribute('data-theme', next);
  localStorage.setItem('figenTheme', next);
});

// Set FormSubmit _next to current page so it redirects back after submit
const formNextUrl = document.getElementById('formNextUrl');
if (formNextUrl) {
  formNextUrl.value = window.location.href;
}

// ---- NAVBAR SCROLL & ACTIVE LINK ----
const navbar = document.getElementById('navbar');
const navLinks = document.querySelectorAll('.nav-link');
const sections = document.querySelectorAll('section[id]');

window.addEventListener('scroll', () => {
  // Scrolled state
  if (window.scrollY > 50) navbar.classList.add('scrolled');
  else navbar.classList.remove('scrolled');

  // Back to top
  const btt = document.getElementById('backToTop');
  if (window.scrollY > 400) btt.classList.add('visible');
  else btt.classList.remove('visible');

  // Active nav link
  let current = '';
  sections.forEach(sec => {
    const offset = sec.offsetTop - 120;
    if (window.scrollY >= offset) current = sec.id;
  });
  navLinks.forEach(link => {
    link.classList.remove('active');
    if (link.getAttribute('href') === '#' + current) link.classList.add('active');
  });
});

// ---- MOBILE MENU ----
const hamburger = document.getElementById('hamburger');
const mobileMenu = document.getElementById('navLinks');

hamburger.addEventListener('click', () => {
  hamburger.classList.toggle('open');
  mobileMenu.classList.toggle('open');
});
// Close on link click
mobileMenu.querySelectorAll('a').forEach(a => {
  a.addEventListener('click', () => {
    hamburger.classList.remove('open');
    mobileMenu.classList.remove('open');
  });
});

// ---- BACK TO TOP ----
document.getElementById('backToTop').addEventListener('click', () => {
  window.scrollTo({ top: 0, behavior: 'smooth' });
});

// ---- REVEAL ON SCROLL ----
const revealEls = document.querySelectorAll('.reveal-up, .reveal-left, .reveal-right');

const revealObs = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (!entry.isIntersecting) return;
    const el = entry.target;
    const delay = parseInt(el.getAttribute('data-delay') || '0');
    setTimeout(() => el.classList.add('in'), delay);
    revealObs.unobserve(el);
  });
}, { threshold: 0.12, rootMargin: '0px 0px -60px 0px' });

revealEls.forEach(el => revealObs.observe(el));

// ---- COUNTER ANIMATION ----
function animateCounter(el) {
  const target = parseInt(el.getAttribute('data-target'));
  const duration = 2000;
  const step = target / (duration / 16);
  let current = 0;
  const timer = setInterval(() => {
    current += step;
    if (current >= target) { current = target; clearInterval(timer); }
    el.textContent = Math.floor(current).toLocaleString();
  }, 16);
}

const counterObs = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (!entry.isIntersecting) return;
    animateCounter(entry.target);
    counterObs.unobserve(entry.target);
  });
}, { threshold: 0.5 });

document.querySelectorAll('.counter, .stat-num[data-target]').forEach(el => counterObs.observe(el));

// ---- CONTACT FORM ----
const contactForm = document.getElementById('contactForm');
const formSuccess = document.getElementById('formSuccess');

if (contactForm) {
  contactForm.addEventListener('submit', async (e) => {
    e.preventDefault();

    // Simple validation
    const required = contactForm.querySelectorAll('[required]');
    let valid = true;
    required.forEach(el => {
      el.style.borderColor = '';
      el.style.boxShadow = '';
      if (!el.value.trim()) {
        el.style.borderColor = '#ef4444';
        el.style.boxShadow = '0 0 0 3px rgba(239,68,68,0.15)';
        valid = false;
      }
    });
    if (!valid) return;

    // Show sending state
    const btn = contactForm.querySelector('button[type="submit"]');
    btn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Sending...';
    btn.disabled = true;

    try {
      const formData = new FormData(contactForm);
      const response = await fetch(contactForm.action, {
        method: 'POST',
        body: formData,
        headers: { 'Accept': 'application/json' }
      });

      if (response.ok) {
        contactForm.style.display = 'none';
        formSuccess.classList.add('visible');
      } else {
        throw new Error('Server error: ' + response.status);
      }
    } catch (err) {
      console.error('Form submission error:', err);
      btn.innerHTML = '<i class="fas fa-paper-plane"></i> Send Enquiry';
      btn.disabled = false;
      alert('Sorry, something went wrong. Please email us directly at support@fi-gen.com');
    }
  });

  // Clear error styling on input
  contactForm.querySelectorAll('input, select, textarea').forEach(el => {
    el.addEventListener('input', () => {
      el.style.borderColor = '';
      el.style.boxShadow = '';
    });
  });
}

// ---- FOOTER YEAR ----
const yearEl = document.getElementById('year');
if (yearEl) yearEl.textContent = new Date().getFullYear();

// ---- SMOOTH SCROLL for anchor links ----
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', (e) => {
    const target = document.querySelector(anchor.getAttribute('href'));
    if (target) {
      e.preventDefault();
      target.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  });
});
