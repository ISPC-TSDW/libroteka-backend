-- Script para insertar datos.
-- Insert into Author table
INSERT INTO author (name, country) VALUES
('Gabriel García Márquez','Colombia'),
('Isabel Allende','Chile'),
('J.K. Rowling','Reino Unido'),
('J.R.R. Tolkien','Reino Unido'),
('Ernest Hemingway','Estados Unidos'),
('Stephen King','Estados Unidos'),
('Guillermo Del Toro','México'),
('Cornelia Funke','Alemania'),
('Sebastian Fitzek','Alemania'),
('Kerri Maniscalco','Estados Unidos'),
('William Shakespeare','Inglaterra'),
('Emily Bronte','Inglaterra'),
('Mery Franco Carrion','España'),
('Paula Hawkins','Inglaterra'),
('Tim Dedopulos','Reino Unido'),
('Antoine De Saint Exupery','Francia'),
('Suzanne Collins','Estados Unidos'),
('Veronica Roth','Estados Unidos'),
('George Orwell','Reino Unido'),
('Ray Bradbury','Estados Unidos'),
('VV.AA.','Desconocido'),
('Jane Austen','Reino Unido'),
('John Green','Estados Unidos'),
('Anna Todd','Estados Unidos'),
('Bram Stoker','Irlanda'),
('H.P. Lovecraft','Estados Unidos');

-- Insert into Editorial table
INSERT INTO editorial (name) VALUES
('Editorial Planeta'),
('Anagrama'),
('Penguin Random House'),
('Ediciones Salamandra'),
('Lumen'),
('Library of American'),
('Impedimenta'),
('Paidós'),
('Caja Negra'),
('Gredos'),
('Legendary Comics y Norma Editorial'),
('Cah. P. Lovecraft y Francois de Regra'),
('Catedra');

-- Insert into Genre table
INSERT INTO genre (name) VALUES
('Novela'),
('Ficción'),
('Ciencia Ficción'),
('Fantasía'),
('Biografía'),
('Suspenso'),
('Drama'),
('Terror');


-- Insert into Books table
INSERT INTO book (title, id_Author_id , id_Genre_id, description, price, stock, id_Editorial_id, avg_rating) VALUES
('Cien años de soledad', 
    (SELECT id_Author FROM author WHERE name ='Gabriel García Márquez'),
    (SELECT id_Genre FROM genre WHERE name ='Novela'),
   'Una obra maestra de Gabriel García Márquez que sigue la historia de la familia Buendía en el mítico pueblo de Macondo. A través de generaciones, la novela explora temas como la soledad, el amor, la violencia y el poder, envueltos en un realismo mágico que mezcla lo extraordinario con lo cotidiano.', 
    29.99, 100, 
    (SELECT id_Editorial FROM editorial WHERE name ='Anagrama'), 0.0),
('La casa de los espíritus', 
    (SELECT id_Author FROM author WHERE name ='Isabel Allende'),
    (SELECT id_Genre FROM genre WHERE name ='Novela'),
   'Una novela que explora la historia de una familia chilena.', 
    19.99, 150, 
    (SELECT id_Editorial FROM editorial WHERE name ='Editorial Planeta'),
    0.0),
('Harry Potter y la piedra filosofal', 
    (SELECT id_Author FROM author WHERE name ='J.K. Rowling'), 
    (SELECT id_Genre FROM genre WHERE name ='Fantasía'), 
   'El joven Harry descubre que es un mago y comienza su formación en Hogwarts, enfrentando secretos de su pasado y un oscuro enemigo.', 
    29.99, 200, 
    (SELECT id_Editorial FROM editorial WHERE name ='Ediciones Salamandra'), 
    0.0),
('El hobbit', 
    (SELECT id_Author FROM author WHERE name ='J.R.R. Tolkien'),
    (SELECT id_Genre FROM genre WHERE name ='Fantasía'),
   'Una aventura fantástica en la Tierra Media.', 
    22.50, 175, 
    (SELECT id_Editorial FROM editorial WHERE name ='Penguin Random House'),
    0.0),
('El viejo y el mar', 
    (SELECT id_Author FROM author WHERE name ='Ernest Hemingway'),
    (SELECT id_Genre FROM genre WHERE name ='Ficción'),
   'Una historia sobre la lucha entre el hombre y la naturaleza.', 
    18.00, 80, 
    (SELECT id_Editorial FROM editorial WHERE name ='Lumen'),
    0.0),
