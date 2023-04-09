const basketButton = document.getElementById("basket");
const stockDiv = document.getElementById("stock");

basketButton.addEventListener("click", () => {
  const quantity = parseInt(document.getElementById("quantity").value);
  const currentStock = parseInt(stockDiv.innerText.split(": ")[1]);
  const newStock = currentStock - quantity;

  if (quantity > 0 && newStock >= 0) {
    stockDiv.innerText = "Stock: " + newStock;
    alert("Item added to basket!");
  } else if (quantity <= 0) {
    alert("Please enter a valid quantity!");
  } else {
    alert("Not enough stock available!");
  }
});