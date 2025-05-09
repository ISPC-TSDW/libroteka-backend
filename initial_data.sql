-- Borra datos de todas las tablas relacionadas
DELETE FROM Book;
DELETE FROM Author;
DELETE FROM Genre;
DELETE FROM Editorial;
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

--Insertar Libros
INSERT INTO Book 
(id_Author, id_Genre, id_Editorial, avg_rating, image, title, description, price, stock, ISBN, year)
VALUES
(79, 25, 41, 0.0, 'http://res.cloudinary.com/dfuuhiqto/image/upload/v1746747203/iptz1v0lmwcbg74dwdww.jpg', 'Cien años de soledad', 'Una obra maestra de Gabriel García Márquez que sigue la historia de la familia Buendía en el mítico pueblo de Macondo. A través de generaciones, la novela explora temas como la soledad, el amor, la violencia y el poder, envueltos en un realismo mágico que mezcla lo extraordinario con lo cotidiano.', 29.99, 100, '9780307474728', 1967),

(80, 25, 40, 0.0, 'http://res.cloudinary.com/dfuuhiqto/image/upload/v1746747535/lgxgit7ocftg9g0ma4nc.jpg', 'La casa de los espíritus', 'Una novela que explora la historia de una familia chilena.', 19.99, 150, '9788433963662', 1982),

(81, 28, 43, 0.0, 'http://res.cloudinary.com/dfuuhiqto/image/upload/v1746747265/tynr2vngae8pqusehhf1.jpg', 'Harry Potter y la piedra filosofal', 'El joven Harry descubre que es un mago y comienza su formación en Hogwarts, enfrentando secretos de su pasado y un oscuro enemigo.', 29.99, 200, '9788478888993', 1997),

(82, 28, 42, 0.0, 'http://res.cloudinary.com/dfuuhiqto/image/upload/v1746747206/usimnvavfbo3alvnoahd.jpg', 'El hobbit', 'Una aventura fantástica en la Tierra Media.', 22.50, 175, '9780261103344', 1937),

(83, 26, 44, 0.0, 'http://res.cloudinary.com/dfuuhiqto/image/upload/v1746747704/aukr5pm6oncda6hegqvs.jpg', 'El viejo y el mar', 'Una historia sobre la lucha entre el hombre y la naturaleza.', 18.00, 80, '9780140031448', 1952),

(84, 32, 42, 0.0, 'http://res.cloudinary.com/dfuuhiqto/image/upload/v1746747385/re09pcyq0izm0alg1jmu.jpg', 'It', 'Una novela de Terror psicológico sobre un grupo de amigos que enfrentan a una fuerza maligna que toma la forma de sus peores miedos.', 22.50, 100, '9780450411434', 1986),

(85, 28, 50, 0.0, 'http://res.cloudinary.com/dfuuhiqto/image/upload/v1746747537/r3dltljbmy2397re5tc7.jpg', 'El laberinto del fauno', 'En la España franquista, una niña llamada Ofelia se refugia en un mundo mágico para escapar de la cruda realidad que la rodea.', 17.99, 50, '9788490942624', 2006),

(86, 28, 46, 0.0, 'http://res.cloudinary.com/dfuuhiqto/image/upload/v1746747240/c7q2ukhnhcpbtjatjgnh.jpg', 'Corazón de tinta', 'Una emocionante aventura donde personajes de los libros cobran vida a través de la lectura en voz alta.', 24.99, 75, '9788415542279', 2003),

(87, 30, 52, 0.0, 'http://res.cloudinary.com/dfuuhiqto/image/upload/v1746747770/grcxne1kbp4ulqkjccto.jpg', 'El pasajero 23', 'Una novela de suspense sobre un crucero en el que se producen desapariciones misteriosas, lo que lleva al protagonista a descubrir oscuros secretos.', 18.99, 40, '9788483833560', 2016),

(88, 30, 42, 0.0, 'http://res.cloudinary.com/dfuuhiqto/image/upload/v1746747427/uioaavxw6bpcw97agswd.jpg', 'A la caza de Jack el Destripador', 'Ambientada en la época victoriana, una joven investiga los brutales crímenes de Jack el Destripador desafiando las convenciones de la sociedad.', 21.50, 90, '9780316273497', 2016),

(84, 30, 44, 0.0, 'http://res.cloudinary.com/dfuuhiqto/image/upload/v1746747484/vvn77gil8rxbcjzh7dmu.jpg', 'El Instituto', 'Luke Ellis es secuestrado y llevado a una institución donde otros niños tienen habilidades sobrenaturales.', 19.99, 80, '9781982110567', 2019),

(89, 31, NULL, 0.0, 'http://res.cloudinary.com/dfuuhiqto/image/upload/v1746747839/tphjpx17q6sn6oqgxgqb.jpg', 'Romeo y Julieta', 'Una tragedia sobre el amor prohibido entre dos jóvenes de familias rivales.', 18.99, 60, '9780451526861', 1597),

(89, 31, 45, 0.0, 'http://res.cloudinary.com/dfuuhiqto/image/upload/v1746747157/spbcgiwxzy7gkdonb4xi.jpg', 'Hamlet', 'Hamlet, príncipe de Dinamarca, busca vengar el asesinato de su padre en un ambiente de traición y locura.', 180.00, 20, '9780743477123', 1603),

(90, 31, 47, 0.0, 'http://res.cloudinary.com/dfuuhiqto/image/upload/v1746747326/fegud6z9evnfxay589km.jpg', 'Cumbres Borrascosas', 'La relación destructiva entre Catherine y Heathcliff, marcada por la obsesión y la venganza.', 180.00, 20, '9788420675712', 1847);