('It', 
    (SELECT id_Author FROM author WHERE name ='Stephen King'), 
    (SELECT id_Genre FROM genre WHERE name ='Terror'), 
   'Una novela de Terror psicológico sobre un grupo de amigos que enfrentan a una fuerza maligna que toma la forma de sus peores miedos.', 
    22.50, 100, 
    (SELECT id_Editorial FROM editorial WHERE name ='Penguin Random House'), 
    0.0),
('El laberinto del fauno', 
    (SELECT id_Author FROM author WHERE name ='Guillermo Del Toro'), 
    (SELECT id_Genre FROM genre WHERE name ='Fantasía'), 
   'En la España franquista, una niña llamada Ofelia se refugia en un mundo mágico para escapar de la cruda realidad que la rodea.', 
    17.99, 50, 
    (SELECT id_Editorial FROM editorial WHERE name ='Legendary Comics y Norma Editorial'), 
    0.0),
('Corazón de tinta', 
    (SELECT id_Author FROM author WHERE name ='Cornelia Funke'), 
    (SELECT id_Genre FROM genre WHERE name ='Fantasía'), 
   'Una emocionante aventura donde personajes de los libros cobran vida a través de la lectura en voz alta.', 
    24.99, 75, 
    (SELECT id_Editorial FROM editorial WHERE name ='Impedimenta'), 
    0.0),
('El pasajero 23', 
    (SELECT id_Author FROM author WHERE name ='Sebastian Fitzek'), 
    (SELECT id_Genre FROM genre WHERE name ='Suspenso'), 
   'Una novela de suspense sobre un crucero en el que se producen desapariciones misteriosas, lo que lleva al protagonista a descubrir oscuros secretos.', 
    18.99, 40, 
    (SELECT id_Editorial FROM editorial WHERE name ='Cátedra'), 
    0.0),
('A la caza de Jack el Destripador', 
    (SELECT id_Author FROM author WHERE name ='Kerri Maniscalco'), 
    (SELECT id_Genre FROM genre WHERE name ='Suspenso'), 
   'Ambientada en la época victoriana, una joven investiga los brutales crímenes de Jack el Destripador desafiando las convenciones de la sociedad.', 
    21.50, 90, 
    (SELECT id_Editorial FROM editorial WHERE name ='Penguin Random House'),
    0.0),
('El Instituto', 
    (SELECT id_Author FROM author WHERE name ='Stephen King'), 
    (SELECT id_Genre FROM genre WHERE name ='Suspenso'), 
   'Luke Ellis es secuestrado y llevado a una institución donde otros niños tienen habilidades sobrenaturales.', 
    19.99, 80, 
    (SELECT id_Editorial FROM editorial WHERE name ='Lumen'),
    0.0),
('Romeo y Julieta', 
    (SELECT id_Author FROM author WHERE name ='William Shakespeare'),
    (SELECT id_Genre FROM genre WHERE name ='Drama'),
   'Una tragedia sobre el amor prohibido entre dos jóvenes de familias rivales.', 
    18.99, 60, 
    (SELECT id_Editorial FROM editorial WHERE name ='Library of America'),
    0.0),
('Hamlet',
    (SELECT id_Author FROM author WHERE name = 'William Shakespeare'),
    (SELECT id_Genre FROM genre WHERE name = 'Drama'),
    'Hamlet, príncipe de Dinamarca, busca vengar el asesinato de su padre en un ambiente de traición y locura.', 
    180, 20, (SELECT id_Editorial FROM editorial WHERE name = 'Library of American'), 0.0),
('Cumbres Borrascosas',
    (SELECT id_Author FROM author WHERE name = 'Emily Bronte'),
    (SELECT id_Genre FROM genre WHERE name = 'Drama'),
    'La relación destructiva entre Catherine y Heathcliff, marcada por la obsesión y la venganza.',
    180, 20, (SELECT id_Editorial FROM editorial WHERE name = 'Paidós'), 0.0),
('El silencio de los vencidos',
    (SELECT id_Author FROM author WHERE name = 'Mery Franco Carrion'),
    (SELECT id_Genre FROM genre WHERE name = 'Drama'),
    'Historia contemporánea de España durante la guerra.', 
    180, 20, (SELECT id_Editorial FROM editorial WHERE name = 'Lumen'), 0.0),
('El resplandor',
    (SELECT id_Author FROM author WHERE name = 'Stephen King'),
    (SELECT id_Genre FROM genre WHERE name = 'Terror'), 
    'Danny, con habilidades sobrenaturales, enfrenta visiones aterradoras en un hotel maldito.', 
    180, 20, (SELECT id_Editorial FROM editorial WHERE name = 'Library of American'), 0.0),
