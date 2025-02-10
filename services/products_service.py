from repositories.products_repository import ProductRepository
class ProductService:
  @staticmethod
  def create_product(name, description):
    return ProductRepository.create_product(name, description)
  def update_product(name, new_name, description):
    return ProductRepository.update_product(name, new_name, description)