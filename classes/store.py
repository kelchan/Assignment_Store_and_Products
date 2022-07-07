from product import Product

class Store:
    def __init__( self, name ):
        self.name = name
        self.products_list = []

    def product_list_info( self ):
        for product in self.products_list:
            product.print_info()

    def add_product( self, new_product ):
        self.products_list.append( new_product )
        print( f"{new_product.name} has been added to the products list")
        return self

    def sell_product( self, id ):
        self.products_list[ id ].print_info()
        self.products_list.remove( id )
        print( f"{self.products_list[id]} has been removed from the products list")
        return self

    def inflation( self, percent_increase ):
        for product in self.products_list:
            product.price += product.price * percent_increase
        print( f"Inflation of {percent_increase}" )
        return self

    def set_clearance( self, category, percent_discount ):
        for product in self.products_list:
            if product.category == category:
                product.price -= product.price * percent_discount
        print( f"{percent_discount * 100}% discount has been applied to {category}" )
        return self



# water = Product( "Water", 1, "Drinks")
# ranch99.add_product( water )

