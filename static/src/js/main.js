$(document).ready(function() {
  setInterval(function() {
    cache_clear()
  }, 10000);
});

function cache_clear() {
  window.location.reload(true);
}