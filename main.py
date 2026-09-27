from pyscript import display
from js import document

def create_order(e):
    document.getElementById("order").innerHTML = ""
    item1 = document.getElementById("item1")
    item2 = document.getElementById("item2")
    item3 = document.getElementById("item3")
    item4 = document.getElementById("item4")
    item5 = document.getElementById("item5")

    subtotal = float(item1.value) * item1.checked + float(item2.value) * item2.checked + float(item3.value) * item3.checked +  float(item4.value) * item4.checked + float(item5.value) * item5.checked

    vat = subtotal * 0.12
    grand_total = subtotal + vat
    display(f"Subtotal: {subtotal}", f"VAT: {vat}", f"Grand Total: {grand_total}", target="order")

def sku_result(e):
        document.getElementById("output2").innerHTML=""

        category = document.getElementById("category")
        product = document.getElementById("product")
        stock = document.getElementById("stock")
        
        type_code = category.value
        squishy_name_value = product.value
        stock_quantity = stock.value

        sku = type_code + "-" + squishy_name_value + "-" + stock_quantity

        display("Generated SKU:" + sku, target="output2")