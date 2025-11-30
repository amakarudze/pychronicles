def test_blog_homepage(client, blog_home):
    response = client.get("/blog/")
    assert response.status_code == 200
    