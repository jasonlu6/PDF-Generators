# PDF generator script for the technology bundles Cyber Monday 2025 November shopping. 

from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", "B", 8)
pdf.cell(0, 10, "USB-C Hubs/Docks with Ethernet & Display Output", ln=True, align="C")
pdf.ln(10)

pdf.set_font("Arial", "", 8)

# Table header
pdf.cell(60, 8, "#", 1)
pdf.cell(100, 8, "Product", 1)
pdf.cell(60, 8, "Price (USD)", 1)
pdf.cell(60, 8, "Rating", 1)
pdf.cell(60, 8, "URL", 1)
pdf.ln()

# Data rows
products = [
    (
        1,
        "HP USB-C Dock G5",
        "$144.99",
        "4.3/5",
        "https://www.hp.com/us-en/shop/pdp/hp-usb-c-dock-g5-p-26d32aa-abl-1",
    ),
    (
        2,
        "Belkin Universal USB-C 8-in-1 Dual Display Core Hub",
        "$139.99",
        "4.4/5",
        "https://www.belkin.com/p/universal-usb-c-8-in-1-dual-display-core-hub/INC015btSGY.html",
    ),
    (
        3,
        "Belkin 11-in-1 USB-C Hub Docking Station",
        "$123.99",
        "4.3/5",
        "https://www.bestbuy.com/product/belkin-11-in-1-usb-c-hub-with-4k-hdmi-dp-vga-100w-pd-docking-station-for-macbook-pro-air-and-more-dark-gray/JX5329KY4L/sku/6589124",
    ),
    (
        4,
        "j5create USB-C Dock Dual 4K HDMI + Ethernet",
        "$110.69",
        "3.4/5",
        "https://www.officedepot.com/a/products/9865335/j5create-Docking-station-USB-C-USB4/",
    ),
    (
        5,
        "Lenovo ThinkPad Universal USB-C Dock 40AY0090US",
        "$197.99",
        "4.3/5",
        "https://www.lenovo.com/us/en/p/accessories-and-software/docking/docking-usb-docks/40ay0090us",
    ),
    (
        6,
        "C2G USB-C 6-in-1 Mini Dock HDMI + Ethernet",
        "$26.99",
        "3.8/5",
        "https://www.dell.com/en-us/shop/c2g-usb-c-6-in-1-dual-display-docking-station-60w-power-supply-hdmi-ethernet-usb-35mm-audio-and-power-delivery-4k-30hz/apd/aa524857/docks",
    ),
    (
        7,
        "Dockteck 7-in-1 USB-C Hub Ethernet + Dual Monitor",
        "$41.99",
        "5.0/5",
        "https://www.dockteck.com/products/7-in-1-multiport-adapter-usb-c-hub-etherne?variant=41100258574388",
    ),
    (
        8,
        "Cable Matters USB-C Multiport Adapter Dual DisplayPort + Ethernet",
        "$25.00",
        "-",
        "https://www.ebay.com/itm/336077909611",
    ),
]

for p in products:
    pdf.cell(60, 8, str(p[0]), 1)
    pdf.cell(100, 8, p[1][:40], 1)
    pdf.cell(60, 8, p[2], 1)
    pdf.cell(60, 8, p[3], 1)
    pdf.cell(60, 8, "Link", 1, link=p[4])
    pdf.ln()

pdf.output("usb_c_hubs_with_ethernet_display.pdf")
print("PDF created: usb_c_hubs_with_ethernet_display.pdf")
