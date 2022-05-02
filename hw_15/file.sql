-- Table 'administrators'

CREATE Table administrators (id SERIAL PRIMARY KEY, login VARCHAR(50), password VARCHAR(50));

-- Table 'readers'

CREATE Table readers (id SERIAL PRIMARY KEY, first_name VARCHAR(50), 
                        last_name VARCHAR(50), passport VARCHAR(50), 
                        address VARCHAR(50), phone VARCHAR(50));

-- Table 'books'

CREATE Table books (id SERIAL PRIMARY KEY, autor VARCHAR(50), 
                        publisher VARCHAR(50), year_of_publication INTEGER, 
                        book_name VARCHAR(50), isbn VARCHAR(50));

-- Table 'librarians'

CREATE Table librarians (id SERIAL PRIMARY KEY, login VARCHAR(50), password VARCHAR(50));

-- Table 'booking_cards'

CREATE Table booking_cards (id SERIAL PRIMARY KEY, id_reader INTEGER, 
                        id_book INTEGER, id_librarian INTEGER,
                        time TIMESTAMP,
                        foreign key (id_reader) references readers(id) on delete cascade,
                        foreign key (id_book) references books(id) on delete cascade,
                        foreign key (id_librarian) references librarians(id) on delete cascade);

-- Table 'books_issue_card'

CREATE Table books_issue_card (id SERIAL PRIMARY KEY, id_reader INTEGER, 
                        id_book INTEGER, time TIMESTAMP, 
                        term TIMESTAMP,
                        foreign key (id_reader) references readers(id) on delete cascade,
                        foreign key (id_book) references books(id) on delete cascade);

-- Table 'rooms'

CREATE Table rooms (id SERIAL PRIMARY KEY, room_name VARCHAR(50));

-- Table 'books_placement'

CREATE Table books_placement (id SERIAL PRIMARY KEY, id_book INTEGER, 
                        id_room INTEGER, book_count INTEGER, 
                        shelf_number INTEGER,
                        foreign key (id_book) references books(id) on delete cascade,
                        foreign key (id_room) references rooms(id) on delete cascade);