('La hora azul',
    (SELECT id_Author FROM author WHERE name = 'Paula Hawkins'),
    (SELECT id_Genre FROM genre WHERE name = 'Drama'), 
    'La escultura de una artista fallecida revela un secreto oscuro relacionado con su esposo desaparecido.', 
    180, 20, (SELECT id_Editorial FROM editorial WHERE name = 'Gredos'), 0.0),
('Juego de Tronos',
    (SELECT id_Author FROM author WHERE name = 'Tim Dedopulos'),
    (SELECT id_Genre FROM genre WHERE name = 'Drama'), 
    'Batallas por el trono en los siete reinos, en un mundo lleno de traiciones y magia.', 
    180, 20, (SELECT id_Editorial FROM editorial WHERE name = 'Catedra'), 0.0),
('El Principito',
    (SELECT id_Author FROM author WHERE name = 'Antoine De Saint Exupery'),
    (SELECT id_Genre FROM genre WHERE name = 'Drama'), 
    'Un pequeño príncipe viaja por el universo y reflexiona sobre el amor y la amistad.', 
    180, 20, (SELECT id_Editorial FROM editorial WHERE name = 'Catedra'), 0.0),
('Los Juegos del Hambre',
    (SELECT id_Author FROM author WHERE name = 'Suzanne Collins'),
    (SELECT id_Genre FROM genre WHERE name = 'Ciencia Ficción'), 
    'Katniss desafía al tiránico Capitolio en una sociedad dividida en 12 distritos.', 
    180, 20, (SELECT id_Editorial FROM editorial WHERE name = 'Gredos'), 0.0),
('Divergente',
    (SELECT id_Author FROM author WHERE name = 'Veronica Roth'),
    (SELECT id_Genre FROM genre WHERE name = 'Ciencia Ficción'), 
    'Una sociedad postapocalíptica donde las personas se dividen en facciones según su personalidad.', 
    180, 20, (SELECT id_Editorial FROM editorial WHERE name = 'Lumen'), 0.0),
('1984',
    (SELECT id_Author FROM author WHERE name = 'George Orwell'),
    (SELECT id_Genre FROM genre WHERE name = 'Drama'), 
    'En un futuro totalitario, el estado controla hasta la vida privada de los ciudadanos.', 
    180, 20, (SELECT id_Editorial FROM editorial WHERE name = 'Catedra'), 0.0),
('Fahrenheit 451',
    (SELECT id_Author FROM author WHERE name = 'Ray Bradbury'),
    (SELECT id_Genre FROM genre WHERE name = 'Ciencia Ficción'), 
    'En una sociedad donde los libros están prohibidos, un bombero cuestiona su rol de quemar libros.', 
    180, 20,
    (SELECT id_Editorial FROM editorial WHERE name = 'Legendary Comics y Norma Editorial'), 0.0),
('Dune',
    (SELECT id_Author FROM author WHERE name = 'VV.AA.'),
    (SELECT id_Genre FROM genre WHERE name = 'Ciencia Ficción'),
    'En un sistema feudal, la política galáctica gira en torno al control del planeta Dune.', 
    180, 20,
    (SELECT id_Editorial FROM editorial WHERE name = 'Library of American'), 0.0),
('Orgullo y Prejuicio',
    (SELECT id_Author FROM author WHERE name = 'Jane Austen'),
    (SELECT id_Genre FROM genre WHERE name = 'Drama'), 
    'La relación entre Elizabeth Bennet y Fitzwilliam Darcy debe superar el orgullo y los prejuicios.', 
    180, 20, (SELECT id_Editorial FROM editorial WHERE name = 'Caja Negra'), 0.0),
('Bajo la misma estrella',
    (SELECT id_Author FROM author WHERE name = 'John Green'),
    (SELECT id_Genre FROM genre WHERE name = 'Suspenso'), 
    'Hazel y Gus enfrentan su realidad con ironía y humor, mientras sueñan en circunstancias difíciles.', 
    180, 20, (SELECT id_Editorial FROM editorial WHERE name = 'Caja Negra'), 0.0),
('After',
    (SELECT id_Author FROM author WHERE name = 'Anna Todd'),
    (SELECT id_Genre FROM genre WHERE name = 'Drama'), 
    'Tessa, en su primer año de universidad, conoce a Hardin, un chico enigmático y rebelde.', 
    180, 20, (SELECT id_Editorial FROM editorial WHERE name = 'Library of American'), 0.0),
('Drácula', 
    (SELECT id_Author FROM author WHERE name = 'Bram Stoker'),
    (SELECT id_Genre FROM genre WHERE name = 'Terror'), 
    'El Conde Drácula busca extender su dominio desde Transilvania.', 
    180, 20, (SELECT id_Editorial FROM editorial WHERE name = 'Library of American'), 0.0),
