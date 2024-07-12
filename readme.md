Urls:


    Author Links -->

        List/Create of all Author:
            GET/POST: 'http://127.0.0.1:8000/author/'

        Single Author:
            GET: http://127.0.0.1:8000/auth-detail/{id}/

        Update Author:
            PUT/PATCH: 'http://127.0.0.1:8000/author/{id}/'

        Delete Author:
            DELETE: 'http://127.0.0.1:8000/author/{id}/'
    
    Book Links -->
        List/Create:
            GET/POST: 'http://127.0.0.1:8000/book/'

    Member Links -->
        List/Create:
            GET/POST: 'http://127.0.0.1:8000/member/'
        
        Member Detail with Borrowed books
            GET: 'http://127.0.0.1:8000/member-detail/{member_id}/'

    Loan Links -->
        List/Create:
            GET/POST: 'http://127.0.0.1:8000/borrow/'
        
        Return_loan:
            PATCH:  http://127.0.0.1:8000/return-book/{loan_id}/



Explanation Video Link:  https://youtu.be/laNgMOgTBgg?si=A_L1r_IbIt8MvnSv

📚 Library Management API Project Using Django Rest Framework (DRF) 📚

Excited to share my latest project: a comprehensive Library Management API built with Django Rest Framework (DRF)! 🚀

🔍 Project Overview:
This API efficiently handles various library management tasks, ensuring seamless interactions between different entities such as Authors, Books, Members, and Loans.

🔧 Key Functionalities:

Models Implementation:

Author: Manage author details.
Book: Handle book information.
Member: Keep track of library members.
Loan: Manage book borrowing and returns by members.
CRUD Operations:

Full CRUD operations for Authors, Books, and Members.
Book Borrowing and Return Management:

Members can borrow books, with borrowing records maintained in the Loan model.
Return management by updating the return date in the Loan model.
Author Details with Related Books:

Retrieve an author's details along with all their authored books.
Member Details with Borrowed and Returned Books:

Access a member's profile, including all borrowed and returned books.
💡 This project demonstrates my ability to build robust and scalable backend solutions using DRF, ensuring data integrity and efficient relationship management between different models.

Feel free to connect if you'd like to know more about this project or discuss potential collaborations! 🌟


Thank You For Visting My Project!

Govendra Sahu
govendrasahu01@gmail.com
+91 8770285038
