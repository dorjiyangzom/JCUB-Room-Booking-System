# JCUB-Room-Booking-System

# 🏫 JCUB Room Booking System (RBS)

## 📌 Overview
The **Room Booking System (RBS)** is a secure and user-friendly **web application** designed for **administrators, staff, and students** at JCUB.  
It provides **real-time room availability**, **instant booking/approval**, and **integration with JCUB's institutional calendar** to ensure smooth and conflict-free room reservations.

---

## ✨ Key Features
- 🔑 **Role-Based Access** – Separate permissions for Admin, Staff/Teacher, and Students.  
- ⚡ **Fast & Simple Booking** – One-click booking for power users and an intuitive form for detailed bookings.  
- 📅 **Real-Time Availability** – Instantly see available rooms and avoid scheduling conflicts.  
- 🛠️ **Equipment & Capacity Filtering** – Search by room size, equipment, or location.  
- 🔔 **Notifications & Sync** – Automatic email/calendar updates on booking confirmations or cancellations.  
- 🔗 **Timetable Integration** – Connects with JCUB’s trimester timetable for accurate scheduling.  

---

## 🧑‍💻 User Roles & Permissions
| Role      | Permissions |
|-----------|-------------|
| **Admin (Max 2)** | Create/Edit/Delete/View bookings, manage user roles, approve/reject bookings (auto-approval if no pending status), secure login, summarized dashboard |
| **Teacher/Staff** | Secure login, request bookings, view personal booking dashboard |
| **Student** | View room booking schedules (no login required) |

---

## ⚙️ Functional Requirements
| Code | Description |
|------|-------------|
| **FR1** | User authentication and role-based access |
| **FR2** | Dashboard with real-time availability and existing bookings |
| **FR3** | Booking form with date, time, room, purpose, equipment |
| **FR4** | Notification system for confirmation/cancellation (email/calendar sync) |
| **FR5** | Admin approval workflow for pending bookings |
| **FR6** | Integration with JCUB trimester timetable |
| **FR7** | Room filters by size, equipment, location |
| **FR8** | Booking history log per user |

---

## 🛡️ Non-Functional Requirements
- **NFR1**: Supports at least **100 concurrent users**  
- **NFR2**: Average response time **< 2 seconds**  
- **NFR3**: System uptime **> 99% per month**  
- **NFR4**: **Mobile-responsive**, intuitive interface  

---

## 🔧 Tech Stack (Suggested)
| Layer | Technology |
|------|------------|
| Frontend | React.js / Vue.js |
| Backend | Node.js / Django / Spring Boot |
| Database | MySQL / PostgreSQL |
| Authentication | JWT / OAuth 2.0 |
| Integration | JCUB Calendar/Timetable API |
| Hosting | AWS / Azure / On-Premise |

---

## 🚀 Installation & Setup
1. **Clone Repository**
   ```bash
   git clone https://github.com/your-org/jcub-rbs.git
   cd jcub-rbs
