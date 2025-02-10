from models.products import Products, db

class ProductRepository:
  @staticmethod
  def create_product(name, description):
    product = Products(name=name, description=description)

    db.session.add(product)
    db.session.commit()
    return product
  
  @staticmethod
  def update_product(name, new_name, description):

    product = db.session.execute(db.select(Products).filter_by(name=name)).scalar_one()
    if(new_name != None):
      product.name = new_name
    if(description != None):
      product.description = description

    db.session.commit()
    return product
  