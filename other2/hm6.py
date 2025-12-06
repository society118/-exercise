#N1
full_name = lambda s1,s2: s1 + " " + s2
print(full_name("gleb","linux"))
#N2
products = [('Яблуко', 2.5), ('Банан', 1.8), ('Апельсин', 3.0)]
sorted_products = sorted(products,key =lambda product: product[1])
print(sorted_products)
#N3
books = [
  {'title': 'Python Guide', 'price': 150, 'is_available': True},
    {'title': 'Data Science Basics', 'price': 220, 'is_available': False},
    {'title': 'Web Development', 'price': 95, 'is_available': True}
]

new_books =list(filter(lambda b:b["is_available"],books))
discount_books = list(map(lambda b: (b , {'price': round(b['price'] * 0.9, 2)}), new_books))
print(discount_books)