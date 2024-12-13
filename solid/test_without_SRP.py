def test_add_user():
    db_connection = Database()
    user_manager = UserManager(db_connection)
    
    user_manager.add_user("john_doe", "password123")
    
    assert db_connection.query("SELECT * FROM users WHERE username = 'john_doe'") is not None