const basketButton = document.getElementById("basket");
const stockDiv = document.getElementById("stock");

basketButton.addEventListener("click", () => {
  const quantity = parseInt(document.getElementById("quantity").value);
  const currentStock = parseInt(stockDiv.innerText.split(": ")[1]);
  const newStock = currentStock - quantity;
});