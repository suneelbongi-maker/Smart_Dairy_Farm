🐄 Smart Dairy Farm Management System

A simple and user-friendly web-based **Smart Dairy Farm Management System** developed using **Python, Flask, HTML, and CSS**.

This project helps dairy farmers manage cow details, milk production, cow health, feed records, and milk sales from a single dashboard.

---

📌 Project Overview

Managing a dairy farm manually can be difficult because information about cows, milk production, health, feed, and sales may be stored in different places.

The **Smart Dairy Farm Management System** provides a centralized system where farm information can be recorded, viewed, updated, and managed easily.

The application has a dashboard that provides an overview of important farm information.

---

✨ Features

🐄 Cow Management
- Add new cow details
- View registered cows
- Search cows
- Update cow information
- Delete cow records

🥛 Milk Production
- Record daily milk production
- Store morning milk quantity
- Store evening milk quantity
- Automatically calculate total milk production
- View milk production records

❤️ Cow Health Management
- Record cow health information
- Record health condition
- Record temperature
- Record treatment details
- Store next checkup date

🌿 Feed Management
- Add feed records
- Store feed name
- Record feed quantity
- Store feed price
- Record feed purchase date

💰 Milk Sales
- Add customer information
- Record milk quantity sold
- Store price per litre
- Automatically calculate total sales amount
- View sales records

📊 Dashboard
The dashboard displays:
- Total number of cows
- Today's milk production
- Milk sold
- Today's revenue
- Healthy cows
- Cows needing checkup
- Cows under treatment
- Quick action buttons

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Backend programming |
| Flask | Web application framework |
| HTML | Web page structure |
| CSS | Website design and styling |
| JSON | Data storage |
| VS Code | Development environment |
| Git & GitHub | Version control and project hosting |

                    ┌───────────────────────────┐
                    │          USER             │
                    │      Farmer / Admin       │
                    └─────────────┬─────────────┘
                                  │
                                  ▼
                    ┌───────────────────────────┐
                    │       WEB BROWSER         │
                    │     Google Chrome         │
                    └─────────────┬─────────────┘
                                  │
                                  ▼
              ┌─────────────────────────────────────┐
              │          FRONTEND LAYER              │
              │                                     │
              │        HTML + CSS                   │
              │                                     │
              │  Dashboard | Cows | Milk | Health  │
              │  Feed | Sales                       │
              └──────────────────┬──────────────────┘
                                 │
                                 ▼
              ┌─────────────────────────────────────┐
              │          APPLICATION LAYER           │
              │                                     │
              │          Python + Flask             │
              │                                     │
              │  • Add Records                      │
              │  • View Records                     │
              │  • Update Records                   │
              │  • Delete Records                   │
              │  • Search Records                   │
              │  • Calculate Milk & Revenue          │
              └──────────────────┬──────────────────┘
                                 │
                                 ▼
              ┌─────────────────────────────────────┐
              │             DATA LAYER               │
              │                                     │
              │             JSON Files              │
              │                                     │
              │  cows.json                           │
              │  milk.json                           │
              │  health.json                         │
              │  feed.json                           │
              │  sales.json                          │
              └─────────────────────────────────────┘
