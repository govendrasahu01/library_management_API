



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



