#   GYM MANAGEMENT SYSTEM WITH SMS SUPPORT

The D'Grit Gym Management System with SMS support is a desktop application aim to enhance the fitness center's communication efficiency, 
streamline operations, and improve gym member management. The system includes a QR code for  member and employee attendance. With the use of SMS, 
this creative system may provide timely attendance notifications, automate duties, and communicate with gym members via SMS, reminders for gym membership 
plans,and analytics. Reduced operating costs, better communication, more satisfaction among members, improved security of information. 

1. Account Management
2. Membership Management with renewal(1-month only)
3. Employee Management
4. Trainer Management
5. Equipment Inventory

# Requirements For Installation
- pip install -r Requirements.txt
- if it doesn't work, check the packages in setup.py and install them manually
- Username - Admin#11
- Password - Admin#11

  Note:
  - Every Account Registered has only 1 role.
  - Semaphore API key is required for sending sms.
  - Only the registered account's contact number will only recieve the OTP for resetting the username and password.
  - username and password must be mixed with uppercase and lowercase, numbers and symbols.
  - When the end_date is reached, the status of the member will automatically expire and the qr code will be denied in the qr attendance.
  - If the status of the trainer and employee is inactive, the qr attendance will deny the qr code.
  - Press Q to close the scanner.
 
 ![1](https://github.com/user-attachments/assets/60de062c-7d55-46ed-94f0-2cd6c9c0ef91)
