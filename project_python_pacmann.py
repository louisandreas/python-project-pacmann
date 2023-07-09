# -*- coding: utf-8 -*-
"""Project Python Pacmann.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KsOKnGzjdjJd3bkXHs9LzTVGk124F2qp
"""

#fungsi untuk perhitungan total price
def calculate_total_price(items):
    total_price = 0
    for item in items:
        item_total = item['quantity'] * item['price']
        item['total'] = item_total
        total_price += item_total
    return total_price

#fungsi untuk membuat transaction id
def generate_transaction_id(counter):
    return f"Order{counter:03}"

#fungsi untuk edit item
def edit_item(item):
    item_name = input("Masukkan nama barang: ")
    item_quantity = int(input("Masukkan quantity barang: "))
    item_price = float(input("Masukkan harga barang: "))

    item['name'] = item_name
    item['quantity'] = item_quantity
    item['price'] = item_price

#fungsi untuk delete item
def delete_item(items):
    item_index = int(input("Masukkan barang nomor berapa yang ingin dihapus: "))
    if item_index < 1 or item_index > len(items):
        print("Salah memasukkan nomor")
    else:
        del items[item_index - 1]
        print("Barang dihapus")

#fungsi untuk delete all item
def delete_all_items(items):
    confirm = input("Apakah anda yakin mau menghapus seluruh barang? (ya/tidak): ")
    if confirm.lower() == 'ya':
        items.clear()
        print("Seluruh barang dihapus")

#fungsi untuk perhitungan diskon
def apply_discount(total_price):
    discount = 0
    if total_price > 500000:
        discount = 0.10
    elif total_price > 300000:
        discount = 0.08
    elif total_price > 200000:
        discount = 0.05
    return discount

#fungsi untuk cek ulang receipt setelah lakukan edit item
def recheck_receipt(items, total_price, discount, discounted_price):
    print("\n----- Updated Receipt -----")
    print("{:<5} {:<15} {:<10} {:<10} {:<10}".format("No.", "Item", "Quantity", "Price", "Total"))
    for i, item in enumerate(items, start=1):
        print("{:<5} {:<15} {:<10} {:<10.2f} {:<10.2f}".format(i, item['name'], item['quantity'], item['price'], item['total']))
    print("---------------------------")
    print(f"Total Harga: {total_price}")
    print(f"Diskon: {discount * 100:.2f}%")
    print(f"Harga setelah diskon: {discounted_price}")

#fungsi utama input item
def main():
    transaction_counter = 1
    items = []

    while True:
        item_name = input("Masukkan nama barang (atau 'stop' apabila sudah selesai): ")
        if item_name == 'stop':
            break

        item_quantity = int(input("Masukkan quantity barang: "))
        item_price = float(input("Masukkan harga barang: "))

        item = {
            'name': item_name,
            'quantity': item_quantity,
            'price': item_price
        }
        items.append(item)

    total_price = calculate_total_price(items)
    discount = apply_discount(total_price)
    discounted_price = total_price - (total_price * discount)

    transaction_id = generate_transaction_id(transaction_counter)

    #print receipt
    print("\n----- Receipt -----")
    print(f"Transaction ID: {transaction_id}")
    print("{:<5} {:<15} {:<10} {:<10} {:<10}".format("No.", "Item", "Quantity", "Price", "Total"))
    for i, item in enumerate(items, start=1):
        print("{:<5} {:<15} {:<10} {:<10.2f} {:<10.2f}".format(i, item['name'], item['quantity'], item['price'], item['total']))
    print("---------------------------")
    print(f"Total Harga: {total_price}")
    print(f"Diskon: {discount * 100:.2f}%")
    print(f"Harga setelah diskon: {discounted_price}")


    #cek ulang receipt untuk memberikan pilihan edit atau hapus item
    while True:
        recheck_receipt(items, total_price, discount, discounted_price)
        check_input = input("Cek total belanja? (ya/tidak): ")
        if check_input.lower() != 'ya':
            break

        option = input("Apakah ada lagi yang ingin ditambahkan? \n1. Edit barang \n2. Tambah barang \n3. Hapus barang \n4. Hapus seluruh barang \n5. Lanjut \nPilihan: ")
        if option == '1':
            item_index = int(input("Masukkan barang nomor berapa yang ingin diedit: "))
            if item_index < 1 or item_index > len(items):
                print("Salah memasukkan nomor")
            else:
                edit_item(items[item_index - 1])
                total_price = calculate_total_price(items)
                discount = apply_discount(total_price)
                discounted_price = total_price - (total_price * discount)
        elif option == '2':
            item_name = input("Masukkan nama barang: ")
            item_quantity = int(input("Masukkan quantity barang: "))
            item_price = float(input("Masukkan harga barang: "))

            new_item = {
                'name': item_name,
                'quantity': item_quantity,
                'price': item_price
            }
            items.append(new_item)
            total_price = calculate_total_price(items)
            discount = apply_discount(total_price)
            discounted_price = total_price - (total_price * discount)
        elif option == '3':
            delete_item(items)
            total_price = calculate_total_price(items)
            discount = apply_discount(total_price)
            discounted_price = total_price - (total_price * discount)
        elif option == '4':
            delete_all_items(items)
            total_price = 0
            discount = 0
            discounted_price = 0
        elif option == '5':
            continue
        else:
            print("Pilihan tidak tersedia")

    print("Total Belanja Final")

if __name__ == "__main__":
    main()