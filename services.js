/* ============================================================
   FI-GEN LOGISTICS — SERVICE PAGES SCRIPT (services.js)
   ============================================================ */
(function () {
  // Theme toggle (shared with homepage preference key)
  var html = document.documentElement;
  var savedTheme = localStorage.getItem('theme') || localStorage.getItem('figenTheme') || 'dark';
  html.setAttribute('data-theme', savedTheme);

  var themeToggle = document.getElementById('themeToggle');
  if (themeToggle) {
    themeToggle.addEventListener('click', function () {
      var current = html.getAttribute('data-theme');
      var next = current === 'dark' ? 'light' : 'dark';
      html.setAttribute('data-theme', next);
      localStorage.setItem('theme', next);
      localStorage.setItem('figenTheme', next);
    });
  }

  // Mobile menu
  var hamburger = document.getElementById('hamburger');
  var navLinksContainer = document.getElementById('navLinks');
  if (hamburger && navLinksContainer) {
    hamburger.addEventListener('click', function () {
      hamburger.classList.toggle('active');
      navLinksContainer.classList.toggle('active');
    });
    document.querySelectorAll('.nav-link').forEach(function (link) {
      link.addEventListener('click', function () {
        hamburger.classList.remove('active');
        navLinksContainer.classList.remove('active');
      });
    });
  }

  // Scroll reveal
  var revealElements = document.querySelectorAll('.reveal-up');
  if ('IntersectionObserver' in window) {
    var observer = new IntersectionObserver(function (entries, obs) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('active');
          obs.unobserve(entry.target);
        }
      });
    }, { rootMargin: '0px 0px -80px 0px' });
    revealElements.forEach(function (el) { observer.observe(el); });
  } else {
    revealElements.forEach(function (el) { el.classList.add('active'); });
  }

  // Counter animation
  var counters = document.querySelectorAll('.counter');
  if ('IntersectionObserver' in window && counters.length) {
    var counterObserver = new IntersectionObserver(function (entries, obs) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          var counter = entry.target;
          var target = +counter.getAttribute('data-target');
          var duration = 2000;
          var increment = target / (duration / 16);
          var current = 0;
          var update = function () {
            current += increment;
            if (current < target) {
              counter.innerText = Math.ceil(current).toLocaleString();
              requestAnimationFrame(update);
            } else {
              counter.innerText = target.toLocaleString();
            }
          };
          update();
          obs.unobserve(counter);
        }
      });
    }, { rootMargin: '0px 0px -50px 0px' });
    counters.forEach(function (c) { counterObserver.observe(c); });
  }

  // Footer year
  var yearEl = document.getElementById('year');
  if (yearEl) yearEl.textContent = new Date().getFullYear();
})();
