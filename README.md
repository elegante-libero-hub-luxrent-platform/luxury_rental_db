# User & Profile Database (Sprint 1)

This repository contains the relational schema and connectivity test for the **User & Profile microservice** of the Luxury Fashion Rental Platform.  
The database is deployed on **Google Cloud SQL (MySQL 8.0)** and manages user accounts, profiles, and membership levels.

---

## 🗂️ Database Overview
**Database name:** `user_profile_db`

| Table | Purpose | Key Columns |
|--------|----------|-------------|
| `users` | Stores basic account and membership info | `user_id`, `username`, `email`, `membership_level`, `created_at` |
| `user_profiles` | Stores personal details and contact information | `profile_id`, `user_id`, `full_name`, `phone_number`, `address`, `profile_picture_url` |
| `membership_history` | Tracks changes in membership level over time | `history_id`, `user_id`, `old_level`, `new_level`, `changed_at` |

---

## 🔗 Relationships
- `user_profiles.user_id → users.user_id`  (**1 : 1**) – each user has one profile  
- `membership_history.user_id → users.user_id`  (**1 : N**) – a user can have many membership changes  

### ER Diagram
```mermaid
erDiagram
    USERS {
        int user_id PK
        varchar username
        varchar email
        enum membership_level
        timestamp created_at
    }

    USER_PROFILES {
        int profile_id PK
        int user_id FK
        varchar full_name
        varchar phone_number
        varchar address
        varchar profile_picture_url
    }

    MEMBERSHIP_HISTORY {
        int history_id PK
        int user_id FK
        enum old_level
        enum new_level
        timestamp changed_at
    }

    USERS ||--o| USER_PROFILES : has
    USERS ||--o{ MEMBERSHIP_HISTORY : has
