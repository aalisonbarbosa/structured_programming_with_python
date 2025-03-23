/*
Isabela Vitoriano foi contratada para desenvolver um sistema para gestão da Universidade ABC. Abaixo temos uma relação de 3 tabelas que são
necessárias para o sistema.
• Alunos (MAT, nome, endereço, cidade)
• Disciplinas (COD_DISC, nome_disc, carga_hor)
• Professores (COD_PROF, nome, endereco, cidade)
Consultas a serem criadas:
• Crie cada uma das 3 tabelas (o sublinhado significa chave primária)
• Faça ao menos 3 inserções em cada uma das tabelas
• Listar todos os alunos
• Listar todas as disciplinas
• Listar todos os professores
• Listar todos os alunos que residem em Campina Grande
• Listar todos os alunos que possuem algum sobrenome Abella
• Listar os dados do aluno que possui matrícula 1
• Listar o nome do aluno que possui matrícula 1
• Listar as disciplinas que possuem carga horária maior ou igual a 60
• Listar as disciplinas que possuem no seu nome a palavra PYTHON
• Listar todos os professores que residem em Campina Grande
*/

create table alunos (
	matricula int auto_increment,
    nome varchar(100),
    endereco varchar(100),
    cidade varchar(50),
    primary key(matricula)
);

create table professores (
	codigo int auto_increment,
    nome varchar(100),
    endereco varchar(100),
    cidade varchar(50),
    primary key(codigo)
);

create table disciplinas (
	codigo int auto_increment,
    nome varchar(100),
    carga_horaria float,
    primary key(codigo)
);

insert into alunos (nome,endereco,cidade)
values("alison","ibiranga","serrinha");

insert into alunos (nome,endereco,cidade)
values("mateus","juripiranga","serrinha");

insert into alunos (nome,endereco,cidade)
values("joão pedro","juripiranga","serrinha");

insert into professores (nome,endereco,cidade)
values("daniel abella","rua b","campina grande");

insert into professores (nome,endereco,cidade)
values("salatiel","rua a","itambé");

insert into professores (nome,endereco,cidade)
values("larisa souza","rua c","serrinha");

insert into disciplinas (nome,carga_horaria)
values("programação estruturada em python", 120);

insert into disciplinas (nome,carga_horaria)
values("matemática", 200);

insert into disciplinas (nome,carga_horaria)
values("português", 200);

select * from alunos;
select * from professores;
select * from disciplinas;
select * from alunos where cidade = "campina grande";
select * from alunos where nome like "%abella%";
select * from alunos where matricula = 1;
select nome from alunos where matricula = 1;
select * from disciplinas where carga_horaria >= 60;
select * from disciplinas where nome like "%python%";
select * from professores where cidade = "campina grande";