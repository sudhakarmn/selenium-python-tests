def test_get_all_products(product_client):
    response = product_client.get("/products")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_get_single_product(product_client):
    response = product_client.get("/products/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1
