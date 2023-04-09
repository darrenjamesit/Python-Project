// Get references to the quantity and total elements
const quantity = document.getElementById("itemcount");
const total = document.getElementById("total");

// Listen for changes to the quantity input
quantity.addEventListener("change", function() {
  // Get the new quantity value
  const newQuantity = quantity.value;

  // Get the price from the data-price attribute
  const price = parseFloat(total.getAttribute("data-price"));

  // Calculate the new total price
  const newTotal = (newQuantity * price).toFixed(2);

  // Update the text of the total element
  total.textContent = "Total: " + newTotal + " RON";
});