('La llamada de Cthulhu',
    (SELECT id_Author FROM author WHERE name = 'H.P. Lovecraft'),
    (SELECT id_Genre FROM genre WHERE name = 'Fantasía'), 
    'Un culto oculto revela los misterios de Cthulhu a través de las investigaciones de Francis Thurston.', 
    180, 20, (SELECT id_Editorial FROM editorial WHERE name = 'Cah. P. Lovecraft y Francois de Regra'), 0.0);

-- Update existing books with ISBN, year, and image information

-- 1. Cien años de soledad
UPDATE book SET 
    isbn = '9780307474728',
    year = 1967,
    image = NULL
WHERE title = 'Cien años de soledad' 
AND id_Author_id = (SELECT id_Author FROM author WHERE name = 'Gabriel García Márquez' LIMIT 1);

-- 2. La casa de los espíritus
UPDATE book SET 
    isbn = '9788433963662',
    year = 1982,
    image = NULL
WHERE title = 'La casa de los espíritus' 
AND id_Author_id = (SELECT id_Author FROM author WHERE name = 'Isabel Allende' LIMIT 1);

-- 3. Harry Potter y la piedra filosofal
UPDATE book SET 
    isbn = '9788478888993',
    year = 1997,
    image = NULL
WHERE title = 'Harry Potter y la piedra filosofal' 
AND id_Author_id = (SELECT id_Author FROM author WHERE name = 'J.K. Rowling' LIMIT 1);

-- 4. El hobbit
UPDATE book SET 
    isbn = '9780261103344',
    year = 1937,
    image = NULL
WHERE title = 'El hobbit' 
AND id_Author_id = (SELECT id_Author FROM author WHERE name = 'J.R.R. Tolkien' LIMIT 1);

-- 5. El viejo y el mar
UPDATE book SET 
    isbn = '9780140031448',
    year = 1952,
    image = NULL
WHERE title = 'El viejo y el mar' 
AND id_Author_id = (SELECT id_Author FROM author WHERE name = 'Ernest Hemingway' LIMIT 1);

-- 6. It
UPDATE book SET 
    isbn = '9780450411434',
    year = 1986,
    image = NULL
WHERE title = 'It' 
AND id_Author_id = (SELECT id_Author FROM author WHERE name = 'Stephen King' LIMIT 1);

-- 7. El laberinto del fauno
UPDATE book SET 
    isbn = '9788490942624',
    year = 2006,
    image = NULL
WHERE title = 'El laberinto del fauno' 
AND id_Author_id = (SELECT id_Author FROM author WHERE name = 'Guillermo Del Toro' LIMIT 1);

-- 8. Corazón de tinta
UPDATE book SET 
    isbn = '9788415542279',
    year = 2003,
    image = NULL
WHERE title = 'Corazón de tinta' 
AND id_Author_id = (SELECT id_Author FROM author WHERE name = 'Cornelia Funke' LIMIT 1);

-- 9. El pasajero 23
UPDATE book SET 
    isbn = '9788483833560',
    year = 2016,
    image = NULL
WHERE title = 'El pasajero 23' 
AND id_Author_id = (SELECT id_Author FROM author WHERE name = 'Sebastian Fitzek' LIMIT 1);

-- 10. A la caza de Jack el Destripador
UPDATE book SET 
    isbn = '9780316273497',
    year = 2016,
    image = NULL
WHERE title = 'A la caza de Jack el Destripador' 
AND id_Author_id = (SELECT id_Author FROM author WHERE name = 'Kerri Maniscalco' LIMIT 1);

-- 11. El Instituto
UPDATE book SET 
    isbn = '9781982110567',
    year = 2019,
    image = NULL
WHERE title = 'El Instituto' 
AND id_Author_id = (SELECT id_Author FROM author WHERE name = 'Stephen King' LIMIT 1);

-- 12. Romeo y Julieta
UPDATE book SET 
    isbn = '9780451526861',
    year = 1597,
    image = NULL
WHERE title = 'Romeo y Julieta' 
AND id_Author_id = (SELECT id_Author FROM author WHERE name = 'William Shakespeare' LIMIT 1);

-- 13. Hamlet
UPDATE book SET 
    isbn = '9780743477123',
    year = 1603,
    image = NULL
WHERE title = 'Hamlet' 
AND id_Author_id = (SELECT id_Author FROM author WHERE name = 'William Shakespeare' LIMIT 1);

-- 14. Cumbres Borrascosas
UPDATE book SET 
    isbn = '9788420675712',
    year = 1847,
    image = NULL
