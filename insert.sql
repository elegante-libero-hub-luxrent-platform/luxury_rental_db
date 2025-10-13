INSERT INTO users (username, email, password_hash, membership_level)
VALUES
('alice_w', 'alice@example.com', 'hash_1234', 'silver'),
('bob_chen', 'bob@example.com', 'hash_5678', 'basic'),
('carol_z', 'carol@example.com', 'hash_91011', 'gold');

INSERT INTO user_profiles (user_id, full_name, phone_number, address, profile_picture_url)
VALUES
(1, 'Alice Wang', '123-456-7890', '123 Market St, San Francisco, CA', 'https://example.com/alice.jpg'),
(2, 'Bob Chen', '234-567-8901', '456 Broadway, New York, NY', 'https://example.com/bob.jpg'),
(3, 'Carol Zhang', '345-678-9012', '789 Sunset Blvd, Los Angeles, CA', 'https://example.com/carol.jpg');

INSERT INTO membership_history (user_id, old_level, new_level)
VALUES
(1, 'basic', 'silver'),
(3, 'silver', 'gold');
