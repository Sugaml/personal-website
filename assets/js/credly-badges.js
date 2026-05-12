/**
 * Renders Credly digital badges from same-origin JSON (see assets/data/credly-badges.json).
 * Regenerate JSON after new badges: curl -sS "https://www.credly.com/users/babulal-tamang/badges.json" | python3 scripts/refresh-credly-badges.py
 */
(function () {
  function escapeHtml(str) {
    if (str == null || str === '') return '';
    var div = document.createElement('div');
    div.textContent = str;
    return div.innerHTML;
  }

  function refreshAos() {
    if (typeof AOS !== 'undefined' && AOS.refresh) {
      AOS.refresh();
    }
  }

  var root = document.getElementById('credly-badges-root');
  if (!root) return;

  var src = root.getAttribute('data-credly-src') || 'assets/data/credly-badges.json';
  var profileFallback =
    'https://www.credly.com/users/babulal-tamang/badges#credly';

  function failHtml() {
    return (
      '<div class="col-12 text-center">' +
      '<p class="text-muted mb-2">Badge list could not be loaded.</p>' +
      '<a class="btn btn-outline-primary btn-sm" href="' +
      profileFallback +
      '" target="_blank" rel="noopener noreferrer">Open Credly profile</a>' +
      '</div>'
    );
  }

  fetch(src, { credentials: 'same-origin' })
    .then(function (r) {
      if (!r.ok) throw new Error('bad status');
      return r.json();
    })
    .then(function (data) {
      var badges = data.badges;
      if (!Array.isArray(badges) || badges.length === 0) {
        root.innerHTML = failHtml();
        refreshAos();
        return;
      }

      var profileUrl = data.profileUrl || profileFallback;
      var html = badges
        .map(function (b) {
          var name = escapeHtml(b.name || '');
          var issuer = b.issuer || '';
          var issued = b.issued || '';
          var desc = escapeHtml(b.description || '');
          var img = escapeHtml(b.imageUrl || '');
          var href = escapeHtml(b.assertionUrl || '');
          var metaText = issued
            ? 'Issued ' + issued + (issuer ? ' · ' + issuer : '')
            : issuer;

          return (
            '<div class="col-lg-4 col-md-6" data-aos="fade-up">' +
            '<article class="card h-100 credly-badge-card position-relative">' +
            '<div class="credly-badge-img-wrap">' +
            '<img class="credly-badge-img" src="' +
            img +
            '" alt="' +
            name +
            ' badge" loading="lazy" width="200" height="200">' +
            '</div>' +
            '<div class="card-body d-flex flex-column">' +
            '<h4 class="card-title credly-badge-title">' +
            name +
            '</h4>' +
            (metaText
              ? '<p class="credly-meta mb-2">' + escapeHtml(metaText) + '</p>'
              : '') +
            (desc ? '<p class="card-text credly-badge-desc flex-grow-1">' + desc + '</p>' : '') +
            '</div>' +
            '<a href="' +
            href +
            '" class="stretched-link" target="_blank" rel="noopener noreferrer">' +
            '<span class="visually-hidden">View ' +
            name +
            ' on Credly</span></a>' +
            '</article></div>'
          );
        })
        .join('');

      html +=
        '<div class="col-12 text-center mt-2"><a class="btn btn-outline-primary btn-sm" href="' +
        escapeHtml(profileUrl) +
        '#credly" target="_blank" rel="noopener noreferrer">All badges on Credly</a></div>';

      root.innerHTML = html;
      refreshAos();
    })
    .catch(function () {
      root.innerHTML = failHtml();
      refreshAos();
    });
})();
