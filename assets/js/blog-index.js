/**
 * Sort blog index cards within each row by data-published (ISO date).
 */
(function () {
  "use strict";

  var section = document.getElementById("blog");
  if (!section) return;

  var toolbar = section.querySelector(".blog-index-toolbar");
  if (!toolbar) return;

  var buttons = toolbar.querySelectorAll("[data-blog-sort]");
  var rows = section.querySelectorAll(".row.g-4");

  function sortRow(row, order) {
    var cols = Array.prototype.slice.call(
      row.querySelectorAll(":scope > .col-md-6, :scope > .col-lg-4")
    );
    var withCards = cols.filter(function (col) {
      return col.querySelector(".blog-index-card[data-published]");
    });
    if (withCards.length < 2) return;

    withCards.sort(function (a, b) {
      var da = a.querySelector(".blog-index-card").getAttribute("data-published");
      var db = b.querySelector(".blog-index-card").getAttribute("data-published");
      if (da === db) return 0;
      return order === "newest" ? (da < db ? 1 : -1) : da < db ? -1 : 1;
    });

    withCards.forEach(function (col) {
      row.appendChild(col);
    });
  }

  function applySort(order) {
    rows.forEach(function (row) {
      sortRow(row, order);
    });
  }

  buttons.forEach(function (btn) {
    btn.addEventListener("click", function () {
      var order = btn.getAttribute("data-blog-sort");
      buttons.forEach(function (b) {
        var active = b === btn;
        b.classList.toggle("active", active);
        b.setAttribute("aria-pressed", active ? "true" : "false");
      });
      applySort(order);
    });
  });

  applySort("newest");
})();