WHERE title = 'Cumbres Borrascosas' 
AND id_Author_id = (SELECT id_Author FROM author WHERE name = 'Emily Bronte' LIMIT 1);

-- 15. El silencio de los vencidos
UPDATE book SET 
    isbn = '9788466355951',
    year = 2021,
    image = NULL
WHERE title = 'El silencio de los vencidos' 
AND id_Author_id = (SELECT id_Author FROM author WHERE name = 'Mery Franco Carrion' LIMIT 1);

-- 16. El resplandor
UPDATE book SET 
    isbn = '9780307743657',
    year = 1977,
    image = NULL
WHERE title = 'El resplandor' 
AND id_Author_id = (SELECT id_Author FROM author WHERE name = 'Stephen King' LIMIT 1);

-- 17. La hora azul
UPDATE book SET 
    isbn = '9780735211209',
    year = 2021,
    image = NULL
WHERE title = 'La hora azul' 
AND id_Author_id = (SELECT id_Author FROM author WHERE name = 'Paula Hawkins' LIMIT 1);

-- 18. Juego de Tronos
UPDATE book SET 
    isbn = '9788498722218',
    year = 2014,
    image = NULL
WHERE title = 'Juego de Tronos' 
AND id_Author_id = (SELECT id_Author FROM author WHERE name = 'Tim Dedopulos' LIMIT 1);

-- 19. El Principito
UPDATE book SET 
    isbn = '9780156012195',
    year = 1943,
    image = NULL
WHERE title = 'El Principito' 
AND id_Author_id = (SELECT id_Author FROM author WHERE name = 'Antoine De Saint Exupery' LIMIT 1);

-- 20. Los Juegos del Hambre
UPDATE book SET 
    isbn = '9780439023528',
    year = 2008,
    image = NULL
WHERE title = 'Los Juegos del Hambre' 
AND id_Author_id = (SELECT id_Author FROM author WHERE name = 'Suzanne Collins' LIMIT 1);

-- 21. Divergente
UPDATE book SET 
    isbn = '9780062024039',
    year = 2011,
    image = NULL
WHERE title = 'Divergente' 
AND id_Author_id = (SELECT id_Author FROM author WHERE name = 'Veronica Roth' LIMIT 1);

-- 22. 1984
UPDATE book SET 
    isbn = '9780451524935',
    year = 1949,
    image = NULL
WHERE title = '1984' 
AND id_Author_id = (SELECT id_Author FROM author WHERE name = 'George Orwell' LIMIT 1);

-- 23. Fahrenheit 451
UPDATE book SET 
    isbn = '9781451673319',
    year = 1953,
    image = NULL
WHERE title = 'Fahrenheit 451' 
AND id_Author_id = (SELECT id_Author FROM author WHERE name = 'Ray Bradbury' LIMIT 1);

-- 24. Dune
UPDATE book SET 
    isbn = '9780441172719',
    year = 1965,
    image = NULL
WHERE title = 'Dune' 
AND id_Author_id = (SELECT id_Author FROM author WHERE name = 'VV.AA.' LIMIT 1);

-- 25. Orgullo y Prejuicio
UPDATE book SET 
    isbn = '9780141439518',
    year = 1813,
    image = NULL
WHERE title = 'Orgullo y Prejuicio' 
AND id_Author_id = (SELECT id_Author FROM author WHERE name = 'Jane Austen' LIMIT 1);

-- 26. Bajo la misma estrella
UPDATE book SET 
    isbn = '9780142424179',
    year = 2012,
    image = NULL
WHERE title = 'Bajo la misma estrella' 
AND id_Author_id = (SELECT id_Author FROM author WHERE name = 'John Green' LIMIT 1);

-- 27. After
UPDATE book SET 
    isbn = '9781501106408',
    year = 2014,
    image = NULL
WHERE title = 'After' 
AND id_Author_id = (SELECT id_Author FROM author WHERE name = 'Anna Todd' LIMIT 1);

-- 28. Drácula
UPDATE book SET 
    isbn = '9780486411095',
    year = 1897,
    image = NULL
WHERE title = 'Drácula' 
AND id_Author_id = (SELECT id_Author FROM author WHERE name = 'Bram Stoker' LIMIT 1);

-- 29. La llamada de Cthulhu
UPDATE book SET 
    isbn = '9788498006325',
    year = 1928,
    image = NULL
WHERE title = 'La llamada de Cthulhu' 
AND id_Author_id = (SELECT id_Author FROM author WHERE name = 'H.P. Lovecraft' LIMIT 1);