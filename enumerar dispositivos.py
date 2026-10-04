import hid
for dev in hid.enumerate():
    print(hex(dev['vendor_id']), hex(dev['product_id']), dev['product_string'])
