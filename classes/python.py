from store import Store
from product import Product

if __name__ == '__main__':
    ranch99 = Store( "99ranch" )
    # print( ranch99.name )
    # print( 'working...' )

    water = Product( "Water", 1, "Drinks")
    ranch99.add_product( water )

    banana = Product( 'Banana', 1, 'Fruit' )
    ranch99.add_product( banana )

    ranch99.product_list_info()

    ranch99.inflation( 1.00 )

    ranch99.product_list_info()

    ranch99.set_clearance( "Drinks", 0.5 )

    ranch99.product_list_info()
