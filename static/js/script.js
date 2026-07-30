document.addEventListener('DOMContentLoaded', function () {
  var tabs = document.querySelectorAll('.gallery-tab');
  var items = document.querySelectorAll('.gallery-item');

  if (!tabs.length || !items.length) return;

  tabs.forEach(function (tab) {
    tab.addEventListener('click', function () {
      var filter = tab.getAttribute('data-filter');

      tabs.forEach(function (t) { t.classList.remove('is-active'); });
      tab.classList.add('is-active');

      items.forEach(function (item) {
        var matches = filter === 'all' || item.getAttribute('data-type') === filter;
        item.classList.toggle('is-hidden', !matches);
      });
    });
  });
});
