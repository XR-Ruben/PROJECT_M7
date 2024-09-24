console.log("TEST-SCRIPT-JS")

function updateFilter(event, touch_is) {
  event.preventDefault();

  const form = document.getElementById("filters-form");
  form.submit();
}

console.log(`connect function - updateFilter ${updateFilter}`);